import discord
import random
import os
import re
from discord.utils import get

#No token for you
TOKEN = os.environ.get('DISCORDTOKEN', 'default value')

client = discord.Client()

cmdMark = '!'
cmdSlash = '/'
cmdGambler = 'hey gambler, '
cmdGambler = 'hey seeker, '
trgLog = 'log'
trgRoll = 'roll'
trgBCN = 'blood'
trgDescribe = 'describe'
trgInspiration = 'inspiration'
trgThrok = 'throk'

def getCommand(message):
  if message.content.lower().startswith((cmdMark, cmdSlash, cmdGambler)):
    if message.content.lower().startswith((cmdMark, cmdSlash)):
      trim = len(cmdMark)
    else:
      trim = len(cmdGambler)
    return message.content[trim:].lower().split(' ')[0]
  return 'nocommand'

@client.event
async def on_message(message):

  if random.randint(1, 10000000) == 1 or 'Invoke innocence' in message.content:
    innocence = get(client.emojis, name='innocence')
    await message.add_reaction(innocence)
    await message.clear_reaction(innocence)
  
  # nice
  niceRegex = re.compile(r"(\D|\b)(420|69)+(\D|\b)")
  if re.search(niceRegex, message.content) != None:
#if '69' in message.content:
    await message.add_reaction('🇳')
    await message.add_reaction('🇮')
    await message.add_reaction('🇨')
    await message.add_reaction('🇪')
    await message.add_reaction('👌')
    
  # we do not want the bot to reply to itself
  if message.author == client.user:
    if 'Puzzle!' in message.content:
      await message.add_reaction('☝️')
    return

  if getCommand(message) == trgLog:
    print(str(message.author) + ': ' + message.content)

  if '<@!185462125940965376>' in message.content:
    msg = '"Motherfucker."'
    await message.channel.send(msg)
      
  if message.content.lower().startswith('hey sam can '):
    msg = '"No."'
    if random.randint(1, 100) == 1 or str(message.author) == 'SquigBoss#1353':
      msg = '"Eh, sure. Why not?"'
    await message.channel.send(msg)
      
  if message.content.lower().startswith('hey will should '):
    msg = '"Do it."'
    if random.randint(1, 100) == 1:
      msg = 'http://gph.is/2efKpdD'
    await message.channel.send(msg)

  if message.content.lower().startswith('hey kay will that joke ever not be funny'):
    msg = '"Nope, it\'s hilarious."'
    if str(message.author) == 'MouseEXE#8367':
      msg = '"It was never funny."'
    await message.channel.send(msg)
  
  if 'RIP' in message.content:
    respects = get(client.emojis, name='payrespects')
    await message.add_reaction(respects)
  
  if 'pour one out' in message.content.lower():
    if str(message.author) == 'Hitwave#9901':
      await message.add_reaction('🥛')
    else:
      await message.add_reaction('🍺')
    await message.add_reaction('⤵')

  if str(message.author) == 'Will G.#6807' and random.randint(1, 10000) == 1:
    wut = get(client.emojis, name='wutaeus')
    await message.add_reaction(wut)

  if 'puzzle' in message.content.lower():
    msg = 'Puzzle!'
    await message.channel.send(msg)
  
  if 'good bot' in message.content.lower():
    await message.add_reaction('🇹')
    await message.add_reaction('🇭')
    await message.add_reaction('🇦')
    await message.add_reaction('🇳')
    await message.add_reaction('🇰')
    await message.add_reaction('🇸')

  if 'bad bot' in message.content.lower():
    await message.add_reaction('🖕')

  if getCommand(message) == trgBCN:
    cleanmsg = cleanMessage(message, trgBCN).replace('-', '+-')
    dice = cleanmsg.split('+')
    total = 0
    breakdown = ' ['
    for die in dice:
      die = die.strip()
      didx = die.find('d')
      if die.startswith('d'):
        numDice = 1
      else:
        numDice = int(die[0:didx])
      sides = int(die[didx+1:])
      for idx in range(numDice):
        r = random.randint(1, sides)
        if r >= 4:
          writeup = '*' + str(r) + '*'
          total += 1
        else:
          writeup = '~~' + str(r) + '~~'
        writeup += ' + '
        breakdown += writeup
    breakdown = breakdown[:len(breakdown) - 3]
    breakdown += ']'
    msg = getRollMsg(total) + str(total) + '!"' + breakdown
    await message.channel.send(msg)


  if getCommand(message) == trgRoll:
    cleanmsg = cleanMessage(message, trgRoll).replace('-', '+-')
    dice = cleanmsg.split('+')
    if isAdvOrDis(cleanmsg):
      dice[0] = '2d20'
    total = 0
    minRoll = False
    maxRoll = False
    breakdown = ' ['
    for die in dice:
      die = die.strip()
      didx = die.find('d')
      if didx != -1:
        if die.startswith('d'):
          numDice = 1
        else:
          numDice = int(die[0:didx])
        sides = int(die[didx+1:])
        for idx in range(numDice):
          r = random.randint(1, sides)
          if r == 1:
            minRoll = True
          elif r == 20:
            maxRoll = True
          writeup = '(' + str(r) + ')'
          if isAdvantage(cleanmsg):
            if r > total:
              total = r
            writeup += ', '
          elif isDisadvantage(cleanmsg):
            if r < total or total == 0:
              total = r
            writeup += ', '
          else:
            total += r
            writeup += ' + '
          breakdown += writeup
      else:
        total += int(die)
        writeup = die + ' + '
        breakdown += writeup
    if isAdvOrDis(cleanmsg):
      breakdown = breakdown[:len(breakdown) - 2]
    else:
      breakdown = breakdown[:len(breakdown) - 3]
    breakdown += ']'
    if (cleanmsg == '2d20' or isAdvOrDis(cleanmsg)) and minRoll and maxRoll:
      msg = '"Way to minmax your rolls, you got a ' + str(total) + '!"' + breakdown
    else:
      msg = getRollMsg(total) + str(total) + '!"' + breakdown
    await message.channel.send(msg)

  if getCommand(message) == trgDescribe:
    player = cleanMessage(message, trgDescribe)
    msg = getUnexpected()
    if player == 'throk':
      msg = '"Although I have never met the individual, I have heard tales of his great deeds."'
    if player == 'seeker':
      msg = '"Of course I know him. He\'s me."'
    if player == 'keeper' or player == 'gambler' or player == 'olden':
      msg = '"Now that\'s a name I haven\'t heard in a long time."'
    if player == 'tweaker':
      msg = '"Get that vermin out of my random access memory."'
    await message.channel.send(msg)

  if message.content.startswith('!help'):
    msg = """To ask Seeker to roll you a die (or multiple dice!) simply type '!roll', followed by your roll query.
    \nRoll queries are either a number of dice, followed by a 'd', followed by the sides on the die, or a straight number.
    \nFor example, you can use 1d20 or 42d69 to roll a single 20 sided die, or 42 69 sided dice.
    \nYou can chain these queries together with a '+'.
    \nFor example, you can say '!roll 1d420 + 1d69 + 42069'"""
    await message.channel.send(msg)
      
  if message.content == '!stat':
    msg = rollOneStat()
    await message.channel.send(msg)
      
  if message.content == '!statblock':
    msg = '['
    for i in range(6):
      msg += str(rollOneStat())
      if i < 5:
        msg += ', '
    msg += ']'
    await message.channel.send(msg)

