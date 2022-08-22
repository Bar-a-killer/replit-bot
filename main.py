import discord
import json, asyncio, datetime
import keep_alive
from discord import channel
from discord.ext import commands
import pymongo
import dns
import time
import asyncio
import datetime
from datetime import timedelta
from random import randint
import random

a1233321 = 'mongodb+srv://bar-king:32tmmcwkp@bar.52hjm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = pymongo.MongoClient(a1233321)
bot = commands.Bot(command_prefix='')

RED = client['bot']['red']
BLUE = client['bot']['blue']


#-----------------------成員加入-------------------------#
@bot.event  #out
async def on_member_join(member):
    print(f'{member}join')
    channel = bot.get_channel(855032575575851041)
    await channel.send(f'{member}一起墮入狂賭的深淵吧!')


@bot.event  #in
async def on_member_leave(member):
    print(f'{member}leave')
    channel = bot.get_channel(855032575575851041)
    await channel.send(f'{member}我們懷念他')


#----------------------成員退出---------------------------#


#----------------------上線及執行--------------------------#
@bot.event
async def on_ready():
    print("一起墮入狂賭的深淵吧!")

    game = discord.Game('Bar')
    await bot.change_presence(status=discord.Status.idle, activity=game)

    channel = bot.get_guild(855032575575851038).get_channel(862693719807623188)
    todebug = 0
    tdebug = 0
    #---------------------接下去-----------------------#
    #members = RED.find_one({'id': 'data'})['member']
    #for i in range(len(members)): 
      #if RED.find_one({'_id': members[i+1]})['money']<0:
        
        #RED.update_one({'_id':members[i+1]},{'$set':{'money':0}})
        #RED.update_one({'_id':members[i+1]},{'$set':{'rob':0}})
        #RED.update_one({'_id':members[i+1]},{'$set':{'rober':['沒','有人']}})
        #RED.update_one({'_id':members[i+1]},{'$set':{'lock':0}})

#---------------------被洗劫了!!-----------------------#
    while True:
        await asyncio.sleep(60)
        if datetime.datetime.now().minute == 1:
          memb=RED.find_one({'id':'data'})['member']
          for i in range(len(memb)):
            if RED.find_one({'_id':memb[i]})['hometime'] == 12:
              a=RED.find_one({'_id':memb[i]})['money']//2
              if a<0:
                a=0
              RED.update_one({'_id':memb[i]},{'$inc':{'money':-a}})
              b=RED.find_one({'_id':memb[i]})['rober']
              name=RED.find_one({'_id':memb[i]})['name']
              #if type(b) is list:
              b=b[-1]
              RED.update_one({'_id':b},{'$inc':{'money':a}})
              RED.update_one({'name':b},{'$set':{'rob':0}})
              RED.update_one({'_id':memb[i]},{'$set':{'hometime':0}})
              for k in range(2):
                if k == 0:
                    channel = bot.get_guild(
                        855032575575851038).get_channel(862995250611486740)
                if k == 1:
                    channel = bot.get_guild(
                        915511946680348682).get_channel(944597342420619364)

                await channel.send(f"{name}被{b}洗劫了! 趕快去復仇吧!")
            
            elif RED.find_one({'_id':memb[i]})['hometime'] != 0:
              RED.update_one({'_id':memb[i]},{'$inc':{'hometime':1}})
#---------------------被洗劫了!!-----------------------#
#---------------------報盤啦---------------------------#              
        if datetime.datetime.now().hour == 23 or datetime.datetime.now(
        ).hour == 11:
            if todebug == 0:
                print(datetime.datetime.now().hour)
                a = RED.find_one({'id': "data"})['red']
                b = RED.find_one({'id': "data"})['blue']
                for i in range(2):
                    if i == 0:
                        channel = bot.get_guild(
                            855032575575851038).get_channel(862995250611486740)
                    if i == 1:
                        channel = bot.get_guild(
                            915511946680348682).get_channel(944597342420619364)

                    await channel.send(f"報盤啦!\n現在的資料是:\nA:{a} B:{b}")
                todebug = 1
