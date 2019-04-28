import discord
import random
import os
from discord.utils import get

#No token for you
TOKEN = os.environ.get('DISCORDTOKEN', 'default value')

client = discord.Client()

cmdMark = '!'
cmdSlash = '/'
cmdGambler = 'hey gambler, '
trgLog = 'log'
trgRoll = 'roll'
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
  # we do not want the bot to reply to itself
  if message.author == client.user:
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
    respects = get(client.emojis(), name='payrespects')
    #msg = '<:payrespects:502292405152645122>'
    await message.add_reaction(respects)
  
  if 'pour one out' in message.content.lower():
    if str(message.author) == 'Hitwave#9901':
      await message.add_reaction('🥛')
    else:
      await message.add_reaction('🍺')
    await message.add_reaction('⤵')

  if getCommand(message) == trgThrok:
    msg = '<:throkflex:486598697228959760>'
    await message.channel.send(msg)
      
  if getCommand(message) == trgInspiration:
    msg = '<:milano:542939947544346644>'
    await message.channel.send(msg)

  if str(message.author) == 'Will G.#6807' and random.randint(1, 96) == 1:
    kick = get(client.emojis(), name='wulfkick')
    await message.add_reaction(kick)

  
  if 'good bot' in message.content.lower():
    await message.add_reaction('🇹')
    await message.add_reaction('🇭')
    await message.add_reaction('🇦')
    await message.add_reaction('🇳')
    await message.add_reaction('🇰')
    await message.add_reaction('🇸')
    #msg = '"Thanks!"'
    #await message.channel.send(msg)

  if 'bad bot' in message.content.lower():
    await message.add_reaction('🖕')
    #msg = '"Fuck you."'
    #await message.channel.send(msg)

  if getCommand(message) == trgRoll:
    cleanmsg = cleanMessage(message, trgRoll).replace('-', '+-')
    dice = cleanmsg.split('+')
    if isAdvOrDis(cleanmsg):
      dice[0] = '2d20'
    if isCassandra(cleanmsg):
      dice = ['2d20', '10']
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
          if isCassandra(cleanmsg) and r < 8:
            writeup = '(~~' + str(r) + '~~ 8)'
            r = 8
          else:
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
    if player == 'rayne' or player == 'scaley':
      msg = '"Nerd."'
    if player == 'wivaun' or player == 'wiv':
      msg = '"He was a good soul. Not sure what it was that messed him up like that, but I hope things get better."'
    if player == 'khyrim':
      msg = '"Live by the edge, die by the edge. Rest in peace pal."'
    if player == 'kay' or player == 'boy':
      msg = '"Kid\'s been taking a lot of initiative lately. Not sure if I should be proud or scared."'
    if player == 'kai':
      msg = '"Now I won\'t mix up Kai and Kay, finally. I will miss her though, good lass."'
    if player == 'wulfred':
      msg = '"A tavern always needs a grumpy old dwarf. I\'ll miss the guy."'
    if player == 'throk' or player == 'muscles':
      msg = '"Throk\'s so tough, I bet he\'d eat a bowl of nails for breakfast. Without any milk."'
    if player == 'fenric':
      msg = '"I heard he got killed by a swarm of squirrels in the night."'
    if player == 'fidelius':
      msg = '"That little bitch cheated at cards."'
    if player == 'vondal':
      msg = '"Who? Oh, is he dead now? Didn\'t notice."'
    if player == 'avos':
      msg = '"Surprised he lived that long to be honest. Horny little bugger, wasn\'t he?"'
    if player == 'theodwin':
      msg = '"I literally only care about this guy because of Rocky."'
    if player == 'evin':
      msg = '"Gone too soon, pour one out for the lad."'
    if player == 'takrend':
      msg = '"I guess it\'s fitting that he\'s back on a boat now, huh? I\'ll miss the guy."'
    if player == 'wil' or player == 'wilavor' or player == 'halves':
      msg = '"Kid sure knows how to drum up a crowd. Get it? Because he\'s got that fancy drum?"'
    if player == 'agamemnon' or player == 'fireheart':
      msg = '"Bit of an explosive exit, no? Wonder where they went. At least I got their dogs. Who\'s a good girl? You are!"'
    if player == 'namira':
      msg = '"Aasimar, huh? Guess that was kind of obvious in hindsight. Burn marks on the eyes and all that."'
    if player == 'moryn' or player == 'dwarf':
      msg = '"Glad he made it back alright. He reminds me of my dad. But less grumpy."'
    if player == 'cassandra' or player == 'cass':
      msg = '"She\'s got quite the temper these days, doesn\'t she? Can\'t really say I blame her, though. Still, what\'s up with her eye? That\'s weird."'
    if player == 'crimson' or player == 'firesoul':
      msg = '"Has anyone seen her around lately? I hope she\'s alright."'
    if player == 'aban' or player == 'slit-eyes':
      msg = '<:4ban:550062949603999981>'
    if player == 'antaeus' or player == 'goldy':
      msg = '"The new king of baller moves. 100% badass, even if he can\'t read."'
    if player == 'dendro' or player == 'milkdrinker':
      msg = '"Good to see him going out again, he spent a while just sitting around the tavern, huh?"'
    if player == 'grixie' or player == 'barabbas':
      msg = '"Wow, he certainly has the face of a young man, doesn\'t he?"'
    if player == 'isla':
      msg = '"She puts up with way more shit than I would if I ran this place."'
    if player == 'xarthisius':
      msg = '"I didn\'t know monkeys could be wizards."'
    if player == 'lumpkin':
      msg = '"Creepy flesh fellow, ain\'t he?"'
    if player == 'peck':
      msg = '"I just wish Throk brought him around more often."'
    if player == 'rocky':
      msg = '"Also known as the: the only reason we keep the firbolg around."'
    if player == 'dexter':
      msg = '"Whossa good girl? You are! Yes you are!"'
    if player == 'sapphire':
      msg = '"Fetch! No, wait, don\'t eat that! No!"'
    if player == 'sarah finley':
      msg = '"Theodwin has put her through a lot of shit, hasn\'t he?"'
    if player == 'mieka':
      msg = '"Why is she always white? Doesn\'t Rayne know how edgy that is?"'
    if player == 'karl':
      msg = '"Has... anyone seen him around lately? Kay doesn\'t seem to bring him about much anymore."'
    if player == 'artax':
      msg = '"Not a huge fan of holy types, but he\'s alright I guess."'
    if player == 'granny':
      msg = '"She reminds me of my grandmother. Except... creepier."'
    if player == 'keldrick':
      msg = '"Not the most annoying wizard I\'ve met, so credit there I suppose."'
    if player == 'yai':
      msg = '"She makes good tools. I appreciate that."'
    if player == 'vizigo' or player == 'vizigo al-fathwedi zaritissa':
      msg = '"I don\'t think he thinks I\'m real. Heh."'
    if player == 'tuli':
      msg = '"Glad we finally got him some tools."'
    if player == 'valkea':
      msg = '"Honestly not really sure what her deal is. Maybe I\'ll ask one day."'
    if player == 'quilliby':
      msg = '"A walking quill? Weird."'
    if player == 'mugston':
      msg = '"A walking mug? Odd."'
    if player == 'glassthew':
      msg = '"A walking glass? Bizarre."'
    if player == 'bowlrick':
      msg = '"A walking bowl? Unreal."'
    if player == 'scout':
      msg = '"Cute weasel!"'
    if player == 'skitter':
      msg = '"Large rat!"'
    if player == 'digger':
      msg = '"First badger I\'ve seen in a while."'
    if player == 'tusks':
      msg = '"Fierce looking boar."'
    if player == 'ebony':
      msg = '"That is one large cat."'
    if player == 'burrow':
      msg = '"Oh, an even larger badger."'
    if player == 'moon':
      msg = '"That is a terrifying wolf."'
    if player == 'legend':
      msg = '"That elk is massive."'
    if 'fortinbras' in player:
      msg = '"Please refer to the gentleman by his proper name."'
    if player == 'sir mister fortinbras olliver gripplesnitch iv, esquire' or player == 'sir mister fortinbras olliver gripplesnitch iii, esquire':
      msg = '"Thank you."'
    if 'mercer' in player:
      msg = '"The antichrist."'
    if player == 'verdant':
      msg = '"Bush."'
    if player == 'vabalar':
      msg = '"Never met a ' + getFirbolg()  + ', maybe you\'re imagining things?"'
        
    await message.channel.send(msg)

  if message.content.startswith('!help'):
    msg = """To ask the Old Gambler to roll you a die (or multiple dice!) simply type '!roll', followed by your roll query.
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

def getFirbolg():
  r = random.randint(0, 10)
  if r == 0:
    return 'Fortnite'
  elif r == 1:
    return 'Fallot'
  elif r == 2:
    return 'Foglight'
  elif r == 3:
    return 'Failure'
  elif r == 4:
    return 'Flatulence'
  elif r == 5:
    return 'Fight Club'
  elif r == 6:
    return 'Vandalblast'
  elif r == 7:
    return 'Zavala'
  elif r == 8:
    return 'Fountain drink'
  elif r == 9:
    return 'F to pay respects'
  elif r == 10:
    return 'Farmer Joe'

def isAdvantage(message):
  return message.startswith('advantage') or isCassandra(message)

def isDisadvantage(message):
  return message.startswith('disadvantage')

def isCassandra(message):
  return message.startswith('cassandra') or message.startswith('cass')

def isAdvOrDis(message):
  return isAdvantage(message) or isDisadvantage(message)

def getUnexpected():
  r = random.randint(0, 10)
  if r == 0:
    return '"Friend, I got rightly no idea who you\'re talking about. Maybe check yer spelling?"'
  elif r == 1:
    return '"Who in the nine hells is that? Maybe yer spelling is off, pal."'
  elif r == 2:
    return '"Fella, I\'m not familiar with that individual. Did ya spell the name wrong?"'
  elif r == 3:
    return '"Uh.. who?"'
  elif r == 4:
    return '"Nobody ever been here with that name, least not that I know of."'
  elif r == 5:
    return '"Who? I don\'t know anyone by that name, buddy"'
  elif r == 6:
    return '"I don\'t believe we\'ve got anyone here by that name, sorry \'bout that."'
  elif r == 7:
    return '"Nope, nobody named that who lives here. Maybe try to spell it right next time, hm?"'
  elif r == 8:
    return '"Is this a joke? None of the folks in here go by that name, friend."'
  elif r == 9:
    return '"Doesn\'t ring any bells to me."'
  elif r == 10:
    return '"Hmm, no, I don\'t think anyone here is called that."'

def getRollMsg(roll):
  r = random.randint(0, 5)
  if r == 0:
    return '"Aye, I got' + getAn(roll)
  elif r == 1:
    return '"The dice say '
  elif r == 2:
    return '"That\'s not cocked, is it? Looks like' + getAn(roll)
  elif r == 3:
    return '"Looks like' + getAn(roll)
  elif r == 4:
    return '"Heh, almost went off the table! I rolled' + getAn(roll)
  elif r == 5:
    return '"I rolled' + getAn(roll)

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
