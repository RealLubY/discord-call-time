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
        if message == None:
            continue
        if message.type == discord.MessageType.call:
            print(f"Call: {message.call.duration} - Secs: {message.call.duration.total_seconds()} - ID: {message.id}")
            timelist.append(message.call.duration.total_seconds())
    total_time = 0
    for i in timelist:
        total_time += i
    print("-----------")
    print(f"{str(datetime.timedelta(seconds=total_time))} -- SECS: {total_time}")
    print("-----------")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandNotFound):
        return
    raise error

bot.run("", bot=False) # TOKEN
