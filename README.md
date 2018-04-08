# 7dtd_discordBot
7dtd, discord, bot, 7 days to die

## Install
  * Install Python3  
  `apt-get install python3 python3-pip`
  * Install discord.py  
  `pip install discord`
  * Download discord_bot.py  
  `wget https://raw.githubusercontent.com/artnod78/7dtd_discordBot/master/discord_bot.py`  
  Set as executable `chmod +x discord_bot.py`
  * Download discord_hook.py  
  `wget https://raw.githubusercontent.com/artnod78/7dtd_discordBot/master/discord_hook.py`  
  Set as executable `chmod +x discord_hook.py`

## Create Bot
  * Go to: https://discordapp.com/developers/applications/me
  * Create **App**
  * In **App** create **App Bot User**
  * And get **Token**

## Create WebHook
  * Go on your discord server
  * Edit a chat room
  * Create **Webhooks**
  * And get **webhook url**
 
## Configuration
In **discord_bot.py**, edit with your settings:
```
bot_channel = '<channel_id>'
bot_token = '<bot_token>'
admin_list=('<admin_id>',)
```  

In **discord_hook.py**, edit with your settings:
```
webhook_url = 'https://discordapp.com/api/webhooks/id/token'
hostname = 'server ip'
port = 26700
servername = 'server name'
```
