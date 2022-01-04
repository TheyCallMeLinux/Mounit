import discord, asyncio, random
from discord.ext import commands, tasks
import aiohttp
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
    channel = bot.get_channel(YOUR_CHANNEL_ID)
    quoteList = ["All systems are functionnal"] 
    await channel.send(str(random.choice(quoteList)))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@bot.event
async def on_ready():
    
    print(f'{bot.user} succesfully logged in!') #Console message
    await bot.change_presence(activity=discord.Game(name="Learning about the human race")) #Discord presence (game, watching, listening)
    channel = bot.get_channel(YOUR_CHANNEL_ID)
    quote = get_quote()
    status = "[LAPTOP] UP! <@YOUR_USER_ID>" #Let the admin know it's up
    await channel.send(status)
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://aws.random.cat/meow') # Make a request
      catjson = await request.json() # Convert it to a JSON dictionary
    embed = discord.Embed(title="up!", color=discord.Color.purple())
    embed.set_image(url=catjson['file']) # Set the embed image to the value of the 'link' key
    embed.set_footer(text=(quote))
    await channel.send(embed=embed) # Send the embed
    test.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)


bot.run(os.getenv("DISCORD_TOKEN"))