#---------------------報盤結束----------------------#
#---------------------發錢-------------------------#


        elif datetime.datetime.now().hour == 12 or datetime.datetime.now(
        ).hour == 0:
            if tdebug == 0:
                a = RED.find_one({'id': "data"})['red']
                b = RED.find_one({'id': "data"})['blue']
                members = RED.find_one({'id': 'data'})['member']
              
                RED.update_one({'name': 'systeem'}, {'$inc': {'money': a + b}})
                put = givemoney(a, b, members[0], 0, 0)

                for i in range(len(members) - 1):
                    num = RED.find_one({'_id': members[i + 1]})['num']
                    num2 = BLUE.find_one({'_id': members[i + 1]})['num']
                    givemoney(a, b, members[i + 1], num, num2)
                todebug = 1
              
                for i in range(2):
                    if i == 0:
                        channel = bot.get_guild(
                            855032575575851038).get_channel(862995250611486740)
                    if i == 1:
                        channel = bot.get_guild(
                            915511946680348682).get_channel(944597342420619364)
                    await channel.send(
                        f'下{put}者得勝!\n獎金已經發下去了，請查收\n最終的資料是:\nA:{a}B:{b}')
                #random  
                seted=random.randrange(0, 2)
                stmun=len(RED.find_one({'id':'data'})['member'])*50
                RED.update_one({'id': 'data'}, {'$set': {'red': 0}})
                RED.update_one({'id': 'data'}, {'$set': {'blue': 0}})
                if seted==0:
                  RED.update_one({'id': 'data'}, {'$set': {'blue': stmun}})
                else:
                  RED.update_one({'id': 'data'}, {'$set': {'red': stmun}})
                  
                tdebug = 1
        else:
            todebug = 0
            tdebug = 0
#---------------------發錢-------------------------#

#-----------------------反利函式---------------------#
def givemoney(a, b, member, num, num2):

    if a < b:
        y = a
        x = b
        put = 'A'
    elif b < a:
        x = a
        y = b
        put = 'B'
        num = num2
    else:
        timenow = time.localtime(time.time())
        if timenow.tm_sec % 2 == 1:
            y = a
            x = b
            put = 'A'
        else:
            x = a
            y = b
            put = 'B'
            num = num2
    if y==0:
      y=1

    out = (y + x) // y * num * 9
    print(out, put, num, x, y, member)
    RED.update_one({'_id': member}, {"$inc": {'money': out}})
    BLUE.update_one({'_id': member}, {"$set": {'num': 0}})
    RED.update_one({'_id': member}, {"$set": {'num': 0}})
    return put


#-----------------------反利函式結束-------------------#


@bot.event
async def on_message(message):

    if message.content.startswith("購買項目") or message.content == "領取番茄幣":
        
#-------------------------開戶-----------------------------#
        if RED.count_documents({"_id": message.author.id}) == 0:
            await message.channel.send('等等...我先幫你開個戶...')
            timenow = time.localtime(time.time())
            BLUE.insert_one({
                '_id': message.author.id,
                'name': message.author.name,
                'num': 0
            })

            RED.insert_one({
                '_id': message.author.id,
                'name': message.author.name,
                'num': 0,
                'money': 0,
                'lastday': timenow.tm_mday - 1,
                'hometime':0,
                'rob':0,
                'rober':['-','-'],
            })
            if message.author.nick==None:
              RED.update_one({"_id":message.author.id},{'$set':{'name':message.author.name}})
            else:
              RED.update_one({"_id":message.author.id},{'$set':{'name':message.author.nick}})
            #members=RED.find_one({'id':'data'})['member']
            ids = message.author.id
            #members=members.append(ids)
            RED.update_one({'id': 'data'}, {'$push': {'member': ids}})
            await message.channel.send('開戶完成 盡情狂賭吧!(請再操作一次)')
#-------------------------開戶結束--------------------------#
        
        if RED.find_one({"_id":message.author.id})['name']==None:
          if message.author.nick==None:
            RED.update_one({"_id":message.author.id},{'$set':{'name':message.author.name}})
          else:
            RED.update_one({"_id":message.author.id},{'$set':{'name':message.author.nick}})
          await message.channel.send('很抱歉，由於系統出了些問題，需要您重新輸入')

#-------------------------領取籌碼--------------------------#
        else:
            if message.content == "領取番茄幣":
                timenow = time.localtime(time.time())
                if timenow.tm_mday != RED.find_one({'_id': message.author.id})['lastday']:
                    RED.update_one({'_id': message.author.id},
                                   {'$inc': {'money': 100}})
                    RED.update_one({"_id": message.author.id},
                                   {"$set": {'lastday': timenow.tm_mday}})
                    await message.channel.send('錢已經給你打過去了(100)')
                elif timenow.tm_mday == RED.find_one({'_id': message.author.id})['lastday'] and timenow.tm_hour >= 16:
                    RED.update_one({'_id': message.author.id},
                                  {'$inc': {'money': 100}})
                    RED.update_one({"_id": message.author.id},
                                  {"$set": {'lastday': timenow.tm_mday+1}})
                    await message.channel.send('錢已經給你打過去了(100)')

                else:
                    await message.channel.send("今天的錢已經領完了喔")
