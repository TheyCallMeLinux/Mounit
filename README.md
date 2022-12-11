

(BETA)

# Mounit

This little guy might not have all the bells and whistles of some of the other bots out there, but what he lacks in features he makes up for in pure, unadulterated fun. Whether he's sending out random sentences, quoting your favorite philosophers, or just chatting with your users, Mounit is sure to keep things interesting. So if you're looking for a low-maintenance and configurable bot that's all about having a good time, give Mounit a try!


## Features

-   The bot will automatically post a random sentence from the `sentences-en.json` file in a specified channel every 5-25 minutes.
-   The bot will post a random quote and a cat image in the specified channel when it starts up.
-   The bot can respond to the following commands:
    -   `hello`: The bot will respond with "Hi <user>"
    -   `bye`: The bot will respond with "Goodbye <user>"
    -   `news`: The bot will respond with a link to the BBC news website


## Requirements:

Make sure you have Python 3.6 or newer installed on your system (example uses python3.8). If you don't have it installed, you can download it using the following command in your terminal:

    apt install python3.8

Install pip, the Python package manager, if you don't already have it. You can do this by running the following command in your terminal:

    apt install python3-pip

Once pip is installed, you can use it to install the required libraries for discord. To do this, run the following command in your terminal:

    pip3 install -U discord
    pip3 install -U discord.py
    pip3 install -U python-dotenv
    pip3 install -U aiohttp
    pip3 install -U beautifulsoup4
    
Or

    pip install -U discord.py aiohttp python-dotenv
    
    

## Running the bot

To run the bot, follow these steps:
Create a new bot on Discord and get the token by following these instructions.
https://discordnet.dev/guides/getting_started/first-bot.html

Create or edit the .env file in the same directory as the script and add the following environment variables:


    TOKEN=<DISCORD_BOT_TOKEN_SECRET>
    ADMINID=<ADMINISTRATOR_DISCORD_ID>
    CHANNELID=<YOUR_DISCORD_CHANNEL_ID>



## Rundown:

The following variables are defined in the script:

***minTime***: The minimum time in seconds between each iteration of the test task.

***maxTime***: The maximum time in seconds between each iteration of the test task.

***channelid***: The Discord channel ID where the bot will post messages.

***adminid***: The Discord user ID of the bot's administrator.



## Functions
The following functions are defined in the script:

 ***test task***: This task will run in the background and will send a random sentence from the sentences-en.json file to the specified Discord channel at random intervals (between minTime and maxTime seconds).

 ***get_quote***: This function makes a request to the zenquotes API to get a random quote.

***on_ready***: This event handler will be called when the bot has successfully connected to the Discord API and is ready to receive messages. This function sends a message to the specified Discord channel to let the administrator know that the bot is up and running, and also sets the bot's presence on Discord. It also sends a random quote to the Discord channel, along with a random cat image from the aws.random.cat API.

***on_message***: This event handler will be called whenever the bot receives a message on Discord. The function first checks if the message was sent by the bot itself, and if so, it does nothing. Otherwise, the function checks if the message content is one of a few predefined strings (e.g. "hello", "bye", "news"). If the message matches one of these strings, the bot will respond with a predefined message.

## License

**This project is licensed under the MIT License**

> *The MIT License is a super flexible and chill open-source license that lets you do whatever you want with your code, as long as you're
> not a total jerk and give credit where it's due. Basically, it's like
> the "Live and let live" of software licenses. Other developers can
> take your code, modify it, and even make their own versions of it. And
> all they have to do is include a copy of the MIT License with their
> code and say "Thanks, nerd!"*
> 
> *In short, the MIT License is like the cool older sibling of software licenses. It's not strict, it's not uptight, and it lets you have all
> the freedom you need to do your own thing. Plus, it's short and sweet,
> so you don't have to read a whole novel just to understand what you
> can and can't do with your code.*
> 
> -chat.openai

