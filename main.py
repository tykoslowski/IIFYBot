import discord
import datetime
from secrets import bot_key

client = discord.Client()

yes = 'Yes! LET\'S GO!!!'
no = 'No, not yet!'
evan_flag = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 262687110853689355:
        evan_flag = True

    if message.content.startswith('is it ') or message.content.startswith('Is it '):
        rest_of_message = message.content[6:] # Get the rest of the message
        today = datetime.datetime.today().weekday() # Get the day of the week as an integer (Mon: 0 - Sun: 6)

        if 'monday' in rest_of_message or 'Monday' in rest_of_message or 'mon' in rest_of_message or 'Mon' in rest_of_message:
            if today == 0:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            return
        if 'tuesday' in rest_of_message or 'Tuesday' in rest_of_message or 'tues' in rest_of_message or 'Tues' in rest_of_message:
            if today == 1:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            return
        if 'wednesday' in rest_of_message or 'Wednesday' in rest_of_message or 'wed' in rest_of_message or 'Wed' in rest_of_message:
            if today == 2:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            return
        if 'thursday' in rest_of_message or 'Thursday' in rest_of_message or 'thurs' in rest_of_message or 'Thurs' in rest_of_message:
            if today == 3:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            return
        if 'friday' in rest_of_message or 'Friday' in rest_of_message or 'fri' in rest_of_message or 'Fri' in rest_of_message:
            if today == 4:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            return
        if 'saturday' in rest_of_message or 'Saturday' in rest_of_message or 'sat' in rest_of_message or 'Sat' in rest_of_message:
            if today == 5:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            return
        if 'sunday' in rest_of_message or 'Sunday' in rest_of_message or 'sun' in rest_of_message or 'Sun' in rest_of_message:
            if today == 6:
                await message.channel.send(yes)
            else:
                await message.channel.send(no)
            return
        
        # If no date has been specified, send an error message
        await message.channel.send('Please enter a valid date.')

        if evan_flag is True:
            await message.channel.send('Are you excited for D&D day, Evan?')

client.run(bot_key)