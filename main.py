import discord
import random
from dotenv import load_dotenv
import os

load_dotenv()

bot_key = os.environ.get("DISCORD_DA_BABY_KEY")

client = discord.Client()

triggers = [
    "dababy", 
    "da baby", 
    "baby",
    ]

phrases = [
    "LET\'S GO!",
    "I needed some shit with some bop in it!",
    "Woo!", 
    "Yeah!",
    "I got me a milli', I did it legit-ly!",
    "You know it's Baby, hahaha",
    "You know it's Baby",
    "Go call my chauffeur, bitch, 'cause I don't like to drive!",
    "I'm on front row at BET without my Glock!",
    "Brand new Lamborghini, fuck a cop car!",
    "I flew past the whip with that blunt in my mouth!",
    "She wanna fuck with me, but I don't got the time!",
    "Mmh, mmh",
    "Oh Lord, Jetson made another one!",
    "I'm a young CEO!",
    "Ayy!",
    "I'm goin’ baby on baby!",
    "Told my bitch \"I love you\", that was just a typo",
    "I'M DABABY",
    "LETSSS GOOO!",
    "I'm YOUNG KIRK!",
    "It's DaBaby, what you heard about me?",
    "I'm in the rental truck sticked up like Walker Texas Ranger",
    "This ain't no guitar, bitch, this a Glock",
    "With the pistol on my hip like I'm a cop",
    "LESSSSS GOOOOO!!!!",
    "DA BABY LESSS GOOO!",
    "BABY ON BABY!",
    "https://gossiponthis.com/wp-content/uploads/2018/11/da-baby.jpg",
    "https://cache.umusic.com/_sites/officialdababy.com/images/OG.jpg",
    "https://images.complex.com/complex/images/c_fill,g_center,w_1200/fl_lossy,pg_1/yae9bzxqqtr05isuebm7/dababy-smile-getty",
    "https://guardian.ng/wp-content/uploads/2020/11/Da-Baby-1062x598.jpg",
    "https://secureservercdn.net/184.168.47.225/d0e.a1c.myftpupload.com/wp-content/uploads/2020/03/images-21.jpg?time=1583776204"
    ]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if (message.author == client.user) or (message.author.id == 159985870458322944):
        return

    for i in range(len(triggers)):
        if triggers[i] in message.content.lower():
            await message.channel.send(random.choice(phrases))
            return


client.run(bot_key)