#------------------------領取籌碼結束------------------------#

#------------------------指令錯誤----------------------------#
            else:

                tmp = message.content.split(" ")
                if len(tmp) == 1:
                    await message.channel.send(
                        f"{message.author.mention} 告訴我~你想要什麼~")
                elif len(tmp) == 2:
                    if tmp[1] == 'A' or tmp[1] == 'B':
                        await message.channel.send(
                            f"{message.author.mention} 說吧 你要下多少")
                    else:
                        await message.channel.send('查無此項目')
#----------------------指令沒錯-------------------------------#

#----------------------下注開始-------------------------------#
                elif len(tmp) == 3:
                    tmp[2] = int(tmp[2])
                    tmps=tmp[2]
                    if (datetime.datetime.now().hour <= 23 and datetime.datetime.now().hour >= 24) or (datetime.datetime.now().hour <= 11 and datetime.datetime.now().hour >= 12):
                      tmps=tmp[2]*2
                    if tmp[2] * 10 <= int(RED.find_one({'_id': message.author.id})['money']) and (0 <= tmp[2] * 10):
                        if tmp[1] == 'A':
                            RED.update_one({"_id": message.author.id},
                                           {"$inc": {
                                               'num': tmps
                                           }})
                            RED.update_one({"_id": message.author.id},
                                           {"$inc": {
                                               'money': -(10 * tmp[2])
                                           }})
                            RED.update_one({"id": "data"},
                                           {"$inc": {
                                               'red': tmps
                                           }})
                            await message.channel.send(
                                f"{message.author.mention} 下注完成 祝好運")

                        elif tmp[1] == 'B':
                            BLUE.update_one({"_id": message.author.id},
                                            {"$inc": {
                                                'num': tmps
                                            }})
                            RED.update_one({"_id": message.author.id},
                                           {"$inc": {
                                               'money': -(10 * tmp[2])
                                           }})
                            RED.update_one({"id": "data"},
                                           {"$inc": {
                                               'blue': tmps
                                           }})
                            await message.channel.send(
                                f"{message.author.mention} 下注完成 祝好運")

                        else:
                            await message.channel.send("沒這玩意")
                    elif tmp[2] < 0:
                        await message.channel.send("沒用的，可可試過，而且成功了、所以這個BUG就沒了")
                    else:
                        await message.channel.send("錢錢不夠喔")

                else:
                    await message.channel.send("滾")
#----------------------下注結束-------------------------------#
#-----------------------買鎖---------------------------------#
    if message.content.startswith("$購買"):
      spoke=message.content.split(' ')
      spoke[2]=int(spoke[2])
      if spoke[1]=='鎖':
        
        if spoke[2]*100<RED.find_one({'_id':message.author.id})['money']:
          RED.update_one({'_id':message.author.id},{'$inc':{'money':-spoke[2]*1000}})
          RED.update_one({'_id':message.author.id},{'$inc':{'lock':spoke[2]}})
          
          await message.channel.send("購買成功")
        else:
          await message.channel.send("指令錯誤")  

#-----------------------買鎖---------------------------------#
                  
#------------------------回家--------------------------------#
    if message.content=='$回家':
      
      robr=RED.find_one({'_id':message.author.id})['rober']
      print(robr)
      print(len(robr))
      if RED.find_one({'_id':message.author.id})['hometime']==0:
        await message.channel.send('你家很安全')
      else:  
        await message.channel.send("你的家曾被")
        for i in range(len(robr)):
          if robr[i]!=robr[i-1] and robr[i]!=robr[i-2]:
            await message.channel.send(robr[i])
        await message.channel.send('入侵過，請小心安全')
        RED.update_one({"_id": message.author.id},{"$set": {'rober': ['-','-']}})
        #抓賊
        if RED.find_one({'_id':message.author.id})['hometime']!=0:
          await message.channel.send(f'抓到竊賊{robr[-1]}，開始擲骰子決定處置方式')
          RED.update_one({'name':robr[-1]},{'$set':{'rob':0}})
          dice=randint(1,6)          
          await asyncio.sleep(1)
          await message.channel.send(f'骰到{dice}，處置方式為')
          money=RED.find_one({'_id':message.author.id})['money']
          rbid=RED.find_one({'name':robr[-1]})['_id']
          RED.update_one({"_id": message.author.id},{"$set": {'rober': ['-','-']}})
          #bemoney=RED.find({'_id':rbid})['money']
          #處置1
          if dice==1:     
            cg= money//4

            RED.update_one({"_id": message.author.id},{"$inc": {'money': -cg}})
            RED.update_one({"_id": rbid},{"$inc": {'money': cg}})
            await message.channel.send('超級仁慈的分了四分之一的財產給了竊賊')
          #處置234
          elif dice==2 or dice==3 or dice==4:
            await message.channel.send('仁慈的放過竊賊')
          #處置56
          else:
            cg= money//4
            if cg<0:
              cg=1
            RED.update_one({"_id": message.author.id},{"$inc": {'money': cg}})
            RED.update_one({"_id": rbid},{"$inc": {'money': -cg}})
            await message.channel.send('從竊賊手裡A走了自己手裡的錢，並要求償還被企圖奪取的財產的二分之一')
            if cg==0:
              await message.channel.send('但竊賊超窮，所以你放過了他')
            if cg==1:
              await message.channel.send('但竊賊超窮，所以系統給你1元安慰你')
          
          RED.update_one({"_id": message.author.id},{"$set": {'hometime': 0}})
