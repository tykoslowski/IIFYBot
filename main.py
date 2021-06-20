import discord
import datetime
from secrets import bot_key

client = discord.Client()

yes = 'Yes! LET\'S GO!!!'
no = 'No, not yet!'
evan_flag = False
dnd_day = [0, 2]
dst = True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    # Don't check own messages
    if message.author == client.user:
        return

    # Set Evan flag
    if message.author.id == 262687110853689355:
        evan_flag = True
    else:
        evan_flag = False
    
    # Set message to all lowercase for processing
    mess_temp = message.content.lower()
    if mess_temp.startswith('is it '):
        
        # Grab and format the rest of the message
        rest_of_message_temp = message.content[6:]
        rest_of_message = rest_of_message_temp.lower()

        # Set timezone to PST or PDT depending on daylight savings time
        today = 0
        if dst is True:
            tz_PDT = datetime.timezone(datetime.timedelta(hours=-7))
            dt_PDT = datetime.datetime.now(tz=tz_PDT)
            today = dt_PDT.weekday()
        else:
            tz_PST = datetime.timezone(datetime.timedelta(hours=-8))
            dt_PST = datetime.datetime.now(tz=tz_PST)
            today = dt_PST.weekday()

        # Check for each weekday
        if 'monday' in rest_of_message or 'mon' in rest_of_message:
            if today == 0:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            if evan_flag is True:
                await message.channel.send('Are you excited for D&D day, Evan?')
            return
        elif 'tuesday' in rest_of_message or 'tues' in rest_of_message:
            if today == 1:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            if evan_flag is True:
                await message.channel.send('Are you excited for D&D day, Evan?')
            return
        elif 'wednesday' in rest_of_message or 'wed' in rest_of_message:
            if today == 2:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            if evan_flag is True:
                await message.channel.send('Are you excited for D&D day, Evan?')
            return
        elif 'thursday' in rest_of_message or 'thurs' in rest_of_message:
            if today == 3:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            if evan_flag is True:
                await message.channel.send('Are you excited for D&D day, Evan?')
            return
        elif 'friday' in rest_of_message or 'fri' in rest_of_message:
            if today == 4:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            if evan_flag is True:
                await message.channel.send('Are you excited for D&D day, Evan?')
            return
        elif 'saturday' in rest_of_message or 'sat' in rest_of_message:
            if today == 5:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            if evan_flag is True:
                await message.channel.send('Are you excited for D&D day, Evan?')
            return
        elif 'sunday' in rest_of_message or 'sun' in rest_of_message:
            if today == 6:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            if evan_flag is True:
                await message.channel.send('Are you excited for D&D day, Evan?')
            return
        
        # If no date has been specified, check for "dnd day" or "d&d day"
        elif 'dnd day' in rest_of_message or 'd&d day' in rest_of_message or 'dndday' in rest_of_message or 'd&dday' in rest_of_message:
            if today in dnd_day:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            if evan_flag is True:
                await message.channel.send('Hope you\'re liking the new update, Evan!')
            return

        # Otherwise, request valid date
        else:
            await message.channel.send('Please enter a valid date.')

client.run(bot_key)