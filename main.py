import discord
import datetime
import random
from enum import Enum
from secrets import bot_key

random.seed(a=None)

client = discord.Client()

class Days(Enum):
    MONDAY=0
    TUESDAY=1
    WEDNESDAY=2
    THURSDAY=3
    FRIDAY=4
    SATURDAY=5
    SUNDAY=6
    DNDDAY=7

dnd_days = {
    Days.MONDAY.value: False,
    Days.TUESDAY.value: False,
    Days.WEDNESDAY.value: False,
    Days.THURSDAY.value: False,
    Days.FRIDAY.value: False,
    Days.SATURDAY.value: False,
    Days.SUNDAY.value: False
}

schedule = {}

yes = ["Yes! LET'S GO!!!", "Oh yea, you excited?", "Yuuuuuup.", "I just checked and... it is!", "Heck yea dude!"]
no = ["No, not yet!", "No, maybe soon though...", "Nope.", "Nah.", "No. You know how to use a calendar, right?"]

evan_flag = False
evan_message = "Glad to have you back, Evan."

dst = True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Don't check own messages
    if message.author == client.user:
        return
    
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
    
    # Set Evan flag
    if message.author.id == 262687110853689355:
        evan_flag = True
    else:
        evan_flag = False
    
    # Set message to all lowercase for processing
    mess_temp = message.content.lower()

    # LEGACY FUNCTION - ENABLED
    if mess_temp.startswith('is it '): 
        args = mess_temp[6:].split(' ') # Grab and format rest of message
        args = args[:10] # Take max 10 args
        for a in args: # Check for each weekday or dnd day
            asked_day = -1
            if 'monday' == a or 'mon' == a:
                asked_day = Days.MONDAY.value
            elif 'tuesday' == a or 'tues' == a or 'chewsday' == a:
                asked_day = Days.TUESDAY.value
            elif 'wednesday' == a or 'wed' == a:
                asked_day = Days.WEDNESDAY.value
            elif 'thursday' == a or 'thurs' == a:
                asked_day = Days.THURSDAY.value
            elif 'friday' == a or 'fri' == a:
                asked_day = Days.FRIDAY.value
            elif 'saturday' == a or 'sat' == a:
                asked_day = Days.SATURDAY.value
            elif 'sunday' == a or 'sun' == a:
                asked_day = Days.SUNDAY.value
            elif 'd&d' == a or 'dnd' == a:
                asked_day = Days.DNDDAY.value
            if asked_day != -1:
                if asked_day == Days.DNDDAY.value:
                    if dnd_days[today] is True:
                        await message.channel.send(random.choice(yes))
                    else:
                        await message.channel.send(random.choice(no))
                else:
                    if today == asked_day:
                        await message.channel.send(random.choice(yes))
                    else:
                        await message.channel.send(random.choice(no))
        if evan_flag is True: # Send Evan a message if he is the one asking
            await message.channel.send(evan_message)
        return
    
    # New starting character
    elif mess_temp.startswith('&'):
        args = mess_temp[1:].split(' ') # Retrieve rest of message and format
        command = args[0]
        args = args[1:11] # Take max 10 args, cut out command
        
        if command == "help": # List out all commands
            await message.channel.send(
'''
Here are commands that can be used with IIFYBot:
.
**&dnd_days**: Displays what days are currently set as D&D days.
.
**&is_it [DAYS]**: Answers if today is the day(s) provided. This will process a maximum of 10 days. DAYS can consist of the full names of days, such as "Monday", or abbreviations of days, such as "Mon". It will also recognize "D&D Day" or "DnD Day" as a day, and will check against the set D&D days. It is not case sensitive.
.
**&help**: Provides the commands that can be used with IIFYBot.
.
**&rm_days [DAY_ABBRVS]**: Removes D&D days according to the abbreviations provided in DAY_ABBRVS. Valid abbreviaitons are 'M' for Monday, 'T' for Tuesday, 'W' for Wednesday, 'R' for Thursday, 'F' for Friday, 'S' for Saturday, and 'U' for Sunday. For example, to remove Friday and Sunday from D&D days, send the command "&rm_days FU".
.
**&rm_schedule [DATE]**: Removes the date provided from the schedule. DATE should be formatted as "MM-DD-YYYY". For example, a game on May 23, 2022 could be removed from the schedule using "&rm_schedule 05-23-2022".
.
'''
            )
            await message.channel.send(
'''
**&roll_stats**: Rolls stats for a new character.
.
**&schedule**: Displays any upcoming games that are scheduled. This is not self-updating, so games that have passed need to be removed manually. WARNING: Resetting the bot will reset the schedule.
.
**&set_days [DAY_ABBRVS]**: Sets D&D days according to the abbreviations provided in DAY_ABBRVS. Valid abbreviations are 'M' for Monday, 'T' for Tuesday, 'W' for Wednesday, 'R' for Thursday, 'F' for Friday, 'S' for Saturday, and 'U' for Sunday. For example, to set Tuesday and Thursday to be D&D days, send the command "&set_days TR".
.
**&set_schedule [DATE] [DM] [TYPE]**: Adds a game to the schedule. DATE should be formatted as "MM-DD-YYYY". DM is the name of the person running the game. TYPE is the type of game being ran, or the name of the campaign the game belongs to. For example, to add an SKT session ran by Ty on May 23, 2022 to the schedule, send the command "&set_schedule 05-23-2022 Ty SKT".
'''
            )
            return
        
        if command == "dnd_days": # Print out dnd days
            msg = "D&D days currently are:\n"
            msg_valid = False
            for i in range(7):
                if dnd_days[i] is True:
                    msg_valid = True
                    msg += (Days(i).name + '\n')
            if msg_valid is True:
                await message.channel.send(msg[:-1])
            else:
                await message.channel.send("There are no D&D days currently set.")
            return
        
        if command == "is_it": # Check what day it is
            for a in args: # Check for each weekday or dnd day
                asked_day = -1
                if 'monday' == a or 'mon' == a:
                    asked_day = Days.MONDAY.value
                elif 'tuesday' == a or 'tues' == a or 'chewsday' == a:
                    asked_day = Days.TUESDAY.value
                elif 'wednesday' == a or 'wed' == a:
                    asked_day = Days.WEDNESDAY.value
                elif 'thursday' == a or 'thurs' == a:
                    asked_day = Days.THURSDAY.value
                elif 'friday' == a or 'fri' == a:
                    asked_day = Days.FRIDAY.value
                elif 'saturday' == a or 'sat' == a:
                    asked_day = Days.SATURDAY.value
                elif 'sunday' == a or 'sun' == a:
                    asked_day = Days.SUNDAY.value
                elif 'd&d' == a or 'dnd' == a:
                    asked_day = Days.DNDDAY.value
                if asked_day != -1:
                    if asked_day == Days.DNDDAY.value:
                        if dnd_days[today] is True:
                            await message.channel.send(random.choice(yes))
                        else:
                            await message.channel.send(random.choice(no))
                    else:
                        if today == asked_day:
                            await message.channel.send(random.choice(yes))
                        else:
                            await message.channel.send(random.choice(no))
            if evan_flag is True: # Send Evan a message if he is the one asking
                await message.channel.send(evan_message)
            return

        if command == "izzet": # Check what day it is (easter egg)
            for a in args: # Check for each weekday or dnd day
                asked_day = -1
                if 'monday' == a or 'mon' == a:
                    asked_day = Days.MONDAY.value
                elif 'tuesday' == a or 'tues' == a or 'chewsday' == a:
                    asked_day = Days.TUESDAY.value
                elif 'wednesday' == a or 'wed' == a:
                    asked_day = Days.WEDNESDAY.value
                elif 'thursday' == a or 'thurs' == a:
                    asked_day = Days.THURSDAY.value
                elif 'friday' == a or 'fri' == a:
                    asked_day = Days.FRIDAY.value
                elif 'saturday' == a or 'sat' == a:
                    asked_day = Days.SATURDAY.value
                elif 'sunday' == a or 'sun' == a:
                    asked_day = Days.SUNDAY.value
                elif 'd&d' == a or 'dnd' == a:
                    asked_day = Days.DNDDAY.value
                if asked_day != -1:
                    if asked_day == Days.DNDDAY.value:
                        if dnd_days[today] is True:
                            await message.channel.send(random.choice(yes))
                        else:
                            await message.channel.send(random.choice(no))
                    else:
                        if today == asked_day:
                            await message.channel.send(random.choice(yes))
                        else:
                            await message.channel.send(random.choice(no))
            await message.channel.send("Do you like the new update Travis?")
            return
        
        if command == "rm_days": # Set days provided to False in dnd_days
            if len(args) == 0:
                await message.channel.send("No days provided.")
            else:
                for day_abbrv in args[0].lower():
                    rm_day = -1
                    if day_abbrv == 'm':
                        rm_day = 0
                    elif day_abbrv == 't':
                        rm_day = 1
                    elif day_abbrv == 'w':
                        rm_day = 2
                    elif day_abbrv == 'r':
                        rm_day = 3
                    elif day_abbrv == 'f':
                        rm_day = 4
                    elif day_abbrv == 's':
                        rm_day = 5
                    elif day_abbrv == 'u':
                        rm_day = 6
                    if rm_day != -1: # Remove day if valid
                        dnd_days[rm_day] = False
                await message.channel.send("D&D day(s) removed.")
            return
        
        if command == "rm_schedule": # Remove a game on DATE from schedule
            if len(args) == 0:
                await message.channel.send("No date provided.")
            else:
                date = args[0]
                if args[0] in schedule.keys():
                    schedule.pop(date)
                    await message.channel.send("Game removed from schedule.")
                else:
                    await message.channel.send("No game scheduled for the date provided.")
            return
        
        if command == "roll_stats": # Roll stats for a new character
            msg = "Your rolls are:\n"
            d6 = [1, 2, 3, 4, 5, 6]
            stats = []
            for i in range(6):
                rolls = []
                for j in range(4):
                    rolls.append(random.choice(d6))
                tot = sum(rolls) - min(rolls)
                msg += ("(" + str(rolls[0]) + ", " + str(rolls[1]) + ", " + str(rolls[2]) + ", " + str(rolls[3]) + "): " + str(tot) + "\n")
                stats.append(tot)
            msg += ("Your stats are: " + str(stats[0]) + ", " + str(stats[1]) + ", " + str(stats[2]) + ", " + str(stats[3]) + ", " + str(stats[4]) + ", " + str(stats[5]))
            await message.channel.send(msg)
            return

        if command == "schedule": # Display the current schedule
            msg = "Here is the current schedule:\n"
            msg_valid = False
            for k in sorted(schedule.keys()):
                msg_valid = True
                msg += (k + ": " + schedule[k][1] + " ran by " + schedule[k][0] + "\n")
            if msg_valid is True:
                await message.channel.send(msg[:-1])
            else:
                await message.channel.send("The schedule is currently empty.")
            return
                

        if command == "set_days": # Set days provided to True in dnd_days
            if len(args) == 0:
                await message.channel.send("No days provided.")
            else:
                for day_abbrv in args[0].lower():
                    rm_day = -1
                    if day_abbrv == 'm':
                        rm_day = 0
                    elif day_abbrv == 't':
                        rm_day = 1
                    elif day_abbrv == 'w':
                        rm_day = 2
                    elif day_abbrv == 'r':
                        rm_day = 3
                    elif day_abbrv == 'f':
                        rm_day = 4
                    elif day_abbrv == 's':
                        rm_day = 5
                    elif day_abbrv == 'u':
                        rm_day = 6
                    if rm_day != -1: # Add day if valid
                        dnd_days[rm_day] = True
                await message.channel.send("D&D day(s) set.")
            return
        
        if command == "set_schedule": # Add schedule info provided to schedule
            args = message.content.split(' ')[1:]
            if len(args) < 3:
                await message.channel.send("Incorrect number of arguments. Correct format is \"&set_schedule [DATE] [DM] [TYPE]\".")
            else:
                date = args[0]
                dm = args[1]
                typ = ""
                for arg in args[2:]:
                    typ += (arg + ' ')
                typ = typ[:-1]
                split_date = date.split('-')
                if len(split_date) == 3: # Check date validity
                    if split_date[0].isdigit() and int(split_date[0]) >= 1 and int(split_date[0]) <= 12:
                        if split_date[1].isdigit() and int(split_date[1]) >= 1 and int(split_date[1]) <= 31:
                            if split_date[2].isdigit() and len(split_date[2]) == 4:
                                format = "%m-%d-%Y"
                                date_dt = datetime.datetime.strptime(date, format)
                                if date_dt.date() >= datetime.datetime.today().date():
                                    schedule[date] = [dm, typ]
                                    await message.channel.send(typ + " ran by " + dm + " scheduled for " + date + ".")
                                else:
                                    await message.channel.send("Invalid date.")
                                return
                await message.channel.send("Invalid date format.")
            return

client.run(bot_key)