#------------------------回家--------------------------------#

#------------------------搶劫--------------------------------#          
    if message.content.startswith("偷盜"):
      if RED.find_one({'_id':message.author.id})['rob']!=1:
        tmp = message.content.split(" ")
        if len(tmp)==1:
            await message.channel.send('月黑風高，但你睡著了')
        if len(tmp)==2:
            edid=RED.find_one({'name':tmp[1]})['_id']
            edid=int(edid)
            print(edid)
               
            if RED.find_one({"_id":message.author.id})["name"]==tmp[1]:
                await message.channel.send('月黑風高，門很快地開了\n')
                await asyncio.sleep(1)
                await message.channel.send('你回家了') 
            #elif type(edid) is not int:
            #    await message.channel.send('月黑風高，但找不到目標門牌')
            else:
              if RED.find_one({'_id':edid})['hometime']  ==  0:
                det=0
                locks=RED.find_one({'_id':edid})['lock']
                await message.channel.send(f'月黑風高，你走到了{tmp[1]}的門前，門上有{locks}個鎖，你正在試圖不觸發警報的解鎖')
                await asyncio.sleep(2)
                if RED.find_one({'_id':edid})['lock']>0:
                  for j in range(locks):
                      if randint(1,10)<3:
                            await message.channel.send(f'第{j+1}個鎖開了')
                            await asyncio.sleep(1)
                            await message.channel.send('.....')
                            RED.update_one({'_id':edid},{'$inc':{'lock':-1}})
  
                            await asyncio.sleep(1)
                      else:
                            await message.channel.send('啊喔～破門失敗了...')
                            await asyncio.sleep(1)
                            roberts=RED.find_one({'_id':edid})['rober']
                            roberts.append(RED.find_one({'_id':message.author.id})['name'])           
                            RED.update_one({'_id':edid},{'$set':{'rober':roberts}})
                            det=1
                            break
                if det==0:
                  RED.update_one({'_id':edid},{'$set':{'hometime':1}})
                  
                  roberts=RED.find_one({'_id':edid})['rober']
                  #print(roberts)
                  n=RED.find_one({'_id':message.author.id})['name']
                  #print(n)
                  roberts.append(n)
                  #print(roberts)
                  
                  RED.update_one({'_id':edid},{'$set':{'rober':roberts}})
                  await message.channel.send('破門成功...開始翻找錢錢\n祈禱屋主12hr內不會回來吧!')
                  RED.update_one({'_id':message.author.id},{'$set':{'rob':1}})
              else:
                edrob=RED.find_one({'_id':edid})['rober']
                await message.channel.send(f'你尷尬地與{edrob[-1]}互看了一眼並慢慢地退出大門')
      else:
        await message.channel.send(f'{message.author.mention}你正在偷竊別人中')
#------------------------搶劫--------------------------------#
            
