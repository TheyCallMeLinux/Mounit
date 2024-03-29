import discord, asyncio, random
from discord.ext import commands, tasks
import aiohttp
import datetime
import requests
import secrets
import math
import json
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from random import randint

load_dotenv()

# Get the Discord token from the environment
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

minTime = 300
maxTime = 1600
channelid = os.getenv("CHANNELID")
adminid = os.getenv("ADMINID")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

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

    if message.content == "!ping":
       startTime = datetime.datetime.now()
       sentMessage = await message.channel.send("Pinging...")
       latency = (datetime.datetime.now() - startTime).total_seconds() * 1000
       await sentMessage.edit(content="Pong! Latency is {} ms.".format(int(latency)))


    if message.content == '!wallpaper':
        # Get the list of wallpaper file names
        response = requests.get('https://api.github.com/repos/DenverCoder1/minimalistic-wallpaper-collection/contents/images')
        wallpaper_filenames = [item['name'] for item in response.json()]

        # Choose a random wallpaper file
        random_filename = random.choice(wallpaper_filenames)
        image_url = f'https://github.com/DenverCoder1/minimalistic-wallpaper-collection/raw/main/images/{random_filename}'

        embed = discord.Embed(color=discord.Color.orange())
        embed.set_image(url=image_url)
        msg = await message.channel.send(embed=embed)

        await msg.add_reaction('⬅️')
        await msg.add_reaction('➡️')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in ['⬅️', '➡️']

        while True:
            try:
                reaction, user = await bot.wait_for('reaction_add', check=check, timeout=120)
            except asyncio.TimeoutError:
                break
            else:
                await reaction.remove(user)
                if str(reaction.emoji) == '➡️':
                    # Choose the next wallpaper file in the list
                    current_index = wallpaper_filenames.index(random_filename)
                    random_filename = wallpaper_filenames[(current_index + 1) % len(wallpaper_filenames)]
                    image_url = f'https://github.com/DenverCoder1/minimalistic-wallpaper-collection/raw/main/images/{random_filename}'
                    embed = discord.Embed(color=discord.Color.orange())
                    embed.set_image(url=image_url)
                    await msg.edit(embed=embed)
                    await msg.add_reaction('⬅️')
                    await msg.add_reaction('➡️')
                elif str(reaction.emoji) == '⬅️':
                    # Choose the previous wallpaper file in the list
                    current_index = wallpaper_filenames.index(random_filename)
                    random_filename = wallpaper_filenames[(current_index - 1) % len(wallpaper_filenames)]
                    image_url = f'https://github.com/DenverCoder1/minimalistic-wallpaper-collection/raw/main/images/{random_filename}'
                    embed = discord.Embed(color=discord.Color.orange())
                    embed.set_image(url=image_url)
                    await msg.edit(embed=embed)
                    await msg.add_reaction('⬅️')
                    await msg.add_reaction('➡️')

    if message.content == "!anime":
        random_number = randint(1, 107)
        url = f"https://hdqwalls.com/category/anime-wallpapers/page/{random_number}"
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        images = []

        for img in soup.find_all('img', class_="thumbnail img-responsive custom_width"):
            images.append(img['src'])

        limit = len(images)
        pg = 0

        #embed = discord.Embed(color="#FF69B4")
        embed = discord.Embed(color=discord.Colour(value=int("FF69B4", 16)))
        embed.set_image(url=images[0].replace("/thumb", ""))

        msg = await message.channel.send(embed=embed)

        await msg.add_reaction("⬅️")
        await msg.add_reaction("➡️")

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in ["⬅️", "➡️"]

        while True:
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=120.0, check=check)
            except asyncio.TimeoutError:
                break
            else:
                if str(reaction.emoji) == "➡️":
                    if not images[pg + 1]:
                        pg = pg
                    else:
                        pg = pg + 1
                    #embed = discord.Embed(color="#FF69B4")
                    embed = discord.Embed(color=discord.Colour(value=int("FF69B4", 16)))
                    embed.set_image(url=images[pg].replace("/thumb", ""))
                    await msg.edit(embed=embed)
                    await msg.remove_reaction("➡️", user)
                    await msg.add_reaction("⬅️")
                    await msg.add_reaction("➡️")
                elif str(reaction.emoji) == "⬅️":
                    if not images[pg - 1]:
                        pg = pg
                    else:
                        pg = pg - 1
                    #embed = discord.Embed(color="#FF69B4")
                    embed = discord.Embed(color=discord.Colour(value=int("FF69B4", 16)))
                    embed.set_image(url=images[pg].replace("/thumb", ""))
                    await msg.edit(embed=embed)
                    await msg.remove_reaction("⬅️", user)
                    await msg.add_reaction("⬅️")
                    await msg.add_reaction("➡️")

    if message.content.startswith("!purge"):
        number_str = message.content[len("purge"):].strip()
        try:
            number = int(number_str)
        except ValueError:
            return await message.channel.send("Invalid number of messages to delete.")

        if number < 1 or number > 100:
            return await message.channel.send("Number of messages to delete must be between 1 and 100.")
    
        # delete the command message
        await message.delete()

        # delete the specified number of messages
        await message.channel.purge(limit=number+1)


    #basic math functions (sqrt, sin, cos, tan, pi).
    elif message.content.startswith("!calc "):
        try:
            equation = message.content[6:]
            result = eval(equation, {"__builtins__": None}, {"sqrt": math.sqrt, "sin": math.sin, "cos": math.cos, "tan": math.tan, "pi": math.pi})
        except Exception:
            await message.channel.send("Error: Invalid equation")
            return

        await message.channel.send(result)

    elif message.content.find("quote") != -1:
        quote = get_quote()
        await message.channel.send(quote)


    elif message.content == "hello":
        await message.channel.send(f"Hi {message.author.nick}")
    elif message.content == "bye":
        await message.channel.send(f"Goodbye {message.author.nick}")
    if message.content == "!news":
        # Set the API endpoint URL
        API_ENDPOINT = "https://newsapi.org/v2/top-headlines?country=us&category=technology"

        # Set the headers
        headers = {
            "X-Api-Key": NEWS_API_KEY
        }

        # Send the request
        response = requests.get(API_ENDPOINT, headers=headers)

        # Check if the response was successful
        if response.status_code != 200:
            print("Error: Failed to fetch news")
            return

        # Convert the response to a JSON object
        response_json = response.json()

        # Make sure that the 'response_json' variable has been assigned a value
        if response_json is None:
            print("Error: 'response_json' is not defined")
            return

        # Loop through the list of articles in the response
        for i, article in enumerate(response_json["articles"]):
	    # Send the news article to the channel only if the current index is less than 5
            if i < 5:
                await message.channel.send(article["url"])

    if message.content == "!hackernews":
        # Get the top stories from Hacker News
        response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        top_stories = response.json()
        # Create a message with the top stories
        news_message = "Here are the top stories from Hacker News:\n\n"
        for story_id in top_stories[:10]:
            # Get the details for each story
            story_response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
            story_details = story_response.json()

            # Check if the story has a URL
            if "url" in story_details:
                # Add the story title and URL to the message
                news_message += f"{story_details['title']}: {story_details['url']}\n"
            else:
                # Handle the case where the story does not have a URL
                news_message += f"{story_details['title']}: (no URL available)\n"

        # Send the message to the same channel where the "hackernews" message was sent
        await message.channel.send(news_message)

    else:
        return


bot.run(TOKEN)
