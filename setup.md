You will need some sort of server in order to run this bot.
You can run this bot from your personal computer or use a free hosting service such as heroku.
I will make a video eventually  to show you how to complete such a task.

To run this bot open discord developers portal (https://discord.com/developers/applications)
Click on applications - New Application (Name the bot)
Press on Bot - Add Bot
Copy the token
Enable both intents (Presence Intent and Server Members Intent)

To invite the bot press OAuth2 and press bot then scroll and give the bot Administrator to be quicker.

Input the token in config.py e.g. "token":"copy here", "prefix" : "Your Prefix"

If you are running the bot locally make sure you have python 3.9+ if working after 3.9 and pip.
You will then need to open a command line and write pip install discord.py.
After installing discord.py you will need to run bot.py by double clicking it.

Make sure to add the words into the bannedwords[] list inside of bot.py in the format bannedwords["word1", "word2"]
If the bot encounters a word it will send a warning with a mention of the culprit.