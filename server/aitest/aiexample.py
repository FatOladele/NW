import multiprocessing
import time
import copy
from materials import materials, dictionary, TW, DW, TL, DL
letcode=  {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I":  9, "J": 10, "K": 11, "L": 12, "M": 13, "N":14, "O": 15}
def getKey(y, x):
  return str(list(letcode.keys())[list(letcode.values()).index(y + 1)]) + str(x +1)


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
    result = []
    for x in list(sorttiles.keys()):
      word = [y for y in allwords if len(y)/3 == int(x)]
      result.append(tileslotandwords(sorttiles[x], word, rack, language, board, maxPoint))
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
  #starttime = time.time()
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
