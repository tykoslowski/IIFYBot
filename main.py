import discord
from datetime import datetime, timezone
from secrets import bot_key

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

client = discord.Client()

yes = 'Yes! LET\'S GO!!!'
no = 'No, not yet!'
evan_flag = False
dnd_day = [0, 2]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 262687110853689355:
        evan_flag = True
    else:
        evan_flag = False

    
    if message.content.lower().startswith('is it '):
        rest_of_message_temp = message.content[6:] # Get the rest of the message
        rest_of_message = rest_of_message_temp.lower() # Format the rest of the message
        dt_temp = datetime.datetime # Store datetime object
        corrected_dt = utc_to_local(dt_temp) # Change timezone
        today = corrected_dt.today().weekday() # Get the day of the week as an integer (Mon: 0 - Sun: 6)

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