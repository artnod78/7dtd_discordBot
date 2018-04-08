# 7dtd_discordBot
  * Start/Stop 7dtd instances. ( Discord Bot )
  * Send message when instances' state changed. ( Discord WebHook )

## Install
  * Install Python3  
  `apt-get install python3 python3-pip`
  * Install discord.py  
  `pip3 install discord`
  * Download discord_bot.py  
  `wget https://raw.githubusercontent.com/artnod78/7dtd_discordBot/master/discord_bot.py`  
  Set as executable `chmod +x discord_bot.py`
  * Download discord_hooks.py  
  `wget https://raw.githubusercontent.com/artnod78/7dtd_discordBot/master/discord_hooks.py`  
  Set as executable `chmod +x discord_hooks.py`

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

In **discord_hooks.py**, edit with your settings:
```
webhook_url = 'https://discordapp.com/api/webhooks/id/token'
server_ip = '127.0.0.1'
```
