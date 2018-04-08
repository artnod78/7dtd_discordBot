import discord
from discord.ext import commands
import asyncio
from subprocess import Popen, PIPE
import sys


bot_channel = '<channel_id>'
bot_token = '<bot_token>'
admin_list=('<admin_id>',)

STARTCMD = ["/usr/local/bin/7dtd.sh", "start", "!"]
STOPCMD = ["/usr/local/bin/7dtd.sh", "kill", "!"]

description = '''A simple Bot to start/stop 7dtd server'''
bot = commands.Bot(command_prefix='/', description=description)

@bot.event
async def on_ready():
	print('Logged in as {} - {}'.format(bot.user.name, bot.user.id))
	print('------')

@bot.group(pass_context=True)
async def start(ctx):
	"""
	\tStart a specific server
	
	Usage: /start <command>
	"""
	if ctx.invoked_subcommand is None:
		await bot.say('Failed !')
		await bot.say('Try **/help start** !')

@bot.group(pass_context=True)
async def stop(ctx):
	"""
	\tStop a specific server
	
	Usage: /stop <server>
	"""
	if ctx.invoked_subcommand is None:
		await bot.say('Failed !')
		await bot.say('Try **/help stop** !')
		
		
@start.command(pass_context=True)
async def sdtd(ctx):
	"""
	\tStart sdtd server
	
	Usage: /start sdtd
	"""
	channel = ctx.message.channel
	member = ctx.message.author
	if channel.id == bot_channel:
		if member.id in admin_list:
			await bot.say('**{0.name}** try to start ** 7dtd - Vannilla** server\r'.format(member))
			try:
				p = Popen(STARTCMD, stdout=PIPE)
				toto = p.communicate()
				if toto[0] != None:
					await bot.say(toto[0].decode('unicode_escape'))
				else:
					await bot.say(toto[1].decode('unicode_escape'))
			except:
				await bot.say('Command Failed!')
		else:
			await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
			
	else:
		await bot.say('**{0.name}** ! Bad channel!\r'.format(member))

@stop.command(pass_context=True)
async def sdtd(ctx):
	"""
	\tStop sdtd server
	
	Usage: /stop sdtd
	"""
	channel = ctx.message.channel
	member = ctx.message.author
	if channel.id == bot_channel:
		if member.id in admin_list:
			await bot.say('**{0.name}** try to stop ** 7dtd - Vannilla** server\r'.format(member))
			try:
				p = Popen(STOPCMD, stdout=PIPE)
				toto = p.communicate()
				if toto[0] != None:
					await bot.say(toto[0].decode('unicode_escape'))
				else:
					await bot.say(toto[1].decode('unicode_escape'))
			except:
				await bot.say('Command Failed!')
		else:
			await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
			
	else:
		await bot.say('**{0.name}** ! Bad channel!\r'.format(member))
		
bot.run(bot_token)