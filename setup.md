You will need some sort of server in order to run this bot.
You can run this bot from your personal computer or use a free hosting service such as heroku.
I will make a video eventually  to show you how to complete such a task.

To run this bot open discord developers portal (https://discord.com/developers/applications)
Click on applications - New Application (Name the bot)
Press on Bot - Add Bot
Copy the token
Enable both intents (Presence Intent and Server Members Intent)

To invite the bot press OAuth2 and press bot then scroll and give the bot Administrator to be quicker.

If you are running the bot locally make sure you have python 3.9+ if working after 3.9 and pip.
You will then need to open a command line and write pip install discord.py.
After installing discord.py you will need to run bot.py by double clicking it.

To log the warning you will need to specify the id of the channel in config.json in format "channel" : "ID" 

To select words do f!word <WORD>
If you want to prevent words being deleted on bot restart enter them in bannedwords[] in bot.py in format ["Word1", "Word2", "Word3"] and make sure theyre lowercase!!!
If the bot encounters a word it will send a warning to the user.