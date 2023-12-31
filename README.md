# Media-converter bot
 Telegram bot that allows user to convert any media files to any formats

[<img src="https://img.shields.io/badge/Telegram-%40converter__media__bot-blue">](https://t.me/converter_media_bot)
[![wakatime](https://wakatime.com/badge/user/4d0cc4aa-e1c1-483b-8c80-199c9ea5d0c5/project/45475bdb-2f59-4d7a-b6aa-c7372321c08f.svg)](https://wakatime.com/badge/user/4d0cc4aa-e1c1-483b-8c80-199c9ea5d0c5/project/45475bdb-2f59-4d7a-b6aa-c7372321c08f.svg)

![Aiogram](https://img.shields.io/badge/aiogram-14354C?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

 # Contents
 1. <a href="#install">Install</a>
  * <a href="#prequisites">Prequisites</a> 
  * <a href="#basic-startup">Basic startup</a>
  * <a href="#systemd">Systemd</a>
 2. <a href="#todo">TODO</a>

## Install

### Prequisites
1. Python 3.11 or higher

### Basic startup
If you have FFMPEG in your $PATH, then in FFMPEG_PATH put just 'ffmpeg'
Just fill .env and run this commands:
```bash
pip install -r requirements.txt
```
```bash
python main.py
```

### Systemd
Replace '.example' from converter-bot.service.example so it's just converter-bot.service. 
 Then just copy service file to /etc/systemd/system/ 
 ```bash 
 sudo systemctl start converter-bot.service 
 ```

## TODO
1. Convert GIF into video
2. Systemd .service file
