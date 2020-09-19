import discord
from discord.ext import commands

import asyncio

import cogs

import json_manager

import os 

token=json_manager.get(json_manager.config_file_uri, "token")
prefix=json_manager.get(json_manager.config_file_uri, "prefix")

if token == "":
    print("error token is not defined !")
elif prefix == "":
    print("error prefix is not defined !")
else:
    bot=commands.Bot(command_prefix=prefix, description="Bot of group !")
    
    @bot.event
    async def on_ready():
        print("Bot Started !")

    @bot.command()
    async def load(ctx, name=None):
        if name:
            bot.load_extension(name)
            print(name, "has been loaded")
            await ctx.send(str(name + " has been loaded"))
        
    @bot.command()
    async def unload(ctx, name=None):
        if name:
            bot.unload_extension(name)
            print(name, "has been unloaded")
            await ctx.send(str(name + " has been unloaded"))

    @bot.command()
    async def reload(ctx, name=None):
        if name:
            try:
                bot.reload_extension(name)
                print(name, "has been reloaded")
                await ctx.send(str(name + " has been reloaded"))
            except:
                bot.load_extension(name)
                print(name, "has been loaded")
                await ctx.send(str(name + " has been loaded"))

    for file in os.listdir("./commands"):
        if file.endswith(".py"):
            bot.load_extension(f'commands.{file[:-3]}')
            print(file, "has been loaded")

    bot.run(token)
