# 7dtd_discordBot
Simple Bot/Webhook for 7dtd Linux management scripts.  
Required 7dtd Linux management scripts availible on https://7dtd.illy.bz/  
Features:
  * Start/Stop 7dtd instances. ( Discord Bot )
  * Send message when instances' state changed. ( Discord WebHook )  

This wiki will guide you through the setup and usage of the tool set.  
[wiki](https://github.com/artnod78/KSP-DMP-Manager/wiki)
## Installation
```
wget https://raw.githubusercontent.com/artnod78/7dtd_discordBot/master/bootstrap/bootstrap.sh
chmod +x bootstrap.sh
./bootstrap.sh -i
```
## Configuration
Edit `/usr/local/bin/sdtdbot/discord_bot.py` with your settings:
```
bot_token = '<token>'
bot_channel = '<channel>'
bot_admin_list = ('<user>',)
```
Replace **\<token>** by bot token  
Replace **\<channel>** by a channel using by bot  
Replace **\<user>** by id from allowed users. Can add many users `('<user_1_ID>', '<user_2_ID>')`  
 
 
 Edit `/usr/local/bin/sdtdbot/discord_hook.py` with your settings:
```
webhook_url = '<webhook_url>'
webhook_server_ip = '<@IP or hostname>'
```
Replace **\<webhook_url>** by webhook url  
Replace **\<@IP or hostname>** by 7dtd server public IP addresse or hostname (Ex: **8.8.8.8** or **sdtd.domain.tld**)
