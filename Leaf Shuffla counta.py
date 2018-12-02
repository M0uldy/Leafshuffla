import discord
from os import getenv
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
timefrom = 0

Client = discord.Client()
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot:Leaf Shuffla is ready!")

def __init__(self, bot):
    self.bot = bot
    
@client.event
async def on_message(message):
    global timefrom
    if message.content.startswith(".countdown"):
        timelength = message.content.split()[2]
        enteredtime = message.content.split()[1]
        enteredtime2 = int(enteredtime)
        if timelength == "m":
            if int(enteredtime) >= 31:
                await client.send_message(message.channel, "```SORRY, MAX TIME IS 30M```")
                timefrom = -2
            else:
                timefrom = int(enteredtime2 * 60)
                await client.send_message(message.channel, "```" + str(timefrom) + "```")
                time.sleep(1)
                
        elif timelength == "h":
            await client.send_message(message.channel, "```SORRY, THIS FUNCTION HAS BEEN DISCONTINUED```")
            timefrom = -2

        elif timelength == "s":
            timefrom = enteredtime
            await client.send_message(message.channel, "```" + str(timefrom) + "```")
            time.sleep(1)

        while int(timefrom) >= 1:
            timefrom = int(timefrom) - int(1)
            await client.send_message(message.channel, "```" + str(timefrom) + "```")
            time.sleep(1)


        if timefrom == 0:
            await client.send_message(message.channel, "```TIME UP```")

    elif message.content.startswith(".stop"):
        timefrom = -1
        await client.send_message(message.channel, "```STOPPED```")

    elif message.content.startswith(".die"):
        await client.send_message(message.channel, "```NO U```")
        
    elif message.content.startswith(".w"):
        await client.send_message(message.channel, "```MASOCHIST?```")

    elif message.content.startswith(".d"):
        define = "```If you call someone a masochist, you either mean that they take pleasure in pain, or — perhaps more commonly — that they just seem to.```"
        detail = "```Masochism is an eponym — a word named for a person. Leopold von Sacher-Masoch was an Austrian writer in the nineteenth century who described the gratification he got from his own pain and humiliation. There are many self-proclaimed masochists out there today — and, one would have to imagine, at least as many sadists, those who enjoy inflicting pain on others (from the name of the Marquis de Sade). But these days you're most likely to hear the word used jokingly by someone who doesn't understand another's motivations for doing something painful or difficult: 'You're still building that stone wall? What are you, some kind of masochist?```"
        await client.send_message(message.channel, define + detail)

    elif message.content.startswith(".mc"):
        await client.send_message(message.channel, "```WANNA PLAY MINECWAF?```")

    elif message.content.startswith(".ANSWERME!"):
        await client.send_message(message.channel, "```A```")
        time.sleep(1)
        await client.send_message(message.channel, "```B```")
        time.sleep(1)
        await client.send_message(message.channel, "```C```")
        time.sleep(1)
        await client.send_message(message.channel, "```D```")
        time.sleep(1)
        await client.send_message(message.channel, "```E```")
        time.sleep(1)
        await client.send_message(message.channel, "```F```")
        time.sleep(1)
        await client.send_message(message.channel, "```G```")
        time.sleep(1)
        await client.send_message(message.channel, "```H```")
        time.sleep(1)
        await client.send_message(message.channel, "```I```")
        time.sleep(1)
        await client.send_message(message.channel, "```J```")
        time.sleep(1)
        await client.send_message(message.channel, "```K```")
        time.sleep(1)
        await client.send_message(message.channel, "```L```")
        time.sleep(1)
        await client.send_message(message.channel, "```M```")
        time.sleep(1)
        await client.send_message(message.channel, "```N```")
        time.sleep(1)
        await client.send_message(message.channel, "```O```")
        time.sleep(1)
        await client.send_message(message.channel, "```P```")
        time.sleep(1)
        await client.send_message(message.channel, "```Q```")
        time.sleep(1)
        await client.send_message(message.channel, "```R```")
        time.sleep(1)
        await client.send_message(message.channel, "```S```")
        time.sleep(1)
        await client.send_message(message.channel, "```T```")
        time.sleep(1)
        await client.send_message(message.channel, "```U```")
        time.sleep(1)
        await client.send_message(message.channel, "```V```")
        time.sleep(1)
        await client.send_message(message.channel, "```W```")
        time.sleep(1)
        await client.send_message(message.channel, "```X```")
        time.sleep(1)
        await client.send_message(message.channel, "```Y```")
        time.sleep(1)
        await client.send_message(message.channel, "```Z```")
        time.sleep(1)
        await client.send_message(message.channel, "```NOW YOU KNOW YOUR ABC```")
        time.sleep(1)
        await client.send_message(message.channel, "```WILL YOU FUCKING ANSWER ME?!```")
client.run(getenv("token"))


