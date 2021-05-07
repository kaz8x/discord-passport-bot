from PIL import Image, ImageFont, ImageDraw
import discord
import os
import json
from discord.ext import commands

#read data.json
f = open('data.json',)
data = json.load(f)
bot = commands.Bot(command_prefix = data["prefix"])
selected_font = data["font"]
TOKEN = data["token"]
genderlist = data["gender"]
f.close()

@bot.event
async def on_ready():
    print("Bot Is Ready And Online!")

@bot.command(name = "generatepassport", description = "Use to generate passport. Replace <arg> with male or female", pass_context = True)
async def generatepassport(ctx, arg):

    #variables
    gender = arg
    name = ctx.message.author.name + "#" + ctx.message.author.discriminator
    accid = str(ctx.message.author.id)
    creationdate = ctx.message.author.created_at
    age = creationdate.strftime("%m/%d/%Y, %H:%M:%S")

    if gender in genderlist:
        #getpfp
        await ctx.author.avatar_url.save("pfp.jpg")
    
        pfp_image = Image.open("pfp.jpg")

        pfp_image = pfp_image.resize((177, 177))
    
        passport_image = Image.open("passport.jpg")
        title_font = ImageFont.truetype(selected_font, 40)
        image_editable = ImageDraw.Draw(passport_image)

        #add text
        image_editable.text((605, 200), name, (0, 0, 0), font=title_font)
        image_editable.text((605, 310), age, (0, 0, 0), font=title_font)
        image_editable.text((605, 425 + 10), accid, (0, 0, 0), font=title_font)
        image_editable.text((605, 580 - 20), gender, (0, 0, 0), font=title_font)

    
        passport_image.paste(pfp_image, (628, 705))

        #add ruber stamp
        filename = 'stamp.png'
        ironman = Image.open(filename, 'r')
        ironman = ironman.resize((300, 300))
        ironman = ironman.rotate(-30)
        text_img = Image.new('RGBA', (1173, 927), (0, 0, 0, 0))
        text_img.paste(passport_image, (0,0))
        text_img.paste(ironman, (850,410), mask=ironman)
        text_img.save("result.png", format="png")

        await ctx.send(file=discord.File("result.png"), content = "Here's your passport")
    
        os.remove("pfp.jpg")
        os.remove("result.png")
    else:
        await ctx.send(content = "Thats not valid gender")

bot.run(TOKEN)