def cleanMessage(message, command):
  if message.content.startswith((cmdMark, cmdSlash)):
    trim = len(cmdMark)
  else:
    trim = len(cmdGambler)
  trim += len(command)
  return message.content[trim:].lower().strip()

def isAdvantage(message):
  return message.startswith('advantage')

def isDisadvantage(message):
  return message.startswith('disadvantage')


def isAdvOrDis(message):
  return isAdvantage(message) or isDisadvantage(message)

def getUnexpected():
  return '"My apologies. I don\'t believe I\'ve met the individual you\'re referring to."'

def getRollMsg(roll):
  r = random.randint(0, 3)
  if r == 0:
    return '"I have rolled, and the result is' + getAn(roll)
  elif r == 1:
    return '"My processors report a result of '
  elif r == 2:
    return '"It appears I rolled' + getAn(roll)
  else:
    return '"The routine finished executing. I rolled' + getAn(roll)

def getAn(roll):
  if roll == 8 or roll == 11 or roll == 18:
    return ' an '
  else:
    return ' a '
    
def rollOneStat():
  arr = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
  minIdx = 0
  for idx in range(len(arr)):
    if arr[idx] < arr[minIdx]:
      minIdx = idx
  total = 0
  for idx in range(len(arr)):
    if idx != minIdx:
      total += arr[idx]
  return total

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

client.run(TOKEN)