#----------------------測試指令-------------------------------#

    if message.content == '夢子是雜貓':  #經典
        await message.channel.send('喵~')

    elif message.content == '智乃寶貝':  #智乃保護協會
        await message.channel.send('我代表FBI將你逮捕')

    elif message.content == '$rull':  #規則
        await message.channel.send(
            "賭博規則：\n1、買入項目後(每分項目為10番茄幣，開盤之前買1送1)，系統將會抽取10%的番茄幣作為運轉資金\n    （購買1項目將只有9番茄幣位計入系統）。\n2、每日7：00將公布當下各項目總金額。\n3、開獎後，總金額最低之項目會吸收其他項目的金額並按購入比例分配給購買者。\n4、8:00開獎\n5、每日可輸入[領取番茄幣]領取100番茄幣\n6、輸入[$背包]來查看背包\n  7、輸入[$番茄排行]來查詢目前的前五名、輸入[番茄排行]目前可選項目：\n  項目A 項目B\n  輸入：\n  [購買項目] 項目 購買數\n  如：\n  購買項目 A 1\n偷盜規則:\n1、輸入[偷盜] 被害人名稱\n  如:\n  偷盜 someone\n即可開始破門\n2、若破門成功並屋主沒有在12hr內回家則可以獲得屋主四分之一的財產\n3、如果想要加固家裡可以輸入 [$購買 鎖] 數量\n  如:\n  $購買 鎖 1\n花費1000番茄幣可購賣一個鎖，不過效果頗低\n4、如果你覺得被偷了，可以輸入[$回家]來確認或抓小偷\n5、若是抓到小偷，系統會擲骰子決定處置方式\n6、輸入 [$贈與] 名稱 數量\n 如:\n $贈與 Bar 100\n可以送別人錢")

    elif message.content == '$ping':  #虐待
        pingbot = bot.latency
        await message.channel.send(pingbot)
        if (pingbot > 0.3):
            await message.channel.send("你虐待了夢子，但夢子覺得很爽")

        else:
            await message.channel.send("你好好的對待夢子，但夢子覺得你很無趣")
#----------------------測試結束-------------------------------#

    elif message.content.startswith("$贈與"): 
      tmp=message.content.split(' ')
      tmp[2]=int(tmp[2])
      if tmp[2]>0:
        RED.update_one({'_id':message.author.id},{'$inc':{'money':-tmp[2]}})
        RED.update_one({'name':tmp[1]},{'$inc':{'money':tmp[2]}})
        await message.channel.send("交易成功")
      else:
        await message.channel.send("沒用Ouo")

        

          
#----------------------排行榜---------------------------------#
    elif message.content == '$背包':  #背包
        await message.channel.send(
            f"{message.author.mention}的背包\n-----------\n番茄幣:{RED.find_one({'_id':message.author.id})['money']}\nA:{RED.find_one({'_id':message.author.id})['num']}\nB:{BLUE.find_one({'_id':message.author.id})['num']}\n鎖:{RED.find_one({'_id':message.author.id})['lock']}\n-----------"
        )

    elif message.content == '$番茄排行':
        memberlist = RED.find_one({'id': 'data'})['member']
        alldict = {}
        for i in range(len(memberlist)):
            money = RED.find_one({'_id': memberlist[i]})['money']
            alldict.update({memberlist[i]: money})
        alllist = sorted(alldict.items(), key=lambda i: i[1], reverse=True)
        alllist_1 = [0, 0, 0, 0, 0]
        for i in range(5):
            alllist_1[i] = RED.find_one({'_id': alllist[i][0]})['name']

        await message.channel.send(f'----------------------\n1st.\n{alllist_1[0]}: {alllist[0][1]}\n2nd.\n{alllist_1[1]}: {alllist[1][1]}\n3rd.\n{alllist_1[2]}: {alllist[2][1]}\n4th.\n{alllist_1[3]}: {alllist[3][1]}\n5th.\n{alllist_1[4]}: {alllist[4][1]}\n----------------------')
#----------------------排行榜結束-----------------------------#

#------------------------供養-------------------------#
""" 
    if message.content == '$play':
        await message.channel.send('1=買番茄\n 2=打工\n 3=狩獵\n 4=探險 \n 5=回復\n 6=能力值 \n 7=加運氣\n 8=背包\n 送蕃茄=??????(自己猜)')

    if message.content == '1':
        await message.channel.send('-購買 番茄')
    elif message.content == '2':
        await message.channel.send('打工')
    if message.content == '3':
        await message.channel.send('-狩獵')
    if message.content == '4':
        await message.channel.send('-探險')
    if message.content == '5':
        await message.channel.send('-回復')
    if message.content == '6':
        await message.channel.send('-能力值')
    if message.content == '1206':
        await message.channel.send('-交易 ' f'{message.author.name}' ' 番茄 100')
        await message.delete()
    if message.content == '7':
        await message.channel.send('-技能點 運氣 2')
    if message.content == '8':
        await message.channel.send('-背包')
    if message.content == '9':
        await message.channel.send('-強化技能')
""" 
#-----------------------供養結束-------------------------#

keep_alive.keep_alive()
bot.run('ODc0NjI3ODUwODQ0NjYzODU5.YRJuqQ.blP6e6uqzYHvtd20zvOt17tjK9c')