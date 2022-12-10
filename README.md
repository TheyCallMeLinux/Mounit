# Mounit

This script is a Discord bot written in Python. It uses the discord.py library to interact with the Discord API and implement various features.

The script starts by loading environment variables from a .env file using the dotenv package. It then creates a discord.ext.commands.Bot instance, which will be used to interact with the Discord API.

Next, the script defines some variables:

    minTime: The minimum time in seconds between each iteration of the test task.
    maxTime: The maximum time in seconds between each iteration of the test task.
    chanid: The Discord channel ID where the bot will post messages.
    adminid: The Discord user ID of the bot's administrator.

