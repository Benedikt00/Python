import discord
import time
import asyncio

token = "token"

client = discord.Client()
obfuckkinder = ["vogi31#0926", "Johannes#1695"]
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == "t027":
            await client.send_message(f"Wilkommen auf dem Server {member.mention}. Wennst blödsinn machst bist glei wieder weg")

@client.event
async def on_message(message):
    id = client.get_guild(779345414197215233)
    channels = ["bot"]

    if str(message.channel) in channels:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members {id.member_count}""")
        elif message.content.find("!nuke") != -1:
            await 

    if str(message.author) in obfuckkinder:
        if message.content.find("!hello") != -1:
            await message.channel.send("Du kleiner pisser")




client.run(token)
