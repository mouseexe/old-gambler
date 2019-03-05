# Work with Python 3.6
import discord
import random
import os
from discord.utils import get

TOKEN = os.environ.get('DISCORDTOKEN', 'default value')

client = discord.Client()

rollCmd = '!roll'
altRollCmd = '/roll'
describeCmd = '!describe'

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if '@SquigBoss#1353' in message.content:
        msg = '"You fool! You spoke the forbidden words! His wrath falls upon us!"'
        await client.send_message(message.channel, msg)
        
    if message.content.lower().startswith('hey sam can i '):
        msg = '"No."'
        if random.randint(1, 100) == 1:
            msg = '"Eh, sure. Why not?"'
        await client.send_message(message.channel, msg)
        
    if message.content.lower().startswith('hey will should i '):
        msg = '"Do it."'
        if random.randint(1, 100) == 1:
            msg = 'http://gph.is/2efKpdD'
        await client.send_message(message.channel, msg)
    
    if 'RIP' in message.content:
        msg = '<:payrespects:502292405152645122>'
        await client.send_message(message.channel, msg)
    
    #if 'pour one out' in message.content.lower():
        #beer = get(client.get_all_emojis(), name=':beer:')
        #arrow = get(client.get_all_emojis(), name=':arrow_heading_down:')
        #await client.add_reaction(message, '\u1F37A')
        #await client.add_reaction(message, '\u2935')

    if message.content.startswith('!throk'):
        msg = '<:throkflex:486598697228959760>'
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('!inspiration'):
        msg = '<:milano:542939947544346644>'
        await client.send_message(message.channel, msg)
    
    if 'good bot' in message.content.lower():
        msg = '"Thanks!"'
        await client.send_message(message.channel, msg)

    if 'bad bot' in message.content.lower():
        msg = '"Fuck you."'
        await client.send_message(message.channel, msg)

    if message.content.startswith(rollCmd) or message.content.startswith(altRollCmd):
        cleanmsg = cleanMessage(message, rollCmd).replace('-', '+-')
        dice = cleanmsg.split('+')
        if isAdvOrDis(cleanmsg):
            dice[0] = '2d20'
        if isCassandra(cleanmsg):
            dice = ['2d20', '8']
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
                        r = 8
                        writeup = '(' + str(r) + '*)'
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
            msg = '"Aye, I rolled a ' + str(total) + '!"' + breakdown
        await client.send_message(message.channel, msg)

    if message.content.startswith(describeCmd):
        player = cleanMessage(message, describeCmd)
        msg = getUnexpected()
        if player == 'rayne' or player == 'elf':
            msg = '"She\'s got a lizard hand. Weird. Also she\'s a girl now? Extra weird."'
        if player == 'wivaun' or player == 'wiv':
            msg = '"He was a good soul. Not sure what it was that messed him up like that, but I hope things get better."'
        if player == 'khyrim':
            msg = '"Live by the edge, die by the edge. Rest in peace pal."'
        if player == 'kay' or player == 'boy':
            msg = '"He\'s out there mapping stars in the daytime, and now he\'s speaking with extraplanar beings? Creepy."'
        if player == 'kai':
            msg = '"Now I won\'t mix up Kai and Kay, finally. I will miss her though, good lass."'
        if player == 'wulfred':
            msg = '"A tavern always needs a grumpy old dwarf. I\'ll miss the guy."'
        if player == 'throk' or player == 'muscles':
            msg = '"Iacto got nothing on Throk."'
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
            msg = '"Never see him around. Still my favorite."'
        if player == 'wil' or player == 'wilavor' or player == 'halves':
            msg = '"Kid sure knows how to drum up a crowd. Get it? Because he\'s got that fancy drum?"'
        if player == 'agamemnon' or player == 'fireheart':
            msg = '"Bit of an explosive exit, no? Wonder where they went. At least I got their dogs. Who\'s a good girl? You are!"'
        if player == 'namira':
            msg = '"Aasimar, huh? Guess that was kind of obvious in hindsight. Burn marks on the eyes and all that."'
        if player == 'moryn' or player == 'dwarf':
            msg = '"Glad he made it back alright. He reminds me of my dad. But less grumpy."'
        if player == 'cassandra' or player == 'cass':
            msg = '"She\'s a lot nicer than I gave her credit for. Seems to really care about the tiefling girl too."'
        if player == 'crimson' or player == 'firesoul':
            msg = '"She hasn\'t gotten any less abrasive, huh? Must be a druid thing."'
        if player == 'aban' or player == 'slit-eyes':
            msg = '<:4ban:550062949603999981>'
        if player == 'antaeus' or player == 'goldy':
            msg = '"The new king of baller moves. 100% badass, even if he can\'t read."'
        if player == 'dendro' or player == 'milkdrinker':
            msg = '"Kid\'s walking around with some fancy gear now, isn\'t he? Got some fancy runes on that there sword. Wonder what they say."'
        if player == 'isla' or player == 'xarthisius' or player == 'peck' or player == 'rocky' or player == 'dexter' or player == 'sapphire' or player == 'sarah finley' or player == 'mieka' or player == 'karl' or player == 'artax' or player == 'granny' or player == 'keldrick' or player == 'yai' or player == 'vizigo' or player == 'tuli' or player == 'valkea' or player == 'quilliby':
            msg = '"Nice to see \'em around the taproom sometimes. Cheers me up, ya know? Makes me less lonely."'
            
        #msg = '<:payrespects:502292405152645122>'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!snore'):
        #Join #taproom and play snoring audio
        msg = '"Zzz"'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!wake'):
        #Leave taproom
        msg = '"I\'m up! I\'m up!"'
        await client.send_message(message.channel, msg)

    if message.content.startswith('!help'):
        msg = """To ask the Old Gambler to roll you a die (or multiple dice!) simply type '!roll', followed by your roll query.
        \nRoll queries are either a number of dice, followed by a 'd', followed by the sides on the die, or a straight number.
        \nFor example, you can use 1d20 or 42d69 to roll a single 20 sided die, or 42 69 sided dice.
        \nYou can chain these queries together with a '+'.
        \nFor example, you can say '!roll 1d420 + 1d69 + 42069'"""
        await client.send_message(message.channel, msg)
        
    if message.content == '!stat':
        msg = rollOneStat()
        await client.send_message(message.channel, msg)
        
    if message.content == '!statblock':
        msg = '['
        for i in range(6):
            msg += str(rollOneStat())
            if i < 5:
                msg += ', '
        msg += ']'
        await client.send_message(message.channel, msg)

def cleanMessage(message, command):
    trim = len(command)
    return message.content[trim:].lower().strip()

def isAdvantage(message):
    return message.startswith('advantage') or isCassandra(message)

def isDisadvantage(message):
    return message.startswith('disadvantage')

def isCassandra(message):
    return message.startswith('cassandra') or message.startswith('cass')

def isAdvOrDis(message):
    return isAdvantage(message) or isDisadvantage(message)

def getUnexpected():
    r = random.randint(0, 5)
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
