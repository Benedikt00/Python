import discord
from discord.ext import commands
import datetime
import pyautogui as pg

from urllib import parse, request
import re

token = "ODc1NDM1OTc0NDgwNTIzMzE0.YRVfSQ.OW2dEq6a_l9imr_Qce2aBGLcjjQ"

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

client = discord.Client()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Eventsdu hunt
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Marci", url="http://www.twitch.tv/marci_9877"))
    print('My Ready is Body')



@bot.listen()
async def on_message(message):
    id = client.get_guild(779345414197215233)
    channels = ["bot"]

    if "tutorial" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is that you want http://youtube.com/fazttech')
        await bot.process_commands(message)

    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members {id.member_count}""")
        elif message.content.find("!seidelschmutz") != -1:
            for x in range(100):
                await message.channel.send("@Julian du hunt")
        elif message.content.find("!little simbürger") != -1:
            await message.channel.send("https://www.youtube.com/watch?v=cOb6xz1MXt4")
            await message.channel.send("Go little rockstar")

bot.run(token)