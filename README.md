# Passport bot
Passport bot is discord bot that can be used to generate images of fictional passports for discord users. This can be handy for those nation/history roleplay discord servers. It was originaly made for [Republic of Czechoslovakia](https://discord.gg/Rd4xz8RrCh) server. But i decided to upload it here. Maybe someone will find it usefull.
## Requirements
* Python (tested on Python 3.9.1)
* Discord.py
* Pillow
## Setup
1. Instal Pillow and discord.py using pip
1. Download font that you will be using in .ttf format and save it to fonts folder
1. Use template to create your passport image and save it as passport.jpg
1. Use template to create your stamp image and save it as stamp.png
1. Instead of templates you can use design from our discord server if you want
1. Open data.json and fill out your desired prefix, path to selected font ("fonts\fontname.ttf) and your token
1. Run bot.py
## Usage
Run "prefix"generatepassport and use letter to represent your gender as argument.
