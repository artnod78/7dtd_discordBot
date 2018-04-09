# 7dtd_discordBot
  * Start/Stop 7dtd instances. ( Discord Bot )
  * Send message when instances' state changed. ( Discord WebHook )

## Install
  * Install **Python3**  
  `apt-get install python3 python3-pip`
  * Install **discord.py**  
  `pip3 install discord`
  * Download **discord_bot.py**  
  `wget https://raw.githubusercontent.com/artnod78/7dtd_discordBot/master/discord_bot.py`  
  Set as executable `chmod +x discord_bot.py`
  * Download **discord_hooks.py**  
  `wget https://raw.githubusercontent.com/artnod78/7dtd_discordBot/master/discord_hooks.py`  
  Set as executable `chmod +x discord_hooks.py`

## WebHook
Webhooks are a low-effort way to post messages to channels in Discord.  
They do not require a bot user or authentication to use.

### Create WebHook
  * Go on your discord server
  * Edit a chat room
  * Create **Webhooks**
  * And get **webhook url**

### Configuration
In **discord_hooks.py**, edit with your settings:
```
webhook_url = 'https://discordapp.com/api/webhooks/ID/TOKEN'
server_ip = '127.0.0.1'
```

## Bot
Bot are a way to user interact with third tier app.  

### Create Bot
  * Go on: https://discordapp.com/developers/applications/me
  * Create **App**
  * Get **Client ID**
  * In **App** create **App Bot User**
  * And get **Token**
  * Go on: https://discordapp.com/oauth2/authorize?client_id=CLIENID&scope=bot Replace **CLIENTID** by your app Client ID
  * And add Bot in your server  

### Channel configuration
  * Go on your discord server
  * Add **Read/Write messages** permissions for bot on desired channel  

### Get channel id
  * Go on: https://discordapp.com and open Discord Web version
  * Go on desired channel
  * **Channel Id** is the LATEST PART of url  
Ex:  
channel url = [https://discordapp.com/channels/214128975172516813/**328301020429018971**  ](https://discordapp.com/channels/214128975172516813/328301020429018971)  
channel id = 328301020429018971  

### Get User Id
  * Go on your discord server
  * User Settings > Appearance > Enable Developer Mode > Done
  * Find user on the right side in the User panel > Right click > Copy ID  

### Configuration
In **discord_bot.py**, edit with your settings:
```
bot_channel = '<channel_id>'
bot_token = '<bot_token>'
admin_list=('<admin_id>',)
```  


