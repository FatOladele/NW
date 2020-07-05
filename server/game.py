import gevent
import json 
from gevent import monkey
monkey.patch_all()
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send, rooms, join_room, close_room, leave_room
#import scrabble
import eventlet
scrabble = eventlet.import_patched('scrabble')
import multiprocessing
import threading
# import concurrent.futures
# import time
# Creating a flask app and using it to instantiate a socket object
game = Flask(__name__)
CORS(game, resources={r'/*':{'origin': '*'}})
game.config.from_object(__name__)
socketio = SocketIO(game, cors_allowed_origins="*", logger = True, ping_timeout = 300)
q = multiprocessing.Queue()
allRooms = {}
allgames = {}
activeGamers = {}
gamerInfo = {}
randgames = {}
global compdict 
compdict = {}
complist= {}
# def emitthread(msg, data, room, includeself):
#   emit(msg, data, room=room, include_self = includeself )

# Handler for a message recieved over 'connect' channel

def compthread(room, rule):
  print('compthread')
  gamedata = scrabble.game(room)
  activity = gamedata.compplay(rule)
  #return activity
  compdict[room] = activity
  # with open('compact.json', "r") as file:
  #   data = json.load(file)
  # data[room] = activity
  # with open('compact.json', "w") as file:
  #   json.dump(data, file)


@socketio.on('connect')
def test_connect():
  gamerId = 'Gamer'+str(scrabble.getGamerId())
  while gamerId in list(activeGamers.values()):
    gamerId = 'Gamer'+str(scrabble.getGamerId())
  emit('connected', {'gamernick': gamerId })
  activeGamers[request.sid] = gamerId 

@socketio.on('disconnect')
def on_disconnect():
  gamer = activeGamers[request.sid]
  try:
    room = gamerInfo[gamer]
    on_lroom({'room': room, 'gamerid': gamer})  
  except:
    pass
  del activeGamers[request.sid]

@socketio.on('create')
def on_create(data):
  """Create a game lobby"""
  time = data['time']
  rules = data['rules']
  creator = data['creator']
  observer = data['observer']
  language = data['language']
  room = scrabble.getRoom(time, rules, creator, observer, language)
  while room['id'] in list(allRooms.keys()):
    room = scrabble.getRoom(time, rules, creator, observer, language)
  allRooms[room['id']] = room['data']
  on_join({'room': room['id'], 'gamer': creator})
  #emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
  #print('created')
  #print(allRooms)


@socketio.on('randgame')
def on_randgame(data):
  noofplayer = data['noofplayers']
  noofplayer = [int(x) for x in noofplayer ]
  rules = data['rules']
  gamer = data['player']
  language = data['language']
  added = False
  room = ""
  time = 60
  roomid = ''
  for r in randgames:
    if (randgames[r]['noofplayers'] in noofplayer ) and (randgames[r]['rules'] in rules) and (randgames[r]['language'] == language):
      for s in randgames[r]['slot']:
        if randgames[r]['slot'][s]['nick'] == '':
          randgames[r]['slot'][s]['status'] = 'Ready'
          randgames[r]['slot'][s]['nick'] = gamer
          roomid = r
          added = True
          break
    if added:
      break
  if added:
    gamerInfo[gamer] = roomid
    join_room(roomid)
    allRooms[roomid] = randgames[roomid]
    emit('update_room',{'gameid': roomid, 'roomdata': randgames[roomid]}, room= roomid, include_self = True)
  else:
    room = scrabble.getRandRoom(time, rules[0], gamer, noofplayer[0], language )
    roomid = room['id']
    while room['id'] in list(allRooms.keys()):
      room = scrabble.getRandRoom(time, rules[0], gamer, noofplayer[0], language )
    gamerInfo[gamer] = roomid
    randgames[roomid] = room['data']
    allRooms[roomid] = room['data']
    join_room(roomid)
    emit('update_room',{'gameid': roomid, 'roomdata': randgames[roomid]}, room= roomid, include_self = True)
  roomfull = True
  slot = []
  for s in list(randgames[roomid]['slot'].keys()):
    if randgames[roomid]['slot'][s]['nick'] == '':
      roomfull = False
      break
    elif  randgames[roomid]['slot'][s]['type']  == 'Human':
      slot.append(s)
  if(roomfull):
    on_sgame({'room': roomid, 'slot': slot})


