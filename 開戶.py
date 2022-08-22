import discord
import json, asyncio, datetime
import keep_alive
from discord import channel
from discord.ext import commands
import pymongo
import dns
import time

def 開戶():
  #-------------------------開戶-----------------------------#
  if RED.count_documents({"_id":message.author.id})==0: 
    await message.channel.send('等等...我先幫你開個戶...') 
    timenow=time.localtime(time.time())    
    BLUE.insert_one({'_id':message.author.id,
                      'name':message.author.mention,
                      'num':0})
    
    RED.insert_one({'_id':message.author.id,
                    'name':message.author.mention,
                    'num':0,'money':0,'lastday':timenow.tm_mday-1})
    await message.channel.send('開戶完成 盡情狂賭吧!(請再操作一次)')
#-------------------------開戶結束--------------------------#