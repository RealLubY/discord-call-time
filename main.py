import discord
from discord.ext import commands
import datetime
import time

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")

@bot.event
async def on_ready():
    for ch in bot.private_channels:
        print(f"{ch} - ID: {ch.id}")
    channel = int(input("Channelid\n"))
    timelist = []
    async for message in bot.get_channel(channel).history(limit=None):
        if message.type == discord.MessageType.call:
            timelist.append(message.call.duration.total_seconds())
    total_time = 0
    for i in timelist:
        total_time += i
    print(f"{str(datetime.timedelta(seconds=total_time))}")

bot.run("", bot=False) # TOKEN