@socketio.on('vscomputer')
def on_vscomp(data):
  gamer = data['player']
  res = scrabble.getvscomp(data)
  room = res['rid']
  game =res['game']
  gamerInfo[gamer] = room
  join_room(room)
  emit('gid',{'gameid': room}, room= room, include_self = True)
  emit('game_start',game, room= room, include_self = True)
  gamedata = scrabble.game(room)
  gamedata.fillCompRack()

@socketio.on('ojoin')
def on_ojoin(data):
  room = data['room']
  gamer = data['gamer']
  if gamer in gamerInfo:
    if gamerInfo[gamer] != room:
      try:
        on_lroom({'room': gamerInfo[gamer], 'gamerid': gamer})
      except:
        del gamerInfo[gamer]
    else:
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
      return
  if room in allRooms:
    if (allRooms[room]['observe']):
      allRooms[room]['olist'].append(gamer)
      gamerInfo[gamer] = room
      join_room(room)
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
    else:
      emit('error', {'error': 'Unable to join room. Observers not allowed.'}, included_self = True)
  else:
    emit('error', {'error': 'Unable to join room. Room does not exist.'}, included_self = True)


@socketio.on('join')
def on_join(data):
  room = data['room']
  gamer = data['gamer']
  added = False
  if gamer in gamerInfo:
    if gamerInfo[gamer] != room:
      try:
        on_lroom({'room': gamerInfo[gamer], 'gamerid': gamer})
      except:
        del gamerInfo[gamer]
    else:
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
      return
  if room in allRooms:
    if allRooms[room]['creator'] == gamer:
      added = True
    else:
      for r in allRooms[room]['slot']:
        if allRooms[room]['slot'][r]['nick'] == '':
          allRooms[room]['slot'][r]['status'] = 'Not Ready'
          allRooms[room]['slot'][r]['nick'] = gamer
          added = True
          break
    if added:
      gamerInfo[gamer] = room
      join_room(room)
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
    else:
      emit('error', {'error': 'Unable to join room. Room is full.'}, included_self = True)
  else:
    emit('error', {'error': 'Unable to join room. Room does not exist.'}, included_self = True)


@socketio.on('toggle_slot')
def on_stoggle(data):
  room = data['room']
  slot = data['slot']
  newtype = data['info']
  allRooms[room]['slot'][slot] = newtype
  emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)

@socketio.on('leave_room')
def on_lroom(data):
  room = data['room']
  gamer = data['gamerid']
  try:
    game = scrabble.game(room)
    if(game.getplayers().length > 2):
      game.removeplayer(gamer)
    else:
      emit('left_room')
      emit('left_room', room= room,  include_self = False)
      close_room(room)
      game.deletegame()
      #emergencyend
      pass
  except:
    
    if allRooms[room]['creator'] == gamer:
      del allRooms[room]
      emit('left_room')
      emit('left_room', room= room,  include_self = False)
      close_room(room)
    else:
      for i in allRooms[room]['slot']:
        if (allRooms[room]['slot'][i]['nick'] == gamer):
          allRooms[room]['slot'][i] = { 'type': 'Human', 'status': 'Waiting', 'nick': '' }
      try:
        for i in randgames[room]['slot']:
          if (randgames[room]['slot'][i]['nick'] == gamer):
            randgames[room]['slot'][i] = { 'type': 'Human', 'status': 'Waiting', 'nick': '' }
      except:
        pass
      leave_room(room)
      del gamerInfo[gamer]
      emit('left_room')
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = False)

@socketio.on('p_ready')
def on_pready(data):
  room = data['room']
  gamer = data['gamerid']
  for i in allRooms[room]['slot']:
    if (allRooms[room]['slot'][i]['nick'] == gamer):
      allRooms[room]['slot'][i]['status'] = 'Ready'
      emit('update_room',{'gameid': room, 'roomdata': allRooms[room]}, room= room, include_self = True)
      return
  
@socketio.on('start_game')
def on_sgame(data):
  room = data['room']
  slot = data['slot']
  gamedata = allRooms[room]
  game = scrabble.startGame(gamedata, slot, room)
  allgames[room] = game
  emit('game_start',game, room= room, include_self = True)
  gamedata = scrabble.game(room)
  gamedata.fillCompRack()


