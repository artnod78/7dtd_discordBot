#!/usr/bin/python3
#-*- coding: utf-8 -*-
import asyncio
from discord.ext import commands
from subprocess import Popen, PIPE

bot_token = 'Mzg1MDUwMDUyNTI5MjI1NzM4.DP7u-g.1OUU_lPMexdNSM81VXWqinUGTvE'
bot_channel = '383600437602942978'
bot_admin_list = ('355484130722709506',)


bot = commands.Bot(command_prefix='/', description='A simple Bot to start/stop 7dtd server')

@bot.event
async def on_ready():
    """
    Bot Start
    """
    print('Logged in as {} - {}'.format(bot.user.name, bot.user.id))

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
    
    Usage: /stop <command>
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
        if member.id in bot_admin_list:
            await bot.say('**{0.name}** try to start ** 7dtd server**!\r'.format(member))
            try:
                p = Popen(["/usr/local/bin/7dtd.sh", "start", "!"], stdout=PIPE)
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
        await bot.say('**{0.id}** ! Bad channel!\r'.format(member))

@stop.command(pass_context=True)
async def sdtd(ctx):
    """
    \tStop sdtd server
    
    Usage: /stop sdtd
    """
    channel = ctx.message.channel
    member = ctx.message.author
    if channel.id == bot_channel:
        if member.id in bot_admin_list:
            await bot.say('**{0.name}** try to stop ** 7dtd server**!\r'.format(member))
            try:
                p = Popen(["/usr/local/bin/7dtd.sh", "kill", "!"], stdout=PIPE)
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
        await bot.say('**{0.id}** ! Bad channel!\r'.format(member))

if __name__ == '__main__':
    bot.run(bot_token)
    