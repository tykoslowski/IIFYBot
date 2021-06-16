# IIFYBot
"Is it Friday yet?" bot for Discord!

This bot lets the user know what day it is when they ask "Is it (day)?"

I tried to create a JavaScript version of the bot to make keeping it up easier, but it ended up being buggy. More fixes to come!

To get this running, update the main.py file in the bot's directory:
- Use FileZilla to transfer the new main.py file to the bot's directory
- SSH into the directory using the username and password found on the Vultr website
- Use "pm2 start main.py --interpreter python3" to begin running the main file for the server
- If there are errors, use "pm2 logs" to check the errors
- To check the status of the server, use "pm2 status"
- To stop the server, use "pm2 stop"