@socketio.on('updated_rack')
def on_updaterack(data):
  room = data['room']
  print('update rack')
  print(room)
  gamedata = scrabble.game(room)
  bag = gamedata.getBagL()
  emit('update_bag',{'bag': bag}, room= room, include_self = True)
  
@socketio.on('played_game')
def on_playedgame(data):
  room = data['room']
  gamer =data['gamer']
  tonboard = data['tiles']
  pwords = data['pwords']
  pscore = data['score']
  rule = data['rule']
  gamedata = scrabble.game(room)
  turn = ''
  if rule == 'Custom':
    gameupdate = gamedata.customPlay(tonboard, pwords, pscore, gamer)
    emit('post_play', gameupdate, room=room, include_self = True )
    turn = gameupdate['turnnick']
  else: 
    board = gamedata.probegame(tonboard, pwords, pscore, gamer)
    emit('pre_play', {'board': board, 'gamer': gamer}, room=room, include_self = True )
    gamedata = scrabble.game(room)
    gameupdate = gamedata.compresponse()
    if gameupdate != 'wait' and gameupdate is not None :
      #t1 = threading.Thread(target=emitthread, args=('post_play', gameupdate,room, True ))
      print('emmiting postplay')
      emit('post_play', gameupdate, room=room, include_self = True )
      socketio.sleep(1)
      print('emmited postplay')
      #t1.start()
      #t1.join
      turn = gameupdate['turnnick']
  if turn == 'Computer':
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    #   comp = executor.submit(compthread, room, rule)
    #   activity = comp.result()
    # gamedata = scrabble.game(room)
    # activity = gamedata.compplay(rule)
    comp = threading.Thread(target=compthread, args=(room, rule))
    #comp = multiprocessing.Process(target=compthread, args=(room, rule))
    comp.start()
    complist[room] = comp
    print('computer is thinking')
    # while True:
    #   gevent.sleep(0)
    #   if not comp.is_alive():
    #     print(compdict)
    #     activity = compdict[room]
    #     print(activity)
    #     if activity['type'] == 'play':
    #       if rule ==  'Custom':
    #         game = activity['res']
    #         emit('post_play', game, room=room, include_self = True )
    #       else:
    #         board = activity['res']
    #         emit('pre_play', {'board': board, 'gamer': 'computer'}, room=room, include_self = True )
    #     elif activity['type'] == 'end':
    #       emit('pre_end', room=room, include_self = True)
    #     else:
    #       emit('pass_swap', activity['res'], room=room, include_self = True)
    #     print('breaking')
    #     
    
@socketio.on('get_comp')
def on_getcomp(data):
  room = data['room']
  rule = data['rule']
  comp = complist[room]
  while True:
    socketio.sleep(1)
    if not comp.is_alive():
      #print(compdict)
      #comp.join()
      activity = compdict[room]
      #activity = q.get()
      comp.join()
      # with open('compact.json', "r") as file:
      #   data = json.load(file)
      # activity = data[room]
      print(activity)
      if activity['type'] == 'play':
        if rule ==  'Custom':
          game = activity['res']
          emit('post_play', game, room=room, include_self = True )
          socketio.sleep(1)
        else:
          board = activity['res']
          emit('pre_play', {'board': board, 'gamer': 'computer'}, room=room, include_self = True )
          socketio.sleep(1)
      elif activity['type'] == 'end':
        
        emit('pre_end', room=room, include_self = True)
        socketio.sleep(1)
      else:
        
        emit('pass_swap', activity['res'], room=room, include_self = True)
        socketio.sleep(1)
      print('breaking')
      break


@socketio.on('res_probe')
def on_presponse(data):
  room = data['room']
  gamer =data['gamer']
  response = data['response']
  gamedata = scrabble.game(room)
  gameupdate = gamedata.presponse(gamer, response)
  if gameupdate != 'wait':
    emit('post_play', gameupdate, room=room, include_self = True )
    socketio.sleep(1)
    if gameupdate['turnnick'] == 'Computer':
      gamedata = scrabble.game(room)
      activity = gamedata.compplay()
      if activity['type'] == 'play':
        board = activity['res']
        emit('pre_play', {'board': board, 'gamer': 'computer'}, room=room, include_self = True )
      elif activity['type'] == 'end':
        emit('pre_end', room=room, include_self = True)
      else:
        emit('pass_swap', activity['res'], room=room, include_self = True)

