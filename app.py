# Work with Python 3.6
import discord
import random
import os

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

    if message.content.startswith('!throk'):
        msg = '<:throkflex:486598697228959760>'
        await client.send_message(message.channel, msg)
    
    if 'good bot' in message.content.lower():
        msg = '"Thanks!"'
        await client.send_message(message.channel, msg)

    if 'bad bot' in message.content.lower():
        msg = '"Fuck you."'
        await client.send_message(message.channel, msg)

    if message.content.startswith(rollCmd) or message.content.startswith(altRollCmd):
        cleanmsg = cleanMessage(message, rollCmd)
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
            msg = '"Aye, I rolled a ' + str(total) + '!"' + breakdown
        await client.send_message(message.channel, msg)

    if message.content.startswith(describeCmd):
        player = cleanMessage(message, describeCmd)
        msg = '"Friend, I got rightly no idea who you\'re talking about. Maybe check yer spelling?"'
        if player == 'rayne':
            msg = '"Heard they almost died. Maybe that would get them to stop talking."'
        if player == 'wivaun':
            msg = '"Do you know where he gets his supply? Maybe hit me up, eh? My last dealer died on an adventure six months ago."'
        if player == 'khyrim':
            msg = '"Live by the edge, die by the edge. Rest in peace pal."'
        if player == 'kay':
            msg = '"That skull mask is creepy as hell. Something ain\'t aight right with that kid."'
        if player == 'kai':
            msg = '"Now I won\'t mix up Kai and Kay, finally. I will miss her though, good lass."'
        if player == 'wulfred':
            msg = '"A tavern always needs a grumpy old dwarf. I\'ll miss the guy."'
        if player == 'throk':
            msg = '"Throk and Peck, hell of duo. Who doesn\'t love Throk?"'
        if player == 'fenric':
            msg = '"Kinda moody lately. Is it because a bunch of his friends died? Lame."'
        if player == 'fidelius':
            msg = '"This little bitch cheats at cards."'
        if player == 'vondal':
            msg = '"Who? Oh, is he dead now? Didn\'t notice."'
        if player == 'avos':
            msg = '"Heard he helped kill a dragon. Nice turn around from the time a dragon nearly killed him."'
        if player == 'theodwin':
            msg = '"I literally only care about this guy because of Rocky."'
        if player == 'evin':
            msg = '"Gone too soon, pour one out for the lad."'
        if player == 'takrend':
            msg = '"So many of you "brave" adventurers out here and this guy is the only one who can drive a boat? Weak."'
        if player == 'wil' or player == 'wilavor':
            msg = '"Talented half-elf. Surprised he survived this long but can\'t say I\'m upset about it."'
        if player == 'agamemnon':
            msg = '"Bit of an explosive exit, no? Wonder where they went. At least I got their dogs. Who\'s a good girl? You are!"'
        if player == 'namira':
            msg = '"An intimidating lass for sure. Hope she doesn\'t think I\'m evil, doubt I could stand up against her in a fight."'
        if player == 'moryn':
            msg = '"Hell of a fiery beard! Enough to even rival mine. A holy type though, great. Just great."'
            
        #msg = '<:payrespects:502292405152645122>'
        await client.send_message(message.channel, msg)

    if message.content.lower().startswith('hey sam can i'):
        msg = '"No."'
        if random.randint(1, 100) == 1:
            msg = '"Eh, sure. Why not?"'
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
        msg = """To ask the Old Gambler to roll you a die (or multiple dice!) simply type \"!roll\", followed by your roll query.
        \nRoll queries are either a number of dice, followed by a \'d\', followed by the sides on the die, or a straight number.
        \nFor example, you can use 1d20 or 42d69 to roll a single 20 sided die, or 42 69 sided dice.
        \nYou can chain these queries together with a \'+\'.
        \nFor example, you can say \"!roll 1d420 + 1d69 + 42069\""""
        await client.send_message(message.channel, msg)

def cleanMessage(message, command):
    trim = len(command)
    return message.content[trim:].lower().strip()

def isAdvantage(message):
    return message.startswith('advantage')

def isDisadvantage(message):
    return message.startswith('disadvantage')

def isAdvOrDis(message):
    return isAdvantage(message) or isDisadvantage(message)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
