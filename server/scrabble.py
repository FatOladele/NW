import random
import string
import time
import os
import json
import copy
import itertools
import threading
import multiprocessing as mp
from materials import materials, dictionary, TW, DW, TL, DL
gamePath = os.path.join(os.path.dirname(__file__),'game.json')
letcode=  {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I":  9, "J": 10, "K": 11, "L": 12, "M": 13, "N":14, "O": 15}
def getKey(y, x):
  return str(list(letcode.keys())[list(letcode.values()).index(y + 1)]) + str(x +1)
output = mp.Queue()
# global  yWords
# yWords = dictionary()
# yWords = yWords.dictWords()
class checkWords:
  def __init__(self, nl, board):
    self.nl = nl
    self.emptyboard = True
    self.onstar = False
    try:
      self.board = self.reboard(board)
    except: 
      self.emptyboard = False
      self.board = board
    
  def cw(self):
    if (len(self.nl) > 1):
      return self.checkPlacement()
    else:
      return self.oneletter()
  def reboard(self, board):
    for i in range(len(board)):
      for j in range(len(board[i])):
        if( board[i][j] != 0):
          board[i][j] = board[i][j]['lp']
          self.emptyboard = False
    return board
  def oneletter(self):
    bcode = list(self.nl.keys())[0]
    y = letcode[bcode[0]] - 1
    x = int(bcode[1:]) -1
    plist = []
    cod = 0
    if ((self.emptyboard)):
      return { "status": 'failed', "msg": 'You must play a word'}
    else:
      if( ((y > 0) and (self.board[y-1][x] != 0)) or ((y < 14) and (self.board[y+1][x] != 0))):
        self.direction = 'y'
        plist.append(y)
        cod = x
      elif ( ((x>0) and (self.board[y][x - 1] != 0)) or ((x<14) and (self.board[y][x+1] != 0))):
        self.direction = 'x'
        plist.append(x)
        cod = y
      else:
        return { "status": 'failed', "msg": 'Letter not connected to any word'}
    return self.getWords(plist, cod, [])
  def checkPlacement(self):
    px = []
    py = []
    startX = 0
    startY = 0
    bcode = list(self.nl.keys())
    for i in range(len(bcode)):
      py.append((letcode[bcode[i][0]]) - 1)
      px.append(int(bcode[i][1:]) -1)
    dx = 0
    dy = 0
    for i in range(len(px)):
      if px[i] != px[0]:
        dx = 1
        self.direction = 'x'
      if px[i] == 7:
        startX = 1
    for i in range(len(py)):
      if py[i] != py[0]:
        dy = 1
        self.direction = 'y'
      if py[i] == 7:
        startY = 1
    if((startX == 1) and (startY == 1)):
      self.onstar = True
    if((dx > 0) and (dy > 0)):
      return { "status": 'failed', "msg": 'You can only play vertically or horizontally'}
    elif(self.emptyboard and (not(self.onstar))):
      return { "status": 'failed', "msg": 'Starting word must be on star'}
    else:
      return self.checkConnection(px, py)

  def checkConnection(self,px,py):
    if (self.direction == 'x'):
      px.sort()
      emptyX = [x for x in range(px[0],px[-1]) if x not in px]
      if(len(emptyX) > 0):
        for i in range(len(emptyX)):
          if(self.board[py[0]][emptyX[i]] == 0):
            return { "status": 'failed', "msg": 'Spaces in word'}
      return self.getWords(px,py[0],emptyX)
    elif(self.direction == 'y'):
      py.sort()
      emptyY = [y for y in range(py[0],py[-1]) if y not in py]
      if(len(emptyY) > 0):
        for i in range(len(emptyY)):
          if(self.board[emptyY[0]][px[0]] == 0):
            return { "status": 'failed', "msg": 'Spaces in word'}
      return self.getWords(py,px[0],emptyY)
  def getWords(self,plist, cod, elist ):
    words = {}
    pre = plist[0] - 1
    post = plist[-1] + 1
    new = 0
    while((new >= 0)):
      new = -1
      if pre>= 0:
        if (((self.direction =='y') and (self.board[pre][cod] != 0)) or ((self.direction =='x') and (self.board[cod][pre] != 0))):
          new += 1
          elist.append(pre)
          pre -= 1
      if post <= 14:
        if (((self.direction =='y') and (self.board[post][cod] != 0)) or ((self.direction =='x') and (self.board[cod][post] != 0))):
          new += 1
          elist.append(post)
          post += 1
    
    elist.extend(plist)
    elist
    elist.sort() 
    mw = []
    if(self.direction == 'x'):
      for m in elist:
        if(m in plist):
          key = self.getKey(cod, m)
          # key = str(list(letcode.keys())[list(letcode.values()).index(cod + 1)]) + str(m + 1)
          mw.append(self.nl[key])
        else:
          mw.append(self.board[cod][m])
    elif(self.direction == 'y'):
      for m in elist:
        if(m in plist):
          key = self.getKey(m, cod)
          mw.append(self.nl[key])
        else:
          mw.append(self.board[m][cod])

    words['mainword'] = mw
    othow = self.getOwords(plist, cod)
    words['otho'] = othow
    if ((othow == 'none') and (len(mw) == len(plist))and not(self.emptyboard)):
      return { "status": 'failed', "msg": 'word not connected'}
    else:
      return {"status": 'success', "msg": words}

  def getKey(self, y, x):
    return str(list(letcode.keys())[list(letcode.values()).index(y + 1)]) + str(x +1)
    
  def getOwords(self, plist, cod):
    owords = {}
    for p in range(len(plist)):
      new = 0
      letp = plist[p]
      pre = cod - 1
      post = cod + 1
      elist = []
      while((new >= 0)):
        new = -1
        if pre>= 0:
          if (((self.direction =='y') and (self.board[letp][pre] != 0)) or ((self.direction =='x') and (self.board[pre][letp] != 0))):
            new += 1
            elist.append(pre)
            pre -= 1
        if post <= 14:
          if (((self.direction =='y') and (self.board[letp][post] != 0)) or ((self.direction =='x') and (self.board[post][letp] != 0))):
            new += 1
            elist.append(post)
            post += 1 
      
      if len(elist) != 0:
        elist.append(cod)
        elist.sort()
        ow = []
        if(self.direction == 'x'):
          for m in elist:
            if(m == cod):
              key = self.getKey(m, letp)
              # key = str(list(letcode.keys())[list(letcode.values()).index(cod + 1)]) + str(m + 1)
              ow.append(self.nl[key])
            else:
              ow.append(self.board[m][letp])
        elif(self.direction == 'y'):
          for m in elist:
            if(m == cod):
              key = self.getKey(letp, m)
              ow.append(self.nl[key])
            else:
              ow.append(self.board[letp][m])
        owords[key] = ow

    if (owords != {}): 
      return owords 
    else:  
      return 'none'

def refillRack(rack, bag):
  nbag = bag
  while ((len(rack) < 7) and (len(nbag) > 0)):
    random.shuffle(nbag)
    rack.append(nbag.pop())
  return {'bag': nbag, 'rack': rack}

def getScore(words, tob, language):
  tilesonbord = copy.copy(tob)
  keys = list(tilesonbord.keys())
  dlkey = [x for x in keys if x in DL]
  dwkey = [x for x in keys if x in DW]
  tlkey = [x for x in keys if x in TL]
  twkey = [x for x in keys if x in TW]
  mwscore = 0
  othoscore = 0
  gameObject = materials(language)
  scores = gameObject.getscores()
  mainword = words['mainword']
  for i in dlkey:
    if tilesonbord[i] > 200: tilesonbord[i] = 200
    mwscore += scores[str(tilesonbord[i])]
  for i in tlkey:
    if tilesonbord[i] > 200: tilesonbord[i] = 200
    mwscore += 2 * scores[str(tilesonbord[i])]
  for i in mainword:
    if i > 200: i = 200
    mwscore += scores[str(i)]
  for i in dwkey:
    mwscore = mwscore * 2
  for i in twkey:
    mwscore = mwscore * 3
  if words['otho'] != 'none':
    othokeys = list(words['otho'].keys())
    for k in othokeys:
      if tilesonbord[k] > 200: tilesonbord[k] = 200
      if k in dlkey:
        othoscore += scores[str(tilesonbord[k])]
      elif k in tlkey:
        othoscore += 2 * scores[str(tilesonbord[k])]
      ow = 0
      for i in words['otho'][k]:
        if i > 200: i = 200
        ow += scores[str(i)]
      if k in dwkey:
        ow = ow * 2
      elif k in twkey:
        ow = ow * 3
      othoscore += ow

  return mwscore + othoscore     

def rerack(rack, tileonboard):
  for i in list(tileonboard.values()):
    if i > 200:
      i = 200
    rack.remove(i)
  return rack

def computerplay(board, rack, level, language):
  dictwords = dictionary(language)
  allwords = dictwords.dictWords()
  starttime = time.time()
  maxPoint = 1000
  if level == 1:
    maxPoint = 15
  elif level == 2:
    maxPoint = 30
  elif level == 3:
    maxPoint = 60
  elif level == 4:
    maxPoint = 200
  
  print(starttime)
  possibilities = (-1000,[],{})
  openslot = []
  for y, a in enumerate(board):
    for x, b in enumerate(a):
      if b != 0:
        if y < 14 and board[y+1][x] == 0:
          openslot.append((y + 1,x))
        if y > 0 and board[y-1][x] == 0:
          openslot.append((y - 1,x))
        if x < 14 and board[y][x + 1] == 0:
          openslot.append((y,x + 1))
        if x > 0 and board[y][x - 1] == 0:
          openslot.append((y,x -1))
  
  tileSlots = []
  if len(openslot) > 0:
    for (y,x) in list(set(openslot)):
      for lo in range(len(rack)):
        for hi in range(len(rack)):
          #Build a horizontal tileSlot
          horz = [((y, x), board[y][x], 'x')]
          loCount = 0
          hiCount = 0
          xPos, yPos = x-1, y
          #Build left
          while xPos > 0 and (loCount < lo or board[yPos][xPos] != 0):
            loCount += 1
            horz.insert(0, ((yPos, xPos), board[yPos][xPos], 'x'))
            xPos -= 1
          #Build right
          xPos, yPos = x+1, y
          while xPos < len(board) and (hiCount < hi or board[yPos][xPos] != 0):
            hiCount += 1
            horz.append(((yPos, xPos), board[yPos][xPos], 'x'))	
            xPos += 1	

          vert = [((y, x), board[y][x],'y')]
          loCount = 0
          hiCount = 0
          xPos, yPos = x, y-1
          #Build up
          while yPos > 0 and (loCount < lo or board[yPos][xPos] != 0):
            loCount += 1
            vert.insert(0, ((yPos, xPos), board[yPos][xPos],'y'))
            yPos -= 1
          #Build down
          xPos, yPos = x, y+1
          while yPos < len(board) and (hiCount < hi or board[yPos][xPos] != 0):
            hiCount += 1
            vert.append(((yPos, xPos), board[yPos][xPos],'y'))
            yPos += 1
          tileSlots.append(horz)
          tileSlots.append(vert)
    newtileslot = []
    sorttiles = {}
    for x in tileSlots:
      if (x not in newtileslot) and len(x) > 1:
        newtileslot.append(x)
        if str(len(x)) not in list(sorttiles.keys()):
          sorttiles[str(len(x))] = [x]
        else:
          sorttiles[str(len(x))].append(x)
    print('thinking')
    print(len(newtileslot))
    print(time.time()-starttime)
    #pool = mp.Pool(processes=4)
    #processes = [mp.Process(target =tileslotandwords, args=(sorttiles[x], [y for y in allwords if len(y)/3 == int(x)], rack, language, board, maxPoint)) for x in list(sorttiles.keys())]
    result = []
    for x in list(sorttiles.keys()):
      # thread = threading.Thread(target =tileslotandwords, args=(sorttiles[x], [y for y in allwords if len(y)/3 == int(x)], rack, language, board, maxPoint))
      # thread.start()
      # thread.join()
      poss = tileslotandwords(sorttiles[x], [y for y in allwords if len(y)/3 == int(x)], rack, language, board, maxPoint)
      result.append(poss)
      if(time.time()-starttime) > 7:
        break
    # for p in processes:
    #   p.start()
    # for p in processes:
    #   p.join()
    # result = [output.get() for p in processes]
    print(time.time()-starttime)
    for r in result:
      if r[0] > possibilities[0]:
        possibilities = r
    return possibilities
  else:
    for i in range(2, len(rack) +  1):
      for word in [x for x in allwords if len(x)/3 == i]:
        nword = [int(word[i:i+3]) for i in range(0,len(word),3) ]
        slots = [((7, 7), 0, 'x')]
        cnt = 1
        while cnt < i:
          slots.append(((7, 7 + cnt), 0, 'x'))
          cnt += 1
        played = canmakeword(slots, rack, nword)
        if played != False:
          gword = {}
          gword['mainword'] = nword
          gword['otho'] = 'none'
          score = getScore(gword, played, language)
          if score > possibilities[0] and score < maxPoint:
            possibilities = (score, [nword], played)
    print(time.time()-starttime)
    print(possibilities)
    return possibilities
def tileslotandwords(tileslot, words, rack, language, board, maxPoint):
  possibilities = (-1000,[],{})
  starttime = time.time()
  for word in words:
    for slots in tileslot:
      nword = [int(word[i:i+3]) for i in range(0,len(word),3) ]
      played = canmakeword(slots, rack, nword)
      if played != False:
        #check otho words
        gword = {}
        wordsplayed = []
        
        wordsplayed.append(nword)
        gword['mainword'] = nword
        owordlist = {}
        valid = True
        for tile, letter in played.items():
          oword = checkowords(slots[0][2], tile, letter, board, language)
          if oword == False:
            valid = False
            break
          elif oword == 'none':
            pass
          else:
            owordlist[tile] = oword
            wordsplayed.append(oword)
        if valid:
          if len(owordlist) > 0:
            gword['otho'] = owordlist
          else:
            if len(nword) == len(played):
              continue
            gword['otho'] = 'none'
          score = getScore(gword, played, language)
          if score > possibilities[0] and score < maxPoint:
            possibilities = (score, wordsplayed, played)
      if(time.time()-starttime) > 7:
        break
    if(time.time()-starttime) > 7:
        break
          
  return possibilities
    # output.put(possibilities)

def checkowords(direction, tile, letter, board, language):
  y = letcode[tile[0]] - 1
  x = int(tile[1:]) -1
  word = [letter]
  new = 1 
  letp = 0
  pre = 0
  post = 0
  if direction == 'x':
    letp = x
    pre = y - 1
    post = y + 1
  if direction == 'y':
    letp = y
    pre = x -1
    post = x+ 1
  while((new >= 0)):
    new = -1
    if pre>= 0:
      if (((direction =='y') and (board[letp][pre] != 0))) :
        new += 1
        word.insert(0,board[letp][pre] )
        pre -= 1
      if (((direction =='x') and (board[pre][letp] != 0))):
        new += 1
        word.insert(0,board[pre][letp] )
        pre -= 1
    if post <= 14:
      if (((direction =='y') and (board[letp][post] != 0))):
        new += 1
        word.append(board[letp][post])
        post += 1
      if (((direction =='x') and (board[post][letp] != 0))):
        new += 1
        word.append(board[post][letp])
        post += 1 
  if len(word) < 2:
    return 'none'
  else:
    if checkDictionary([word], language):
      return word
    else: return False


def canmakeword(slots, letters, word):
  let = copy.copy(letters)
  playtiles = {}
  for i in range(len(slots)):
    
    if slots[i][1] != 0:
      if int(word[i]) != slots[i][1]:
        return False
    else:
      if int(word[i]) in let:
        let.remove(int(word[i]))
        playtiles[getKey(slots[i][0][0],slots[i][0][1])] = int(word[i])
      elif 200 in let:
        let.remove(200)
        playtiles[getKey(slots[i][0][0],slots[i][0][1])] = int(word[i]) + 100

      else:
        return False
  return playtiles

def checkDictionary (words, language):
  dictwords = dictionary(language)
  allwords = dictwords.dictWords()
  for word in words:
    wcode = ''.join([str(x) for x in word])
    if wcode not in allwords:
      return False
  return True
def swaptiles(rack, swaptiles, bag):
  for i in swaptiles:
    rack.remove(i)
  res = refillRack(rack, bag)
  newrack = res['rack']
  newbag = res['bag']
  for i in swaptiles:
    newbag.append(i)
  return {'bag': newbag, 'rack': newrack}
  
def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def getRoom(time, rules, creator, observer, language):
  roomId = randomString(5)
  room = {'id': roomId, 'data' : {'slot': {'slot1':{'type':'Human', 'status': 'Not ready', 'nick': creator}, 'slot2':{'type':'Human', 'status': 'waiting', 'nick':''}, 'slot3':{'type':'Human', 'status': 'waiting', 'nick':''}, 'slot4':{'type':'Human', 'status': 'waiting', 'nick':''}}, 'time': time, 'observe': observer, 'olist': [], 'rules': rules, 'creator': creator, 'language': language}}
  return room

def getRandRoom(time, rules, gamer, noofplayers, language):
  roomId = randomString(5)
  slotthree = {'type':'Human', 'status': 'waiting', 'nick':''}
  slotfour = {'type':'Human', 'status': 'waiting', 'nick':''}
  if noofplayers < 3:
    slotthree = {'type':'None', 'status': 'Closed', 'nick':'Closed'}
  if noofplayers < 4:
    slotfour = {'type':'None', 'status': 'Closed', 'nick':'Closed'}
  room = {'id': roomId, 'data' : {'slot': {'slot1':{'type':'Human', 'status': 'Ready', 'nick': gamer}, 'slot2':{'type':'Human', 'status': 'waiting', 'nick':''}, 'slot3':slotthree, 'slot4':slotfour}, 'time': time, 'observe': False, 'olist': [], 'rules': rules, 'creator': 'Random', 'noofplayers': noofplayers, 'language': language}}
  return room

def getGamerId():
  number = random.randint(11111, 99999)
  return number
def getvscomp(data):
  roomid = randomString(5)
  language = data['language']
  gameobject = materials(language)
  time = data['time']
  rules = data['rules']
  player =  data['player']
  level = data['level']
  players = {}
  players[player] = {'id': 1, 'score': 0, 'time': time }
  players['Computer'] = {'id': 2, 'score': 0, 'time': time, 'rack' :[], 'level': level }
  bag = gameobject.getbag()
  board = gameobject.getboard()
  game = {'board': board, 'players': players, 'bag': bag, 'turn': 1, 'tilesonboard':{}, 'probers': {'yes': [], 'no': []}, 'misser': [], 'pwords': [], 'pscore': 0, 'cplayer': '', 'cpasses': 0, 'endgame': {}, 'rules': rules, 'language': language} 
  with open(gamePath, "r") as file:
    data = json.load(file)
  data[roomid] = game
  with open(gamePath, "w") as file:
    json.dump(data, file)
  return {'rid': roomid, 'game': game}
def startGame(roomdata, slot, roomid):
  player = {}
  language = roomdata['language']
  gameobject = materials(language)
  for a in slot:
    gamer = roomdata['slot'][a]['nick']
    if gamer == 'Computer':
      player[gamer] = {'id': a[-1], 'score': 0, 'time': roomdata['time'], 'rack' :[], 'level': roomdata['slot'][a]['level'] }
    else:
      player[gamer] = {'id': a[-1], 'score': 0, 'time': roomdata['time'] }
  bag = gameobject.getbag()
  board = gameobject.getboard()
  game = {'board': board, 'players': player, 'bag': bag, 'turn': 1, 'tilesonboard':{}, 'probers': {'yes': [], 'no': []}, 'misser': [], 'pwords': [], 'pscore': 0, 'cplayer': '', 'cpasses': 0, 'endgame': {}, 'rules': roomdata['rules'], 'language': language} 
  with open(gamePath, "r") as file:
    data = json.load(file)
  data[roomid] = game
  with open(gamePath, "w") as file:
    json.dump(data, file)
  return game

class game:
  def __init__(self, room):
    self.gid = room
    print('in game')
    print(room)
    with open(gamePath, "r") as file:
      data = json.load(file)
    self.gdata = data[self.gid]
    self.gbag = self.gdata['bag']
    self.board = self.gdata['board']
    self.players = self.gdata['players']
    self.language = self.gdata['language']
  def getBag(self):
    return self.gbag
  def getBagL(self):
    return len(self.gbag)
  def getBoard(self):
    return self.board
  def getPlayers(self):
    return self.players
  def setBag(self, bag):
    self.gbag = bag
    self.gdata['bag'] = bag
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
    
  def refillRack(self, rack):
    nbag = self.gbag
    while ((len(rack) < 7) and (len(nbag) > 0)):
      random.shuffle(nbag)
      rack.append(nbag.pop())
    self.setBag(nbag)
    return rack
  def swaptiles(self, rack, swaptiles):
    nbag = self.gbag
    for i in swaptiles:
      rack.remove(i)
      rack.append(nbag.pop())
    for i in swaptiles:
      nbag.append(i)
    self.setBag(nbag)
    return rack
  def setBoard(self, board):
    self.board = board
    self.gdata['board'] = board
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
  def swappass(self, gamer, action, nswap = 0):
    activity = []
    turnnick = ''
    if action == 'swap':
      act = gamer + ' swapped ' + str(nswap) + ' tiles'
      activity.insert(0, act)
    else: 
      act = gamer + ' passed'
      activity.insert(0, act)
      self.gdata['cpasses'] += 1
      if (self.gdata['cpasses']) > (2 * len(self.players)) - 1:
        return 'endgame'
    turn = self.gdata['turn']
    nxtturn = False 
    while not nxtturn:
      turn = turn + 1
      if turn > 4:
        turn = 1
      name = self.getplayername(turn)
      if name != 'none':
        turnnick= name
        misser = self.gdata['misser']
        if name in misser:
          act = name + ' missed a turn for a wrong probe'
          activity.insert(0, act)
          misser.remove(name)
          self.gdata['misser'] = misser
        else:
          nxtturn = True
    self.gdata['turn'] = turn  
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)

    return {'turn': turn, 'activity': activity, 'turnnick': turnnick}
  def fillCompRack(self):
    # computer = [x for x in self.players if x == 'computer']
    try:
      if 'Computer' in list(self.players.keys()):
        rack =  self.players['Computer']['rack']
        rack = self.refillRack(rack)
        self.gdata['players']['Computer']['rack'] = rack
        with open(gamePath, "r") as file:
          data = json.load(file)
        data[self.gid] = self.gdata
        with open(gamePath, "w") as file:
          json.dump(data, file)
    except:
      pass
  
  def compresponse(self):
    game = ''
    if 'Computer' in list(self.players.keys()):
      words = self.gdata['pwords']
      if (checkDictionary(words, self.language)):
        game = self.presponse('Computer', 'no')
      else:
        probe = random.choice(['yes','no'])
        game = self.presponse('Computer', probe)
      return game  
      

  def createbaord(self, tiles, player):
    oboard = self.getBoard()
    board = copy.deepcopy(oboard)
    for bcode in list(tiles.keys()):
      py = ((letcode[bcode[0]]) - 1)
      px = (int(bcode[1:]) -1)
      board[py][px] = { 'pl': player, 'lp': tiles[bcode] }
    return board
  
  def customPlay(self, tilesonboard, pwords, pscore, cplayer):
    score = pscore
    activity = []
    turnnick = ''
    self.gdata['players'][cplayer]['score'] += score
    board = self.createbaord(tilesonboard, self.players[cplayer]['id'])
    self.gdata['board'] = board
    turn = self.gdata['turn']
    act = cplayer + ' scored ' + str(score) + ' pts'
    activity.insert(0, act)
    nxtturn = False 
    while not nxtturn:
      turn = turn + 1
      if turn > 4:
        turn = 1
      name = self.getplayername(turn)
      if name != 'none':
        turnnick= name
        nxtturn = True
    self.gdata['turn'] = turn  
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
    return {'gamer': cplayer, 'turn': turn, 'board': board, 'activity': activity, 'score': score, 'stat': 't', 'pwords': pwords, 'turnnick': turnnick }
    
  def compplay(self,rule = 'Standard'):
    rack =  self.players['Computer']['rack']
    level = self.players['Computer']['level']
    response = {}
    if(len(rack) < 1):
      response['type'] = 'end'
      return response
    board = copy.deepcopy(self.board)
    for i in range(len(board)):
      for j in range(len(board[i])):
        if( board[i][j] != 0):
          board[i][j] = board[i][j]['lp']
    complay = computerplay(board, rack, level, self.language)
    
    if complay[0] > 0:
      if rule == 'Custom':
        game = self.customPlay(complay[2], complay[1], complay[0], 'Computer')
        rack = rerack(rack, complay[2])
        rack = self.refillRack(rack)
        self.gdata['players']['Computer']['rack'] = rack
        response['type'] = 'play'
        response['res'] = game
      else:
        board = self.probegame(complay[2], complay[1], complay[0], 'Computer')
        rack = rerack(rack, complay[2])
        rack = self.refillRack(rack)
        self.gdata['players']['Computer']['rack'] = rack
        response['type'] = 'play'
        response['res'] = board
      
    else:
      dupes = [x for x in rack if rack.count(x) > 1]
      if(len(dupes) > 3) and (len(self.gbag) > 10):
        rack =  self.swaptiles(rack, dupes)
        res = self.swappass('Computer', 'swap', len(dupes))
        response['type'] = 'swap'
        response['res'] = res
      else:
        res = self.swappass('Computer', 'passed', 0)
        if res == 'endgame':
          response['type'] = 'end'
          response['res'] = self.compend()
          return response
        else:
          response['type'] = 'pass'
          response['res'] = res
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
    return response

  def compend(self):
    if 'Computer' in list(self.players.keys()):
      rack =  self.players['Computer']['rack']
      return self.endgame('Computer', rack)
  def probegame(self, tilesonboard, pwords, pscore, cplayer):
    board = self.createbaord(tilesonboard, 5)
    self.gdata['tilesonboard'] = tilesonboard
    self.gdata['pwords'] = pwords
    self.gdata['cplayer'] = cplayer 
    self.gdata['pscore'] = pscore
    self.gdata['cpasses'] = 0
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
    return board
  
  def getplayername(self, pid):
    for player in list(self.players.keys()):
      if (str(self.players[player]['id']) == str(pid)):
        return player
    return 'none'
  def presponse(self, gamer, response):
    probers = self.gdata['probers']
    probers[response].append(gamer)
    turnnick = ''
    if ((len(probers['yes']) + len(probers['no'])) == (len(list(self.players.keys())) - 1)):
      self.gdata['probers'] = {'yes': [], 'no': []}
      activity = []
      score = 0
      cplayer = self.gdata['cplayer']
      words = self.gdata['pwords']
      if (len(probers['yes']) > 0):
        if (checkDictionary(words, self.language)):
          score = self.gdata['pscore']
          self.gdata['players'][cplayer]['score'] += score
          for a in probers['yes']:
            act = a + ' probed wrongly'
            activity.insert(0, act)
            self.gdata['misser'].append(a)
          act = cplayer + ' scored ' + str(score) + ' pts'
          activity.insert(0, act)
          board = self.createbaord(self.gdata['tilesonboard'], self.players[cplayer]['id'])
          self.gdata['board'] = board
          turn = self.gdata['turn']
          nxtturn = False
          while not nxtturn:
            turn = turn + 1
            if turn > 4:
              turn = 1
            name = self.getplayername(turn)
            
            if name != 'none':
              turnnick= name
              misser = self.gdata['misser']
              if name in misser:
                act = name + ' missed a turn for a wrong probe'
                activity.insert(0, act)
                misser.remove(name)
                self.gdata['misser'] = misser
              else:
                nxtturn = True
          self.gdata['turn'] = turn  
          with open(gamePath, "r") as file:
            data = json.load(file)
          data[self.gid] = self.gdata
          with open(gamePath, "w") as file:
            json.dump(data, file)
          return {'gamer': cplayer, 'turn': turn, 'board': board, 'activity': activity, 'score': score, 'stat': 't', 'pwords': words, 'turnnick': turnnick}
        else:
          act = cplayer + 'Scored 0 for playing none existing word(s)'
          activity.insert(0, act)
          turn = self.gdata['turn']
          nxtturn = False 
          while not nxtturn:
            turn = turn + 1
            if turn > 4:
              turn = 1
            name = self.getplayername(turn)
            if name != 'none':
              turnnick= name
              misser = self.gdata['misser']
              if name in misser:
                act = name + ' missed a turn for a wrong probe'
                activity.insert(0, act)
                misser.remove(name)
                self.gdata['misser'] = misser
              else:
                nxtturn = True
          self.gdata['turn'] = turn
          board = self.board  
          with open(gamePath, "r") as file:
            data = json.load(file)
          data[self.gid] = self.gdata
          with open(gamePath, "w") as file:
            json.dump(data, file)
          return {'gamer': cplayer, 'turn': turn, 'board': board, 'activity': activity, 'score': score, 'stat': 'f', 'turnnick': turnnick}
      else:
        score = self.gdata['pscore']
        self.gdata['players'][cplayer]['score'] += score
        board = self.createbaord(self.gdata['tilesonboard'], self.players[cplayer]['id'])
        self.gdata['board'] = board
        turn = self.gdata['turn']
        act = cplayer + ' scored ' + str(score) + ' pts'
        activity.insert(0, act)
        nxtturn = False 
        while not nxtturn:
          turn = turn + 1
          if turn > 4:
            turn = 1
          name = self.getplayername(turn)
          if name != 'none':
            turnnick= name
            misser = self.gdata['misser']
            if name in misser:
              turnnick= name
              act = name + ' missed a turn for a wrong probe'
              activity.insert(0, act)
              misser.remove(name)
              self.gdata['misser'] = misser
            else:
              nxtturn = True
        self.gdata['turn'] = turn  
        with open(gamePath, "r") as file:
          data = json.load(file)
        data[self.gid] = self.gdata
        with open(gamePath, "w") as file:
          json.dump(data, file)
        return {'gamer': cplayer, 'turn': turn, 'board': board, 'activity': activity, 'score': score, 'stat': 't', 'pwords': words, 'turnnick': turnnick }
        
    else:
      self.gdata['probers'] = probers
      with open(gamePath, "r") as file:
        data = json.load(file)
      data[self.gid] = self.gdata
      with open(gamePath, "w") as file:
        json.dump(data, file)
      return 'wait' 
  def cscores(self):
    endeddata = []
    scorelist = []
    enddata = self.gdata['endgame']
    tracksub = 0
    for gamer in enddata:
      tracksub += enddata[gamer]['rsub']
    for gamer in enddata:
      if enddata[gamer]['rsub'] == 0:
        enddata[gamer]['addition'] += tracksub 
        enddata[gamer]['nscore'] += tracksub
      scorelist.append(enddata[gamer]['nscore'])
    scorelist.sort(reverse=True)
    for a, b in enumerate(scorelist):
      for gamer in enddata:
        if enddata[gamer]['nscore'] == b:
          sact = ''
          if enddata[gamer]['rsub'] != 0:
            sact = '(' + str(enddata[gamer]['oscore']) + ' minus ' + str(enddata[gamer]['rsub']) + ')'
          elif enddata[gamer]['addition'] != 0:
            sact = '(' + str(enddata[gamer]['oscore']) + ' plus ' + str(enddata[gamer]['addition']) + ')'
          if a == 0 :
            act = 'WINNER: ' + gamer + ' Total score of ' + str(b) +  sact 
            endeddata.append(act)
          elif a == 1:
            act = '2ND PLACE: ' + gamer + ' Total score of ' + str(b) +  sact 
            endeddata.append(act)
          elif a == 2:
            act = '3RD PLACE: ' + gamer + ' Total score of ' + str(b) +  sact 
            endeddata.append(act)
          elif a == 3:
            act = '4TH PLACE: ' + gamer + ' Total score of ' + str(b) +  sact 
            endeddata.append(act)
          break
    return endeddata
  def removeplayer(self, gamer):
    del self.gdata['players'][gamer]
    with open(gamePath, "r") as file:
      data = json.load(file)
    data[self.gid] = self.gdata
    with open(gamePath, "w") as file:
      json.dump(data, file)
  def endgame(self,gamer, rack):
    enddata = self.gdata['endgame']
    gameObject = materials(self.language)
    scores = gameObject.getscores()
    print(enddata)
    if gamer not in list(enddata.keys()):
      oldscore = self.players[gamer]['score']
      racksub = 0
      newscore = 0
      for i in rack:
        if i > 200: i = 200
        racksub += scores[str(i)]
      newscore = oldscore - racksub
      enddata[gamer] = {'oscore': oldscore, 'rsub': racksub, 'nscore': newscore, 'addition': 0}
    if len(enddata) == len(self.players):
      return self.cscores()
    else:
      self.gdata['endgame'] = enddata
      with open(gamePath, "r") as file:
        data = json.load(file)
      data[self.gid] = self.gdata
      with open(gamePath, "w") as file:
        json.dump(data, file)
      return 'wait' 

  def deletegame(self):
    with open(gamePath, "r") as file:
      data = json.load(file)
    del data[self.gid]
    with open(gamePath, "w") as file:
      json.dump(data, file)

if __name__ == "__main__":
  pass