import discord
from discord.ext import commands
import json

with open("config.json") as f:
    config = json.load(f)

client = commands.Bot(command_prefix = config["prefix"])

bannedwords = ["test"]

@client.event
async def on_ready():
    print("Status : ONLINE")

@client.command()
async def word(ctx):
    bannedwords.append(ctx.message).lower()


@client.event
async def on_message(message):
    log_channel = client.get_channel(config["channel"])
    if any(word in message.content for word in bannedwords):
        await message.delete()
        await message.channel.send(f"{message.author.mention} That Word Is Not Allowed To Be Used!")
    else:
        await client.process_commands(message)

client.run(config["token"])