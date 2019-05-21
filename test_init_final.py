# -*- coding: utf-8 -*- 

import os
import sys
import asyncio
import discord
import datetime
import random
from discord.ext import commands
from gtts import gTTS
#from discord.ext.commands import Bot
#from discord.voice_client import VoiceClient

#if not discord.opus.is_loaded():
#	discord.opus.load_opus('opus')
'''
basicSetting = []
bossData = []

bossNum = 0
chkvoicechannel = 0
chkrelogin = 0
chflg = 0
LoadChk = 0

bossTime = []
tmp_bossTime = []

bossTimeString = []
bossDateString = []
tmp_bossTimeString = []
tmp_bossDateString = []

bossFlag = []
bossFlag0 = []
bossMungFlag = []
bossMungCnt = []

channel_info = []
channel_name = []
channel_id = []
channel_voice_name = []
channel_voice_id = []
channel_type = []
'''

client = discord.Client()

@client.event
async def on_ready():
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