@socketio.on('swapped')
def on_swapped(data):
  room = data['room']
  gamer = data['gamer']
  nswap = data['nswap']
  game = scrabble.game(room)
  res = game.swappass(gamer, 'swap', nswap)
  emit('pass_swap', res, room=room, include_self = True)
  socketio.sleep(1)
  if res['turnnick'] == 'Computer':
      gamedata = scrabble.game(room)
      activity = gamedata.compplay()
      if activity['type'] == 'play':
        board = activity['res']
        emit('pre_play', {'board': board, 'gamer': 'computer'}, room=room, include_self = True )
      elif activity['type'] == 'end':
        emit('pre_end', room=room, include_self = True)
      else:
        emit('pass_swap', activity['res'], room=room, include_self = True)


@socketio.on('passed')
def on_passed(data):
  room = data['room']
  gamer = data['gamer']
  game = scrabble.game(room)
  res = game.swappass(gamer, 'pass')
  if res == 'endgame':
    emit('pre_end', room=room, include_self = True)
    gamedata = scrabble.game(room)
    res =game.compend()
    if res != 'wait':
      emit('game_ended', res, room=room, include_self = True )
      game.deletegame()
  else:
    emit('pass_swap', res, room=room, include_self = True)
    socketio.sleep(1)
    if res['turnnick'] == 'Computer':
      gamedata = scrabble.game(room)
      activity = gamedata.compplay()
      if activity['type'] == 'play':
        board = activity['res']
        emit('pre_play', {'board': board, 'gamer': 'computer'}, room=room, include_self = True )
      elif activity['type'] == 'end':
        emit('pre_end', room=room, include_self = True)
      else:
        emit('pass_swap', activity['res'], room=room, include_self = True)


@socketio.on('end_game')
def on_endgame(data):
  room = data['room']
  emit('pre_end', room=room, include_self = True)
  game = scrabble.game(room)
  res =game.compend()
  if res != 'wait':
    emit('game_ended', res, room=room, include_self = True )
    game.deletegame()

@socketio.on('my_tiles')
def on_mytiles(data):
  room = data['room']
  rack = data['rack']
  gamer = data['gamer']
  game = scrabble.game(room)
  gameupdate = game.endgame(gamer, rack)
  if gameupdate != 'wait':
    emit('game_ended', gameupdate, room=room, include_self = True )
    game.deletegame()

@game.route('/api/played', methods = ['POST'])
def played():
  response = {}
  gamedata = request.get_json()
  board = gamedata['board']
  tiles = gamedata['tiles']
  rules = gamedata['rule']
  language = gamedata['language']
  word = scrabble.checkWords(tiles, board)
  res = word.cw()
  if res['status'] == 'failed':
    response = res
  else:
    wordplayed = []
    score = scrabble.getScore(res['msg'], tiles, language)
    wordplayed.append(res['msg']['mainword'])
    if(res['msg']['otho'] != 'none'):
      wordplayed.extend(list(res['msg']['otho'].values()))
    if rules == 'Custom':
      dictcheck = scrabble.checkDictionary(wordplayed, language)
      if dictcheck != True:
        response['status'] = 'failed'
        response['msg'] = 'One or more words not found in the dictionary'
        return jsonify(response)
    response['status'] = res['status']
    response['words'] = wordplayed
    response['score'] = score
  return jsonify(response)


@game.route('/api/refillrack', methods = ['POST'])
def refillrack():
  print('requested')
  response = {}
  gamedata = request.get_json()
  room = gamedata['id']
  rack = gamedata['rack']
  game = scrabble.game(room)
  nrack = game.refillRack(rack)
  response['rack'] = nrack
  response['status'] = 'success'
  print('updated rack')
  print(response)
  return jsonify(response)

@game.route('/api/swap', methods = ['POST'])
def swap():
  response = {}
  gamedata = request.get_json()
  room = gamedata['room']
  rack = gamedata['rack']
  swaptiles = gamedata['swaptiles']
  game = scrabble.game(room)
  nrack = game.swaptiles(rack, swaptiles)
  response['rack'] = nrack
  response['status'] = 'success'
  return jsonify(response)


if __name__ == '__main__':
  
  socketio.run(game, host = '0.0.0.0', debug= True)
  # socketio.run(game,host = '127.0.0.1', debug= True)
  manager = multiprocessing.Manager()
  #compdict = manager.dict()
