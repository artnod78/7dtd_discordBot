#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 10 avr. 2018

@author: artnod
'''
import sys, asyncio
from subprocess import Popen, PIPE
from discord.ext import commands
from BotLog.Botlog import getBotLogger
from settings import BOT_CONF


# Set up a specific logger with our desired output level
my_logger = getBotLogger('discord_bot')


bot = commands.Bot(command_prefix='/', description='A simple Bot to start/stop 7dtd server')

@bot.event
async def on_ready():
    """
    Bot Start
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    print('Logged in as {} - {}'.format(bot.user.name, bot.user.id))

@bot.group(pass_context=True)
async def start(ctx):
    """
    \tStart a specific server
    
    Usage: /start <command>
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    if ctx.invoked_subcommand is None:
        await bot.say('Failed !')
        await bot.say('Try **/help start** !')

@bot.group(pass_context=True)
async def stop(ctx):
    """
    \tStop a specific server
    
    Usage: /stop <command>
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    if ctx.invoked_subcommand is None:
        await bot.say('Failed !')
        await bot.say('Try **/help stop** !')

@start.command(pass_context=True)
async def sdtd(ctx):
    """
    \tStart sdtd server
    
    Usage: /start sdtd
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    channel = ctx.message.channel
    member = ctx.message.author
    if channel.id == BOT_CONF['bot_channel']:
        if member.id in BOT_CONF['bot_admin_list']:
            await bot.say('**{0.name}** try to start ** 7dtd server**!\r'.format(member))
            try:
                my_logger.info('{0.name} try to start 7dtd server'.format(member))
                p = Popen(["/usr/local/bin/7dtd.sh", "start", "!"], stdout=PIPE)
                toto = p.communicate()
                if toto[0] != None:
                    await bot.say(toto[0].decode('unicode_escape'))
                else:
                    await bot.say(toto[1].decode('unicode_escape'))
            except:
                my_logger.err('Command Failed')
                await bot.say('Command Failed!')
        else:
            my_logger.warn('{0.name} Access Denied'.format(member))
            await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
    else:
        my_logger.warn('{0.name} Bad channel'.format(member))
        await bot.say('**{0.name}** ! Bad channel!\r'.format(member))

@stop.command(pass_context=True)
async def sdtd(ctx):
    """
    \tStop sdtd server
    
    Usage: /stop sdtd
    """
    my_logger.debug(sys._getframe().f_code.co_name)
    channel = ctx.message.channel
    member = ctx.message.author
    if channel.id == BOT_CONF['bot_channel']:
        if member.id in BOT_CONF['bot_admin_list']:
            await bot.say('**{0.name}** try to stop ** 7dtd server**!\r'.format(member))
            try:
                my_logger.info('{0.name} try to stop 7dtd server'.format(member))
                p = Popen(["/usr/local/bin/7dtd.sh", "kill", "!"], stdout=PIPE)
                toto = p.communicate()
                if toto[0] != None:
                    await bot.say(toto[0].decode('unicode_escape'))
                else:
                    await bot.say(toto[1].decode('unicode_escape'))
            except:
                my_logger.err('Command Failed')
                await bot.say('Command Failed!')
        else:
            my_logger.warn('{0.name} Access Denied'.format(member))
            await bot.say('**{0.name}** ! Access Denied!\r'.format(member))
            
    else:
        my_logger.warn('{0.name} Bad channel'.format(member))
        await bot.say('**{0.name}** ! Bad channel!\r'.format(member))

if __name__ == '__main__':
    my_logger.info('Start Discord Bot')
    bot.run(BOT_CONF['bot_token'])
    