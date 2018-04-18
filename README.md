# 7dtd_discordBot
Simple Discord Bot/Webhook for 7dtd Linux management scripts.  
**Required** 7dtd Linux management scripts, available on https://7dtd.illy.bz/  
Features:
  * Start/Stop 7dtd instances. ( Discord Bot )
  * Send message when instances' state changed. ( Discord WebHook )

This wiki will guide you to get settings:  
[wiki](https://github.com/artnod78/7dtd_discordBot/wiki)  
For suggest or help, go on discord:  
[discord](https://discord.gg/dszbz)  

## Install
```
wget https://raw.githubusercontent.com/artnod78/7dtd_discordBot/master/bootstrap/bootstrap.sh
chmod +x bootstrap.sh
./bootstrap.sh -i
```  

## Config
Edit `/usr/local/bin/sdtdbot/settings.py` with your settings.  

### Bot Config
```
BOT_CONF = {
    'bot_token' : '<token>',
    'bot_channel' : '<channel>',
    'bot_admin_list' : ('<user>',),
}
```
Replace **\<token>** by bot token  
Replace **\<channel>** by a channel using by bot  
Replace **\<user>** by id from allowed users. Can add many users `('<user_1_ID>', '<user_2_ID>')`  

### Hook Config  
```
WEBHOOK_CONF = {
    'webhook_url' : '<webhook_url>',
}
```
Replace **\<webhook_url>** by webhook url  

### 7dtd Config  
```
SDTD_CONF = {
    'server_ip' : '<@IP or hostname>',
}
```
Replace **\<@IP or hostname>** by 7dtd server public IP addresse or hostname (Ex: **8.8.8.8** or **sdtd.domain.tld**)  
