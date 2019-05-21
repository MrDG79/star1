# -*- coding: utf-8 -*- 

#import sys
#import asyncio
import discord
#import datetime
#import random
import os
#from discord.ext import commands
#from gtts import gTTS

@client.event
async def on_ready:
	print ("login")
	print (client.user.name)
	print (client.user.id)
	print ("-----------------------")

@client.event
async def on_message(message):
	if message.content.startswith("hi"):
		await client.send_message(message.channel, "HI")

			
access_token = os.environ["BOT_TOKEN"]			
client.run(access_token)
