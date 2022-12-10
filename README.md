# Mounit

This script is a Discord bot written in Python that uses the discord.py library to interact with the Discord API and implement various features.
Setup

The script starts by loading environment variables from a .env file using the dotenv package. It then creates a discord.ext.commands.Bot instance to interact with the Discord API.
Variables

Requirements:
    pip install python-dotenv
    pip install discord

Config the edit dotENV file:
    ADMINID=<ADMINISTRATOR_DISCORD_ID>
    CHANNELID=<CHANNELID>
    DISCORD_TOKEN=<DISCORD_BOT_TOKEN>

The following variables are defined in the script:

    minTime: The minimum time in seconds between each iteration of the test task.
    maxTime: The maximum time in seconds between each iteration of the test task.
    chanid: The Discord channel ID where the bot will post messages.
    adminid: The Discord user ID of the bot's administrator.

Functions

The following functions are defined in the script:

    test task: This task will run in the background and will send a random sentence from the sentences-en.json file to the specified Discord channel at random intervals (between minTime and maxTime seconds).
    get_quote: This function makes a request to the zenquotes.io API to get a random quote.
    on_ready: This event handler will be called when the bot has successfully connected to the Discord API and is ready to receive messages. This function sends a message to the specified Discord channel to let the administrator know that the bot is up and running, and also sets the bot's presence on Discord. It also sends a random quote to the Discord channel, along with a random cat image from the aws.random.cat API.
    on_message: This event handler will be called whenever the bot receives a message on Discord. The function first checks if the message was sent by the bot itself, and if so, it does nothing. Otherwise, the function checks if the message content is one of a few predefined strings (e.g. "hello", "bye", "news"). If the message matches one of these strings, the bot will respond with a predefined message.
