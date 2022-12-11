from typing import Text
import discord, asyncio, random
from discord.ext import commands, tasks
import aiohttp
import datetime
import requests
import secrets
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Get the Discord token from the environment
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

minTime = 300
maxTime = 1600
channelid = os.getenv("CHANNELID")
adminid = os.getenv("ADMINID")

if minTime >= maxTime:
    raise ValueError("maxTime must be greater than minTime")

# Use the secrets module to generate cryptographically secure random numbers
@tasks.loop(seconds=secrets.randbelow(maxTime) + minTime)
async def test():
    channel = bot.get_channel(int(channelid))
    if channel is None:
        print("Error: Invalid channel ID")
        return
    with open('./sentences-en.json') as f:
        data = json.loads(f.read())
        sentences = random.choice(data)
        print(sentences)
    # Use the discord.utils.escape_markdown() function to escape any special characters in the generated sentences
    await channel.send(discord.utils.escape_markdown(sentences))

def get_quote():
  # Use HTTPS to protect the data transmitted in the request
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.event
async def on_ready():
    
    print(f'{bot.user} succesfully logged in!') #Console message
    await bot.change_presence(activity=discord.Game(name="Learning about the human race")) #Discord presence (game, watching, listening)
    channel = bot.get_channel(int(channelid))
    if channel is None:
        print("Error: Invalid channel ID")
        return
    quote = get_quote()
    status = (f"<@{adminid}> the machine is up!") #Let the admin know
    await channel.send(status)
    async with aiohttp.ClientSession() as session:
      # Use HTTPS to protect the data transmitted in the request
      request = await session.get('https://aws.random.cat/meow') # Make a request
      catjson = await request.json() # Convert it to a JSON dictionary
    embed = discord.Embed(title="up!", color=discord.Color.purple())
    embed.set_image(url=catjson['file']) # Set the embed image to the value of the 'file' key
    embed.set_footer(text=(quote))
    await channel.send(embed=embed) # Send the embed
    print("Started Reading JSON file")
    test.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == "hello":
        await message.channel.send(f"Hi {message.author.nick}")
    elif message.content == "bye":
        await message.channel.send(f"Goodbye {message.author.nick}")
    elif message.content == "news":
        logmess = "Command news ran by"+str({message.author.nick})+"at:"+str(datetime.datetime.now())+"\n"
        f=open("log.txt", "a+")
        f.write(logmess)
        await message.channel.send("http://www.bbc.com/news/world")
    else:
        return

bot.run(TOKEN)
