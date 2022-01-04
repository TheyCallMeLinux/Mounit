from typing import Text
import discord, asyncio, random
from discord.ext import commands, tasks
import aiohttp
import datetime
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="!")
minTime = 300 #minimum time in seconds
maxTime = 1600 #maximum time in seconds

@tasks.loop(seconds=random.randint(minTime, maxTime))
async def test():
    channel = bot.get_channel(YOURCHANNELID)
    print("Started Reading JSON file")
    with open('./sentences-en.json') as read_file:
      sentences = json.load(read_file)
    await channel.send(str(random.choice(sentences)))
    #await channel.send(str(random.choice(sentences['sentence'])))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.event
async def on_ready():
    
    print(f'{bot.user} succesfully logged in!') #Console message
    await bot.change_presence(activity=discord.Game(name="Learning about the human race")) #Discord presence (game, watching, listening)
    channel = bot.get_channel(YOURCHANNELID)
    quote = get_quote()
    status = "[LAPTOP] UP! <@YOURUSERID>" #Let the admin know
    await channel.send(status)
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://aws.random.cat/meow') # Make a request
      catjson = await request.json() # Convert it to a JSON dictionary
    embed = discord.Embed(title="up!", color=discord.Color.purple())
    embed.set_image(url=catjson['file']) # Set the embed image to the value of the 'file' key
    embed.set_footer(text=(quote))
    await channel.send(embed=embed) # Send the embed
    test.start()

@bot.event
async def on_message(message):
    x=0
    if message.author == bot.user:   
        return
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')
    if message.content == "keyword":
        logmess = "Command keyword ran by"+str({message.author.nick})+"at:"+str(datetime.datetime.now())+"\n"
        f=open("log.txt", "a+")
        f.write(logmess)
        game=discord.Game(name="testing stuff")
        await bot.change_presence(activity=game)
        while x < 5:
            await message.channel.send("""test""")
            x=x+1
        else:
            return

bot.run(os.getenv("DISCORD_TOKEN"))
