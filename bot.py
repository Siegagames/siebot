import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import asyncio
import random
import json
import os
import datetime
import traceback
import urllib.request, json
import urllib
#abc gewoon een voorbeeld om te zien
cp = '*' #kies zelf een commandprefix
bot = commands.Bot(command_prefix=cp)
print ('Bot is aan het opstarten...')

#zorgt ervoor dat de bot opstart
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Use *help | V1'))
    print('Bot is opgestart')

#de bot werkt hier als een soort chatbot
@bot.event
async def on_message(message):
	if message.content.lower() == ('cookie'):
		await bot.send_message(message.channel, ":cookie:")
	if message.content.lower() == ('hi'):																																	
		await bot.send_message(message.channel, "Hey! How are you doing?")
        
	await bot.process_commands(message) #dit zorgt ervoor dat de andere commands nog werken

#Kick command
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User, *, reden):
    """Kick a user"""
    try:
        await bot.kick(userName)
        await bot.say(f"*** :white_check_mark: {userName} is successful kicked for the following reason: {reden}***" (userName))
    except:
        await bot.say("This user doesn't exist!")

#ban command
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User, *, reden):
    """Ban a user"""
    try:
        await bot.ban(userName)
        await bot.say(f"*** :white_check_mark: {userName} is succesful banned for the following reason: {reden}***" (userName))
    except:
        await bot.say("This user doesn't exist!")

#Unban command
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user):
    """Unban a user"""
    try:
        a = bot.get_bans(ctx.message.server)
        member = discord.utils.get(a, name = user)
        await bot.unban(ctx.message.server, user)
        await bot.say(f'{member} is successful unbanned!')
    except:
        await bot.say("This user isn't banned!")

#Role command
@bot.command(pass_context = True)
async def give(ctx, rol):
    """Give yourself a role"""
    try:
        rol = rol.lower()
        rol = rol.title()
        role = discord.utils.get(ctx.message.server.roles, name=rol)
        await bot.add_roles(ctx.message.author, role)
        embed=discord.Embed(title="RoleGiver", description="You successful received the role!", color=0x00ff00)
        embed.set_footer(text="Made by Siega")
        await bot.say(embed=embed)
    except:
        embed=discord.Embed(title="RoleGiver", description="This role doesn't exist or is to high!", color=0xf50a21)
        embed.set_footer(text="Made by Siega")
        await bot.say(embed=embed)


bot.run(os.getenv('TOKEN')) #hier voer je je token in
