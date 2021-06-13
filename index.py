import discord
import datetime
from discord.ext import commands, tasks
import asyncio
import multiprocessing
import requests
from urllib import request
from bs4 import BeautifulSoup
import threading
import time
import os
access_token = os.environ['BOT_TOKEN']
access_api = os.environ['GET_API']
access_list = os.environ['PLAYER_LIST']
token = access_token #토큰설정

client = discord.Client()
utcnow= datetime.datetime.utcnow()
time_gap= datetime.timedelta(hours=9)
level_kor_time= utcnow+ time_gap
i=0
len_player_lists = 0
first_load = 0

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game(name = "봇 실행")
    await client.change_presence(status=discord.Status.idle, activity=game)
    t1 = threading.Thread(target=loop)
    t1.start()
    loop2.start()

def star(num):
    if level_ranking_list[num][1] < 1100:
        return "✫"
    else:
        return "✪"


@client.event
async def on_message(message):
    global i
    try:
        guild_name = message.guild
    except:
        guild_name = None

    if ((guild_name != None or int(message.author.id) == 810709144915017748) and (message.author != client.user)):
        m = message.content
        m = m.replace(" ","")
        if (m =="/베워레벨" or m=="/배워레벨" or m=="/배워래벨" or m=="/배워레밸" or m=="/배워래밸" or m=="/베워래벨" or m=="/베워레밸" or \
            m=="/베워래밸" or m=="/ㅂㅇㄼ" or m=="/ㅂㅇㄹㅂ" or m=="/qdfq" or m=="/krbwlevel"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐋𝐞𝐯𝐞𝐥 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{level_ranking_list[0][0]}` - {int(level_ranking_list[0][1])}{star(0)}\n\
    :second_place: `{level_ranking_list[1][0]}` - {int(level_ranking_list[1][1])}{star(1)}\n\
    :third_place: `{level_ranking_list[2][0]}` - {int(level_ranking_list[2][1])}{star(2)}\n\
    :medal: `{level_ranking_list[3][0]}` - {int(level_ranking_list[3][1])}{star(3)}\n\
    :medal: `{level_ranking_list[4][0]}` - {int(level_ranking_list[4][1])}{star(4)}\n\
    𝟞. `{level_ranking_list[5][0]}` - {int(level_ranking_list[5][1])}{star(5)}\n\
    𝟟. `{level_ranking_list[6][0]}` - {int(level_ranking_list[6][1])}{star(6)}\n\
    𝟠. `{level_ranking_list[7][0]}` - {int(level_ranking_list[7][1])}{star(7)}\n\
    𝟡. `{level_ranking_list[8][0]}` - {int(level_ranking_list[8][1])}{star(8)}\n\
    𝟙𝟘. `{level_ranking_list[9][0]}` - {int(level_ranking_list[9][1])}{star(9)}\n\
    𝟏𝟏. `{level_ranking_list[10][0]}` - {int(level_ranking_list[10][1])}{star(10)}\n\
    𝟏𝟐. `{level_ranking_list[11][0]}` - {int(level_ranking_list[11][1])}{star(11)}\n\
    𝟏𝟑. `{level_ranking_list[12][0]}` - {int(level_ranking_list[12][1])}{star(12)}\n\
    𝟏𝟒. `{level_ranking_list[13][0]}` - {int(level_ranking_list[13][1])}{star(13)}\n\
    𝟏𝟓. `{level_ranking_list[14][0]}` - {int(level_ranking_list[14][1])}{star(14)}\n\
    𝟏𝟔. `{level_ranking_list[15][0]}` - {int(level_ranking_list[15][1])}{star(15)}\n\
    𝟏𝟕. `{level_ranking_list[16][0]}` - {int(level_ranking_list[16][1])}{star(16)}\n\
    𝟏𝟖. `{level_ranking_list[17][0]}` - {int(level_ranking_list[17][1])}{star(17)}\n\
    𝟏𝟗. `{level_ranking_list[18][0]}` - {int(level_ranking_list[18][1])}{star(18)}\n\
    𝟐𝟎. `{level_ranking_list[19][0]}` - {int(level_ranking_list[19][1])}{star(19)}\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")
                
    #0send
        elif (m=="/베워우승" or m=="/배워우승" or m=="/베워승리" or m=="/배워승리"or m=="/ㅂㅇㅇㅅ" or m=="/ㅂㅇㅅㄹ" or \
            m=="/베워우승0" or m=="/배워우승0" or m=="/베워승리0" or m=="/배워승리0"or m=="/ㅂㅇㅇㅅ0" or m=="/ㅂㅇㅅㄹ0" or \
                m=="/베워우승전체" or m=="/배워우승전체" or m=="/베워승리전체" or m=="/배워승리전체"or m=="/ㅂㅇㅇㅅㅈㅊ" or m=="/ㅂㅇㅅㄹㅈㅊ" or \
                    m=="/qddt" or m=="/qdtf" or m=="/qddt0" or m=="/qdtf0" or m=="/krbwwins"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{wins_ranking_list[0][0]}` - {wins_ranking_list[0][1]}:trophy:\n\
    :second_place: `{wins_ranking_list[1][0]}` - {wins_ranking_list[1][1]}:trophy:\n\
    :third_place: `{wins_ranking_list[2][0]}` - {wins_ranking_list[2][1]}:trophy:\n\
    :medal: `{wins_ranking_list[3][0]}` - {wins_ranking_list[3][1]}:trophy:\n\
    :medal: `{wins_ranking_list[4][0]}` - {wins_ranking_list[4][1]}:trophy:\n\
    𝟞. `{wins_ranking_list[5][0]}` - {wins_ranking_list[5][1]}:trophy:\n\
    𝟟. `{wins_ranking_list[6][0]}` - {wins_ranking_list[6][1]}:trophy:\n\
    𝟠. `{wins_ranking_list[7][0]}` - {wins_ranking_list[7][1]}:trophy:\n\
    𝟡. `{wins_ranking_list[8][0]}` - {wins_ranking_list[8][1]}:trophy:\n\
    𝟙𝟘. `{wins_ranking_list[9][0]}` - {wins_ranking_list[9][1]}:trophy:\n\
    𝟏𝟏. `{wins_ranking_list[10][0]}` - {wins_ranking_list[10][1]}:trophy:\n\
    𝟏𝟐. `{wins_ranking_list[11][0]}` - {wins_ranking_list[11][1]}:trophy:\n\
    𝟏𝟑. `{wins_ranking_list[12][0]}` - {wins_ranking_list[12][1]}:trophy:\n\
    𝟏𝟒. `{wins_ranking_list[13][0]}` - {wins_ranking_list[13][1]}:trophy:\n\
    𝟏𝟓. `{wins_ranking_list[14][0]}` - {wins_ranking_list[14][1]}:trophy:\n\
    𝟏𝟔. `{wins_ranking_list[15][0]}` - {wins_ranking_list[15][1]}:trophy:\n\
    𝟏𝟕. `{wins_ranking_list[16][0]}` - {wins_ranking_list[16][1]}:trophy:\n\
    𝟏𝟖. `{wins_ranking_list[17][0]}` - {wins_ranking_list[17][1]}:trophy:\n\
    𝟏𝟗. `{wins_ranking_list[18][0]}` - {wins_ranking_list[18][1]}:trophy:\n\
    𝟐𝟎. `{wins_ranking_list[19][0]}` - {wins_ranking_list[19][1]}:trophy:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워파킬" or m=="/배워파킬" or m=="/베워파이널킬" or m=="/배워파이널킬" or\
            m=="/배워파이널" or m=="/베워파이널" or m=="/ㅂㅇㅍㅋ" or m=="/ㅂㅇㅍㅇㄴㅋ" or m=="/ㅂㅇㅍㅇㄴ" or \
                m=="/베워파킬0" or m=="/배워파킬0" or m=="/베워파이널킬0" or m=="/배워파이널킬0" or\
            m=="/배워파이널0" or m=="/베워파이널0" or m=="/ㅂㅇㅍㅋ0" or m=="/ㅂㅇㅍㅇㄴㅋ0" or m=="/ㅂㅇㅍㅇㄴ0" or \
                m=="/베워파킬전체" or m=="/배워파킬전체" or m=="/베워파이널킬전체" or m=="/배워파이널킬전체" or\
            m=="/배워파이널전체" or m=="/베워파이널전체" or m=="/ㅂㅇㅍㅋㅈㅊ" or m=="/ㅂㅇㅍㅇㄴㅋㅈㅊ" or m=="/ㅂㅇㅍㅇㄴㅈㅊ" or \
                m=="/qdvz" or m=="/qdvdsz" or m=="/qdvz0" or m=="/qdvdsz0" or m=="/krbwfinalkills"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{finalkills_ranking_list[0][0]}` - {finalkills_ranking_list[0][1]}:bow_and_arrow:\n\
    :second_place: `{finalkills_ranking_list[1][0]}` - {finalkills_ranking_list[1][1]}:bow_and_arrow:\n\
    :third_place: `{finalkills_ranking_list[2][0]}` - {finalkills_ranking_list[2][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_list[3][0]}` - {finalkills_ranking_list[3][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_list[4][0]}` - {finalkills_ranking_list[4][1]}:bow_and_arrow:\n\
    𝟞. `{finalkills_ranking_list[5][0]}` - {finalkills_ranking_list[5][1]}:bow_and_arrow:\n\
    𝟟. `{finalkills_ranking_list[6][0]}` - {finalkills_ranking_list[6][1]}:bow_and_arrow:\n\
    𝟠. `{finalkills_ranking_list[7][0]}` - {finalkills_ranking_list[7][1]}:bow_and_arrow:\n\
    𝟡. `{finalkills_ranking_list[8][0]}` - {finalkills_ranking_list[8][1]}:bow_and_arrow:\n\
    𝟙𝟘. `{finalkills_ranking_list[9][0]}` - {finalkills_ranking_list[9][1]}:bow_and_arrow:\n\
    𝟏𝟏. `{finalkills_ranking_list[10][0]}` - {finalkills_ranking_list[10][1]}:bow_and_arrow:\n\
    𝟏𝟐. `{finalkills_ranking_list[11][0]}` - {finalkills_ranking_list[11][1]}:bow_and_arrow:\n\
    𝟏𝟑. `{finalkills_ranking_list[12][0]}` - {finalkills_ranking_list[12][1]}:bow_and_arrow:\n\
    𝟏𝟒. `{finalkills_ranking_list[13][0]}` - {finalkills_ranking_list[13][1]}:bow_and_arrow:\n\
    𝟏𝟓. `{finalkills_ranking_list[14][0]}` - {finalkills_ranking_list[14][1]}:bow_and_arrow:\n\
    𝟏𝟔. `{finalkills_ranking_list[15][0]}` - {finalkills_ranking_list[15][1]}:bow_and_arrow:\n\
    𝟏𝟕. `{finalkills_ranking_list[16][0]}` - {finalkills_ranking_list[16][1]}:bow_and_arrow:\n\
    𝟏𝟖. `{finalkills_ranking_list[17][0]}` - {finalkills_ranking_list[17][1]}:bow_and_arrow:\n\
    𝟏𝟗. `{finalkills_ranking_list[18][0]}` - {finalkills_ranking_list[18][1]}:bow_and_arrow:\n\
    𝟐𝟎. `{finalkills_ranking_list[19][0]}` - {finalkills_ranking_list[19][1]}:bow_and_arrow:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워침대" or m=="/배워침대" or m=="/베워베드" or m=="/배워배드" or m=="/베워침대파괴" or m=="/배워침대파괴" or m=="/베워배드" or \
            m=="/배워베드" or m=="/ㅂㅇㅊㄷ" or m=="/ㅂㅇㅂㄷ" or \
                m=="/베워침대0" or m=="/배워침대0" or m=="/베워베드0" or m=="/배워배드0" or m=="/베워침대파괴0" or m=="/배워침대파괴0" or m=="/베워배드0" or \
            m=="/배워베드0" or m=="/ㅂㅇㅊㄷ0" or m=="/ㅂㅇㅂㄷ0" or \
                m=="/베워침대전체" or m=="/배워침대전체" or m=="/베워베드전체" or m=="/배워배드전체" or m=="/베워침대파괴전체" or m=="/배워침대파괴전체" or m=="/베워배드전체" or \
            m=="/배워베드전체" or m=="/ㅂㅇㅊㄷㅈㅊ" or m=="/ㅂㅇㅂㄷㅈㅊ" or m=="/qdce" or m=="/qdce0" or m=="/qdqe0" or m=="/qdqe" or m=="/krbwbedsbroken"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{bedsbroken_ranking_list[0][0]}` - {bedsbroken_ranking_list[0][1]}:hammer:\n\
    :second_place: `{bedsbroken_ranking_list[1][0]}` - {bedsbroken_ranking_list[1][1]}:hammer:\n\
    :third_place: `{bedsbroken_ranking_list[2][0]}` - {bedsbroken_ranking_list[2][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_list[3][0]}` - {bedsbroken_ranking_list[3][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_list[4][0]}` - {bedsbroken_ranking_list[4][1]}:hammer:\n\
    𝟞. `{bedsbroken_ranking_list[5][0]}` - {bedsbroken_ranking_list[5][1]}:hammer:\n\
    𝟟. `{bedsbroken_ranking_list[6][0]}` - {bedsbroken_ranking_list[6][1]}:hammer:\n\
    𝟠. `{bedsbroken_ranking_list[7][0]}` - {bedsbroken_ranking_list[7][1]}:hammer:\n\
    𝟡. `{bedsbroken_ranking_list[8][0]}` - {bedsbroken_ranking_list[8][1]}:hammer:\n\
    𝟙𝟘. `{bedsbroken_ranking_list[9][0]}` - {bedsbroken_ranking_list[9][1]}:hammer:\n\
    𝟏𝟏. `{bedsbroken_ranking_list[10][0]}` - {bedsbroken_ranking_list[10][1]}:hammer:\n\
    𝟏𝟐. `{bedsbroken_ranking_list[11][0]}` - {bedsbroken_ranking_list[11][1]}:hammer:\n\
    𝟏𝟑. `{bedsbroken_ranking_list[12][0]}` - {bedsbroken_ranking_list[12][1]}:hammer:\n\
    𝟏𝟒. `{bedsbroken_ranking_list[13][0]}` - {bedsbroken_ranking_list[13][1]}:hammer:\n\
    𝟏𝟓. `{bedsbroken_ranking_list[14][0]}` - {bedsbroken_ranking_list[14][1]}:hammer:\n\
    𝟏𝟔. `{bedsbroken_ranking_list[15][0]}` - {bedsbroken_ranking_list[15][1]}:hammer:\n\
    𝟏𝟕. `{bedsbroken_ranking_list[16][0]}` - {bedsbroken_ranking_list[16][1]}:hammer:\n\
    𝟏𝟖. `{bedsbroken_ranking_list[17][0]}` - {bedsbroken_ranking_list[17][1]}:hammer:\n\
    𝟏𝟗. `{bedsbroken_ranking_list[18][0]}` - {bedsbroken_ranking_list[18][1]}:hammer:\n\
    𝟐𝟎. `{bedsbroken_ranking_list[19][0]}` - {bedsbroken_ranking_list[19][1]}:hammer:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

    #===========================================================================================================================================
    #44send
        elif (m=="/베워우승44" or m=="/배워우승44" or m=="/베워승리44" or m=="/배워승리44"or m=="/ㅂㅇㅇㅅ44" or m=="/ㅂㅇㅅㄹ44" or\
        m=="/베워우승5" or m=="/배워우승5" or m=="/베워승리5" or m=="/배워승리5"or m=="/ㅂㅇㅇㅅ5" or m=="/ㅂㅇㅅㄹ5" or \
            m=="/베워우승4v4" or m=="/배워우승4v4" or m=="/베워승리4v4" or m=="/배워승리4v4"or m=="/ㅂㅇㅇㅅ4v4" or m=="/ㅂㅇㅅㄹ4v4" or\
                m=="/qddt44" or m=="/qddt5" or m=="/qdtf44" or m=="/qdtf5" or m=="/krbw4v4_wins"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟒𝐯𝟒 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{wins_ranking_44_list[0][0]}` - {wins_ranking_44_list[0][1]}:trophy:\n\
    :second_place: `{wins_ranking_44_list[1][0]}` - {wins_ranking_44_list[1][1]}:trophy:\n\
    :third_place: `{wins_ranking_44_list[2][0]}` - {wins_ranking_44_list[2][1]}:trophy:\n\
    :medal: `{wins_ranking_44_list[3][0]}` - {wins_ranking_44_list[3][1]}:trophy:\n\
    :medal: `{wins_ranking_44_list[4][0]}` - {wins_ranking_44_list[4][1]}:trophy:\n\
    𝟞. `{wins_ranking_44_list[5][0]}` - {wins_ranking_44_list[5][1]}:trophy:\n\
    𝟟. `{wins_ranking_44_list[6][0]}` - {wins_ranking_44_list[6][1]}:trophy:\n\
    𝟠. `{wins_ranking_44_list[7][0]}` - {wins_ranking_44_list[7][1]}:trophy:\n\
    𝟡. `{wins_ranking_44_list[8][0]}` - {wins_ranking_44_list[8][1]}:trophy:\n\
    𝟙𝟘. `{wins_ranking_44_list[9][0]}` - {wins_ranking_44_list[9][1]}:trophy:\n\
    𝟏𝟏. `{wins_ranking_44_list[10][0]}` - {wins_ranking_44_list[10][1]}:trophy:\n\
    𝟏𝟐. `{wins_ranking_44_list[11][0]}` - {wins_ranking_44_list[11][1]}:trophy:\n\
    𝟏𝟑. `{wins_ranking_44_list[12][0]}` - {wins_ranking_44_list[12][1]}:trophy:\n\
    𝟏𝟒. `{wins_ranking_44_list[13][0]}` - {wins_ranking_44_list[13][1]}:trophy:\n\
    𝟏𝟓. `{wins_ranking_44_list[14][0]}` - {wins_ranking_44_list[14][1]}:trophy:\n\
    𝟏𝟔. `{wins_ranking_44_list[15][0]}` - {wins_ranking_44_list[15][1]}:trophy:\n\
    𝟏𝟕. `{wins_ranking_44_list[16][0]}` - {wins_ranking_44_list[16][1]}:trophy:\n\
    𝟏𝟖. `{wins_ranking_44_list[17][0]}` - {wins_ranking_44_list[17][1]}:trophy:\n\
    𝟏𝟗. `{wins_ranking_44_list[18][0]}` - {wins_ranking_44_list[18][1]}:trophy:\n\
    𝟐𝟎. `{wins_ranking_44_list[19][0]}` - {wins_ranking_44_list[19][1]}:trophy:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워파킬44" or m=="/배워파킬44" or m=="/베워파이널킬44" or m=="/배워파이널킬44" or\
            m=="/배워파이널44" or m=="/베워파이널44" or m=="/ㅂㅇㅍㅋ44" or m=="/ㅂㅇㅍㅇㄴㅋ44" or m=="/ㅂㅇㅍㅇㄴ44" or \
                m=="/베워파킬5" or m=="/배워파킬5" or m=="/베워파이널킬5" or m=="/배워파이널킬5" or\
            m=="/배워파이널5" or m=="/베워파이널5" or m=="/ㅂㅇㅍㅋ5" or m=="/ㅂㅇㅍㅇㄴㅋ5" or m=="/ㅂㅇㅍㅇㄴ5" or \
                m=="/베워파킬4v4" or m=="/배워파킬4v4" or m=="/베워파이널킬4v4" or m=="/배워파이널킬4v4" or\
            m=="/배워파이널4v4" or m=="/베워파이널4v4" or m=="/ㅂㅇㅍㅋ4v4" or m=="/ㅂㅇㅍㅇㄴㅋ4v4" or m=="/ㅂㅇㅍㅇㄴ4v4" or\
                m=="/qdvz44" or m=="/qdvz5" or m=="/qdvdsz44" or m=="/qdvdsz5" or m=="/krbw4v4_finalkills"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟒𝐯𝟒 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{finalkills_ranking_44_list[0][0]}` - {finalkills_ranking_44_list[0][1]}:bow_and_arrow:\n\
    :second_place: `{finalkills_ranking_44_list[1][0]}` - {finalkills_ranking_44_list[1][1]}:bow_and_arrow:\n\
    :third_place: `{finalkills_ranking_44_list[2][0]}` - {finalkills_ranking_44_list[2][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_44_list[3][0]}` - {finalkills_ranking_44_list[3][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_44_list[4][0]}` - {finalkills_ranking_44_list[4][1]}:bow_and_arrow:\n\
    𝟞. `{finalkills_ranking_44_list[5][0]}` - {finalkills_ranking_44_list[5][1]}:bow_and_arrow:\n\
    𝟟. `{finalkills_ranking_44_list[6][0]}` - {finalkills_ranking_44_list[6][1]}:bow_and_arrow:\n\
    𝟠. `{finalkills_ranking_44_list[7][0]}` - {finalkills_ranking_44_list[7][1]}:bow_and_arrow:\n\
    𝟡. `{finalkills_ranking_44_list[8][0]}` - {finalkills_ranking_44_list[8][1]}:bow_and_arrow:\n\
    𝟙𝟘. `{finalkills_ranking_44_list[9][0]}` - {finalkills_ranking_44_list[9][1]}:bow_and_arrow:\n\
    𝟏𝟏. `{finalkills_ranking_44_list[10][0]}` - {finalkills_ranking_44_list[10][1]}:bow_and_arrow:\n\
    𝟏𝟐. `{finalkills_ranking_44_list[11][0]}` - {finalkills_ranking_44_list[11][1]}:bow_and_arrow:\n\
    𝟏𝟑. `{finalkills_ranking_44_list[12][0]}` - {finalkills_ranking_44_list[12][1]}:bow_and_arrow:\n\
    𝟏𝟒. `{finalkills_ranking_44_list[13][0]}` - {finalkills_ranking_44_list[13][1]}:bow_and_arrow:\n\
    𝟏𝟓. `{finalkills_ranking_44_list[14][0]}` - {finalkills_ranking_44_list[14][1]}:bow_and_arrow:\n\
    𝟏𝟔. `{finalkills_ranking_44_list[15][0]}` - {finalkills_ranking_44_list[15][1]}:bow_and_arrow:\n\
    𝟏𝟕. `{finalkills_ranking_44_list[16][0]}` - {finalkills_ranking_44_list[16][1]}:bow_and_arrow:\n\
    𝟏𝟖. `{finalkills_ranking_44_list[17][0]}` - {finalkills_ranking_44_list[17][1]}:bow_and_arrow:\n\
    𝟏𝟗. `{finalkills_ranking_44_list[18][0]}` - {finalkills_ranking_44_list[18][1]}:bow_and_arrow:\n\
    𝟐𝟎. `{finalkills_ranking_44_list[19][0]}` - {finalkills_ranking_44_list[19][1]}:bow_and_arrow:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워침대44" or m=="/배워침대44" or m=="/베워베드44" or m=="/배워배드44" or m=="/베워침대파괴44" or m=="/배워침대파괴44" or m=="/베워배드44" or \
            m=="/배워베드44" or m=="/ㅂㅇㅊㄷ44" or m=="/ㅂㅇㅂㄷ44" or \
                m=="/베워침대5" or m=="/배워침대5" or m=="/베워베드5" or m=="/배워배드5" or m=="/베워침대파괴5" or m=="/배워침대파괴5" or m=="/베워배드5" or \
            m=="/배워베드5" or m=="/ㅂㅇㅊㄷ5" or m=="/ㅂㅇㅂㄷ5" or \
                m=="/베워침대4v4" or m=="/배워침대4v4" or m=="/베워베드4v4" or m=="/배워배드4v4" or m=="/베워침대파괴4v4" or m=="/배워침대파괴4v4" or m=="/베워배드4v4" or \
            m=="/배워베드4v4" or m=="/ㅂㅇㅊㄷ4v4" or m=="/ㅂㅇㅂㄷ4v4" or m=="/qdqe44" or m=="/qdqe5" or m=="/qdce44" or m=="/qdce5" or m=="/krbw4v4_bedsbroken"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟒𝐯𝟒 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{bedsbroken_ranking_44_list[0][0]}` - {bedsbroken_ranking_44_list[0][1]}:hammer:\n\
    :second_place: `{bedsbroken_ranking_44_list[1][0]}` - {bedsbroken_ranking_44_list[1][1]}:hammer:\n\
    :third_place: `{bedsbroken_ranking_44_list[2][0]}` - {bedsbroken_ranking_44_list[2][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_44_list[3][0]}` - {bedsbroken_ranking_44_list[3][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_44_list[4][0]}` - {bedsbroken_ranking_44_list[4][1]}:hammer:\n\
    𝟞. `{bedsbroken_ranking_44_list[5][0]}` - {bedsbroken_ranking_44_list[5][1]}:hammer:\n\
    𝟟. `{bedsbroken_ranking_44_list[6][0]}` - {bedsbroken_ranking_44_list[6][1]}:hammer:\n\
    𝟠. `{bedsbroken_ranking_44_list[7][0]}` - {bedsbroken_ranking_44_list[7][1]}:hammer:\n\
    𝟡. `{bedsbroken_ranking_44_list[8][0]}` - {bedsbroken_ranking_44_list[8][1]}:hammer:\n\
    𝟙𝟘. `{bedsbroken_ranking_44_list[9][0]}` - {bedsbroken_ranking_44_list[9][1]}:hammer:\n\
    𝟏𝟏. `{bedsbroken_ranking_44_list[10][0]}` - {bedsbroken_ranking_44_list[10][1]}:hammer:\n\
    𝟏𝟐. `{bedsbroken_ranking_44_list[11][0]}` - {bedsbroken_ranking_44_list[11][1]}:hammer:\n\
    𝟏𝟑. `{bedsbroken_ranking_44_list[12][0]}` - {bedsbroken_ranking_44_list[12][1]}:hammer:\n\
    𝟏𝟒. `{bedsbroken_ranking_44_list[13][0]}` - {bedsbroken_ranking_44_list[13][1]}:hammer:\n\
    𝟏𝟓. `{bedsbroken_ranking_44_list[14][0]}` - {bedsbroken_ranking_44_list[14][1]}:hammer:\n\
    𝟏𝟔. `{bedsbroken_ranking_44_list[15][0]}` - {bedsbroken_ranking_44_list[15][1]}:hammer:\n\
    𝟏𝟕. `{bedsbroken_ranking_44_list[16][0]}` - {bedsbroken_ranking_44_list[16][1]}:hammer:\n\
    𝟏𝟖. `{bedsbroken_ranking_44_list[17][0]}` - {bedsbroken_ranking_44_list[17][1]}:hammer:\n\
    𝟏𝟗. `{bedsbroken_ranking_44_list[18][0]}` - {bedsbroken_ranking_44_list[18][1]}:hammer:\n\
    𝟐𝟎. `{bedsbroken_ranking_44_list[19][0]}` - {bedsbroken_ranking_44_list[19][1]}:hammer:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

    #===========================================================================================================================================
    #1send
        elif (m=="/베워우승1s" or m=="/배워우승1s" or m=="/베워승리1s" or m=="/배워승리1s"or m=="/ㅂㅇㅇㅅ1s" or m=="/ㅂㅇㅅㄹ1s" or\
        m=="/베워우승1" or m=="/배워우승1" or m=="/베워승리1" or m=="/배워승리1"or m=="/ㅂㅇㅇㅅ1" or m=="/ㅂㅇㅅㄹ1" or \
            m=="/베워우승솔로" or m=="/배워우승솔로" or m=="/베워승리솔로" or m=="/배워승리솔로"or m=="/ㅂㅇㅇㅅㅅㄹ" or m=="/ㅂㅇㅅㄹㅅㄹ" or\
                m=="/qddt1" or m=="/qdtf1" or m=="/krbwsolo_wins" or m=="/krbw1s_wins"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐒𝐨𝐥𝐨 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{wins_ranking_1_list[0][0]}` - {wins_ranking_1_list[0][1]}:trophy:\n\
    :second_place: `{wins_ranking_1_list[1][0]}` - {wins_ranking_1_list[1][1]}:trophy:\n\
    :third_place: `{wins_ranking_1_list[2][0]}` - {wins_ranking_1_list[2][1]}:trophy:\n\
    :medal: `{wins_ranking_1_list[3][0]}` - {wins_ranking_1_list[3][1]}:trophy:\n\
    :medal: `{wins_ranking_1_list[4][0]}` - {wins_ranking_1_list[4][1]}:trophy:\n\
    𝟞. `{wins_ranking_1_list[5][0]}` - {wins_ranking_1_list[5][1]}:trophy:\n\
    𝟟. `{wins_ranking_1_list[6][0]}` - {wins_ranking_1_list[6][1]}:trophy:\n\
    𝟠. `{wins_ranking_1_list[7][0]}` - {wins_ranking_1_list[7][1]}:trophy:\n\
    𝟡. `{wins_ranking_1_list[8][0]}` - {wins_ranking_1_list[8][1]}:trophy:\n\
    𝟙𝟘. `{wins_ranking_1_list[9][0]}` - {wins_ranking_1_list[9][1]}:trophy:\n\
    𝟏𝟏. `{wins_ranking_1_list[10][0]}` - {wins_ranking_1_list[10][1]}:trophy:\n\
    𝟏𝟐. `{wins_ranking_1_list[11][0]}` - {wins_ranking_1_list[11][1]}:trophy:\n\
    𝟏𝟑. `{wins_ranking_1_list[12][0]}` - {wins_ranking_1_list[12][1]}:trophy:\n\
    𝟏𝟒. `{wins_ranking_1_list[13][0]}` - {wins_ranking_1_list[13][1]}:trophy:\n\
    𝟏𝟓. `{wins_ranking_1_list[14][0]}` - {wins_ranking_1_list[14][1]}:trophy:\n\
    𝟏𝟔. `{wins_ranking_1_list[15][0]}` - {wins_ranking_1_list[15][1]}:trophy:\n\
    𝟏𝟕. `{wins_ranking_1_list[16][0]}` - {wins_ranking_1_list[16][1]}:trophy:\n\
    𝟏𝟖. `{wins_ranking_1_list[17][0]}` - {wins_ranking_1_list[17][1]}:trophy:\n\
    𝟏𝟗. `{wins_ranking_1_list[18][0]}` - {wins_ranking_1_list[18][1]}:trophy:\n\
    𝟐𝟎. `{wins_ranking_1_list[19][0]}` - {wins_ranking_1_list[19][1]}:trophy:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워파킬1s" or m=="/배워파킬1s" or m=="/베워파이널킬1s" or m=="/배워파이널킬1s" or\
            m=="/배워파이널1s" or m=="/베워파이널1s" or m=="/ㅂㅇㅍㅋ1s" or m=="/ㅂㅇㅍㅇㄴㅋ1s" or m=="/ㅂㅇㅍㅇㄴ1s" or \
                m=="/베워파킬1" or m=="/배워파킬1" or m=="/베워파이널킬1" or m=="/배워파이널킬1" or\
            m=="/배워파이널1" or m=="/베워파이널1" or m=="/ㅂㅇㅍㅋ1" or m=="/ㅂㅇㅍㅇㄴㅋ1" or m=="/ㅂㅇㅍㅇㄴ1" or \
                m=="/베워파킬솔로" or m=="/배워파킬솔로" or m=="/베워파이널킬솔로" or m=="/배워파이널킬솔로" or\
            m=="/배워파이널솔로" or m=="/베워파이널솔로" or m=="/ㅂㅇㅍㅋㅅㄹ" or m=="/ㅂㅇㅍㅇㄴㅋㅅㄹ" or m=="/ㅂㅇㅍㅇㄴㅅㄹ" or\
                m=="/qdvz1" or m=="/qdvdsz1" or m=="/krbwsolo_finalkills" or m=="/krbw1s_finalkills"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐒𝐨𝐥𝐨 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{finalkills_ranking_1_list[0][0]}` - {finalkills_ranking_1_list[0][1]}:bow_and_arrow:\n\
    :second_place: `{finalkills_ranking_1_list[1][0]}` - {finalkills_ranking_1_list[1][1]}:bow_and_arrow:\n\
    :third_place: `{finalkills_ranking_1_list[2][0]}` - {finalkills_ranking_1_list[2][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_1_list[3][0]}` - {finalkills_ranking_1_list[3][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_1_list[4][0]}` - {finalkills_ranking_1_list[4][1]}:bow_and_arrow:\n\
    𝟞. `{finalkills_ranking_1_list[5][0]}` - {finalkills_ranking_1_list[5][1]}:bow_and_arrow:\n\
    𝟟. `{finalkills_ranking_1_list[6][0]}` - {finalkills_ranking_1_list[6][1]}:bow_and_arrow:\n\
    𝟠. `{finalkills_ranking_1_list[7][0]}` - {finalkills_ranking_1_list[7][1]}:bow_and_arrow:\n\
    𝟡. `{finalkills_ranking_1_list[8][0]}` - {finalkills_ranking_1_list[8][1]}:bow_and_arrow:\n\
    𝟙𝟘. `{finalkills_ranking_1_list[9][0]}` - {finalkills_ranking_1_list[9][1]}:bow_and_arrow:\n\
    𝟏𝟏. `{finalkills_ranking_1_list[10][0]}` - {finalkills_ranking_1_list[10][1]}:bow_and_arrow:\n\
    𝟏𝟐. `{finalkills_ranking_1_list[11][0]}` - {finalkills_ranking_1_list[11][1]}:bow_and_arrow:\n\
    𝟏𝟑. `{finalkills_ranking_1_list[12][0]}` - {finalkills_ranking_1_list[12][1]}:bow_and_arrow:\n\
    𝟏𝟒. `{finalkills_ranking_1_list[13][0]}` - {finalkills_ranking_1_list[13][1]}:bow_and_arrow:\n\
    𝟏𝟓. `{finalkills_ranking_1_list[14][0]}` - {finalkills_ranking_1_list[14][1]}:bow_and_arrow:\n\
    𝟏𝟔. `{finalkills_ranking_1_list[15][0]}` - {finalkills_ranking_1_list[15][1]}:bow_and_arrow:\n\
    𝟏𝟕. `{finalkills_ranking_1_list[16][0]}` - {finalkills_ranking_1_list[16][1]}:bow_and_arrow:\n\
    𝟏𝟖. `{finalkills_ranking_1_list[17][0]}` - {finalkills_ranking_1_list[17][1]}:bow_and_arrow:\n\
    𝟏𝟗. `{finalkills_ranking_1_list[18][0]}` - {finalkills_ranking_1_list[18][1]}:bow_and_arrow:\n\
    𝟐𝟎. `{finalkills_ranking_1_list[19][0]}` - {finalkills_ranking_1_list[19][1]}:bow_and_arrow:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워침대1" or m=="/배워침대1" or m=="/베워베드1" or m=="/배워배드1" or m=="/베워침대파괴1" or m=="/배워침대파괴1" or m=="/베워배드1" or \
            m=="/배워베드1" or m=="/ㅂㅇㅊㄷ1" or m=="/ㅂㅇㅂㄷ1" or \
                m=="/베워침대1s" or m=="/배워침대1s" or m=="/베워베드1s" or m=="/배워배드1s" or m=="/베워침대파괴1s" or m=="/배워침대파괴1s" or m=="/베워배드1s" or \
            m=="/배워베드1s" or m=="/ㅂㅇㅊㄷ1s" or m=="/ㅂㅇㅂㄷ1s" or \
                m=="/베워침대솔로" or m=="/배워침대솔로" or m=="/베워베드솔로" or m=="/배워배드솔로" or m=="/베워침대파괴솔로" or m=="/배워침대파괴솔로" or m=="/베워배드솔로" or \
            m=="/배워베드솔로" or m=="/ㅂㅇㅊㄷㅅㄹ" or m=="/ㅂㅇㅂㄷㅅㄹ" or m=="/qdce1" or m=="/qdqe1" or m=="/krbwsolo_bedsbroken" or m=="/krbw1s_bedsbroken"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐒𝐨𝐥𝐨 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{bedsbroken_ranking_1_list[0][0]}` - {bedsbroken_ranking_1_list[0][1]}:hammer:\n\
    :second_place: `{bedsbroken_ranking_1_list[1][0]}` - {bedsbroken_ranking_1_list[1][1]}:hammer:\n\
    :third_place: `{bedsbroken_ranking_1_list[2][0]}` - {bedsbroken_ranking_1_list[2][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_1_list[3][0]}` - {bedsbroken_ranking_1_list[3][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_1_list[4][0]}` - {bedsbroken_ranking_1_list[4][1]}:hammer:\n\
    𝟞. `{bedsbroken_ranking_1_list[5][0]}` - {bedsbroken_ranking_1_list[5][1]}:hammer:\n\
    𝟟. `{bedsbroken_ranking_1_list[6][0]}` - {bedsbroken_ranking_1_list[6][1]}:hammer:\n\
    𝟠. `{bedsbroken_ranking_1_list[7][0]}` - {bedsbroken_ranking_1_list[7][1]}:hammer:\n\
    𝟡. `{bedsbroken_ranking_1_list[8][0]}` - {bedsbroken_ranking_1_list[8][1]}:hammer:\n\
    𝟙𝟘. `{bedsbroken_ranking_1_list[9][0]}` - {bedsbroken_ranking_1_list[9][1]}:hammer:\n\
    𝟏𝟏. `{bedsbroken_ranking_1_list[10][0]}` - {bedsbroken_ranking_1_list[10][1]}:hammer:\n\
    𝟏𝟐. `{bedsbroken_ranking_1_list[11][0]}` - {bedsbroken_ranking_1_list[11][1]}:hammer:\n\
    𝟏𝟑. `{bedsbroken_ranking_1_list[12][0]}` - {bedsbroken_ranking_1_list[12][1]}:hammer:\n\
    𝟏𝟒. `{bedsbroken_ranking_1_list[13][0]}` - {bedsbroken_ranking_1_list[13][1]}:hammer:\n\
    𝟏𝟓. `{bedsbroken_ranking_1_list[14][0]}` - {bedsbroken_ranking_1_list[14][1]}:hammer:\n\
    𝟏𝟔. `{bedsbroken_ranking_1_list[15][0]}` - {bedsbroken_ranking_1_list[15][1]}:hammer:\n\
    𝟏𝟕. `{bedsbroken_ranking_1_list[16][0]}` - {bedsbroken_ranking_1_list[16][1]}:hammer:\n\
    𝟏𝟖. `{bedsbroken_ranking_1_list[17][0]}` - {bedsbroken_ranking_1_list[17][1]}:hammer:\n\
    𝟏𝟗. `{bedsbroken_ranking_1_list[18][0]}` - {bedsbroken_ranking_1_list[18][1]}:hammer:\n\
    𝟐𝟎. `{bedsbroken_ranking_1_list[19][0]}` - {bedsbroken_ranking_1_list[19][1]}:hammer:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

    #===========================================================================================================================================
    #2send
        elif (m=="/베워우승2s" or m=="/배워우승2s" or m=="/베워승리2s" or m=="/배워승리2s"or m=="/ㅂㅇㅇㅅ2s" or m=="/ㅂㅇㅅㄹ2s" or\
        m=="/베워우승2" or m=="/배워우승2" or m=="/베워승리2" or m=="/배워승리2"or m=="/ㅂㅇㅇㅅ2" or m=="/ㅂㅇㅅㄹ2" or \
            m=="/베워우승더블" or m=="/배워우승더블" or m=="/베워승리더블" or m=="/배워승리더블"or m=="/ㅂㅇㅇㅅㄷㅂ" or m=="/ㅂㅇㅅㄹㄷㅂ" or\
                m=="/qddt2" or m=="/qdtf2" or m=="/krbwdouble_wins" or m=="/krbw2s_wins"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐃𝐨𝐮𝐛𝐥𝐞 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{wins_ranking_2_list[0][0]}` - {wins_ranking_2_list[0][1]}:trophy:\n\
    :second_place: `{wins_ranking_2_list[1][0]}` - {wins_ranking_2_list[1][1]}:trophy:\n\
    :third_place: `{wins_ranking_2_list[2][0]}` - {wins_ranking_2_list[2][1]}:trophy:\n\
    :medal: `{wins_ranking_2_list[3][0]}` - {wins_ranking_2_list[3][1]}:trophy:\n\
    :medal: `{wins_ranking_2_list[4][0]}` - {wins_ranking_2_list[4][1]}:trophy:\n\
    𝟞. `{wins_ranking_2_list[5][0]}` - {wins_ranking_2_list[5][1]}:trophy:\n\
    𝟟. `{wins_ranking_2_list[6][0]}` - {wins_ranking_2_list[6][1]}:trophy:\n\
    𝟠. `{wins_ranking_2_list[7][0]}` - {wins_ranking_2_list[7][1]}:trophy:\n\
    𝟡. `{wins_ranking_2_list[8][0]}` - {wins_ranking_2_list[8][1]}:trophy:\n\
    𝟙𝟘. `{wins_ranking_2_list[9][0]}` - {wins_ranking_2_list[9][1]}:trophy:\n\
    𝟏𝟏. `{wins_ranking_2_list[10][0]}` - {wins_ranking_2_list[10][1]}:trophy:\n\
    𝟏𝟐. `{wins_ranking_2_list[11][0]}` - {wins_ranking_2_list[11][1]}:trophy:\n\
    𝟏𝟑. `{wins_ranking_2_list[12][0]}` - {wins_ranking_2_list[12][1]}:trophy:\n\
    𝟏𝟒. `{wins_ranking_2_list[13][0]}` - {wins_ranking_2_list[13][1]}:trophy:\n\
    𝟏𝟓. `{wins_ranking_2_list[14][0]}` - {wins_ranking_2_list[14][1]}:trophy:\n\
    𝟏𝟔. `{wins_ranking_2_list[15][0]}` - {wins_ranking_2_list[15][1]}:trophy:\n\
    𝟏𝟕. `{wins_ranking_2_list[16][0]}` - {wins_ranking_2_list[16][1]}:trophy:\n\
    𝟏𝟖. `{wins_ranking_2_list[17][0]}` - {wins_ranking_2_list[17][1]}:trophy:\n\
    𝟏𝟗. `{wins_ranking_2_list[18][0]}` - {wins_ranking_2_list[18][1]}:trophy:\n\
    𝟐𝟎. `{wins_ranking_2_list[19][0]}` - {wins_ranking_2_list[19][1]}:trophy:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워파킬2s" or m=="/배워파킬2s" or m=="/베워파이널킬2s" or m=="/배워파이널킬2s" or\
            m=="/배워파이널2s" or m=="/베워파이널2s" or m=="/ㅂㅇㅍㅋ2s" or m=="/ㅂㅇㅍㅇㄴㅋ2s" or m=="/ㅂㅇㅍㅇㄴ2s" or \
                m=="/베워파킬2" or m=="/배워파킬2" or m=="/베워파이널킬2" or m=="/배워파이널킬2" or\
            m=="/배워파이널2" or m=="/베워파이널2" or m=="/ㅂㅇㅍㅋ2" or m=="/ㅂㅇㅍㅇㄴㅋ2" or m=="/ㅂㅇㅍㅇㄴ2" or \
                m=="/베워파킬더블" or m=="/배워파킬더블" or m=="/베워파이널킬더블" or m=="/배워파이널킬더블" or\
            m=="/배워파이널더블" or m=="/베워파이널더블" or m=="/ㅂㅇㅍㅋㄷㅂ" or m=="/ㅂㅇㅍㅇㄴㅋㄷㅂ" or m=="/ㅂㅇㅍㅇㄴㄷㅂ" or\
                m=="/qdvz2" or m=="/qdvdsz2" or m=="/krbwdouble_finalkills" or m=="/krbw2s_finalkills"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐃𝐨𝐮𝐛𝐥𝐞 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{finalkills_ranking_2_list[0][0]}` - {finalkills_ranking_2_list[0][1]}:bow_and_arrow:\n\
    :second_place: `{finalkills_ranking_2_list[1][0]}` - {finalkills_ranking_2_list[1][1]}:bow_and_arrow:\n\
    :third_place: `{finalkills_ranking_2_list[2][0]}` - {finalkills_ranking_2_list[2][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_2_list[3][0]}` - {finalkills_ranking_2_list[3][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_2_list[4][0]}` - {finalkills_ranking_2_list[4][1]}:bow_and_arrow:\n\
    𝟞. `{finalkills_ranking_2_list[5][0]}` - {finalkills_ranking_2_list[5][1]}:bow_and_arrow:\n\
    𝟟. `{finalkills_ranking_2_list[6][0]}` - {finalkills_ranking_2_list[6][1]}:bow_and_arrow:\n\
    𝟠. `{finalkills_ranking_2_list[7][0]}` - {finalkills_ranking_2_list[7][1]}:bow_and_arrow:\n\
    𝟡. `{finalkills_ranking_2_list[8][0]}` - {finalkills_ranking_2_list[8][1]}:bow_and_arrow:\n\
    𝟙𝟘. `{finalkills_ranking_2_list[9][0]}` - {finalkills_ranking_2_list[9][1]}:bow_and_arrow:\n\
    𝟏𝟏. `{finalkills_ranking_2_list[10][0]}` - {finalkills_ranking_2_list[10][1]}:bow_and_arrow:\n\
    𝟏𝟐. `{finalkills_ranking_2_list[11][0]}` - {finalkills_ranking_2_list[11][1]}:bow_and_arrow:\n\
    𝟏𝟑. `{finalkills_ranking_2_list[12][0]}` - {finalkills_ranking_2_list[12][1]}:bow_and_arrow:\n\
    𝟏𝟒. `{finalkills_ranking_2_list[13][0]}` - {finalkills_ranking_2_list[13][1]}:bow_and_arrow:\n\
    𝟏𝟓. `{finalkills_ranking_2_list[14][0]}` - {finalkills_ranking_2_list[14][1]}:bow_and_arrow:\n\
    𝟏𝟔. `{finalkills_ranking_2_list[15][0]}` - {finalkills_ranking_2_list[15][1]}:bow_and_arrow:\n\
    𝟏𝟕. `{finalkills_ranking_2_list[16][0]}` - {finalkills_ranking_2_list[16][1]}:bow_and_arrow:\n\
    𝟏𝟖. `{finalkills_ranking_2_list[17][0]}` - {finalkills_ranking_2_list[17][1]}:bow_and_arrow:\n\
    𝟏𝟗. `{finalkills_ranking_2_list[18][0]}` - {finalkills_ranking_2_list[18][1]}:bow_and_arrow:\n\
    𝟐𝟎. `{finalkills_ranking_2_list[19][0]}` - {finalkills_ranking_2_list[19][1]}:bow_and_arrow:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워침대2" or m=="/배워침대2" or m=="/베워베드2" or m=="/배워배드2" or m=="/베워침대파괴2" or m=="/배워침대파괴2" or m=="/베워배드2" or \
            m=="/배워베드2" or m=="/ㅂㅇㅊㄷ2" or m=="/ㅂㅇㅂㄷ2" or \
                m=="/베워침대2s" or m=="/배워침대2s" or m=="/베워베드2s" or m=="/배워배드2s" or m=="/베워침대파괴2s" or m=="/배워침대파괴2s" or m=="/베워배드2s" or \
            m=="/배워베드2s" or m=="/ㅂㅇㅊㄷ2s" or m=="/ㅂㅇㅂㄷ2s" or \
                m=="/베워침대더블" or m=="/배워침대더블" or m=="/베워베드더블" or m=="/배워배드더블" or m=="/베워침대파괴더블" or m=="/배워침대파괴더블" or m=="/베워배드더블" or \
            m=="/배워베드더블" or m=="/ㅂㅇㅊㄷㄷㅂ" or m=="/ㅂㅇㅂㄷㄷㅂ" or m=="/qdce2" or m=="/qdqe2" or m=="/krbwdouble_bedsbroken" or m=="/krbw2s_bedsbroken"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐃𝐨𝐮𝐛𝐥𝐞 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{bedsbroken_ranking_2_list[0][0]}` - {bedsbroken_ranking_2_list[0][1]}:hammer:\n\
    :second_place: `{bedsbroken_ranking_2_list[1][0]}` - {bedsbroken_ranking_2_list[1][1]}:hammer:\n\
    :third_place: `{bedsbroken_ranking_2_list[2][0]}` - {bedsbroken_ranking_2_list[2][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_2_list[3][0]}` - {bedsbroken_ranking_2_list[3][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_2_list[4][0]}` - {bedsbroken_ranking_2_list[4][1]}:hammer:\n\
    𝟞. `{bedsbroken_ranking_2_list[5][0]}` - {bedsbroken_ranking_2_list[5][1]}:hammer:\n\
    𝟟. `{bedsbroken_ranking_2_list[6][0]}` - {bedsbroken_ranking_2_list[6][1]}:hammer:\n\
    𝟠. `{bedsbroken_ranking_2_list[7][0]}` - {bedsbroken_ranking_2_list[7][1]}:hammer:\n\
    𝟡. `{bedsbroken_ranking_2_list[8][0]}` - {bedsbroken_ranking_2_list[8][1]}:hammer:\n\
    𝟙𝟘. `{bedsbroken_ranking_2_list[9][0]}` - {bedsbroken_ranking_2_list[9][1]}:hammer:\n\
    𝟏𝟏. `{bedsbroken_ranking_2_list[10][0]}` - {bedsbroken_ranking_2_list[10][1]}:hammer:\n\
    𝟏𝟐. `{bedsbroken_ranking_2_list[11][0]}` - {bedsbroken_ranking_2_list[11][1]}:hammer:\n\
    𝟏𝟑. `{bedsbroken_ranking_2_list[12][0]}` - {bedsbroken_ranking_2_list[12][1]}:hammer:\n\
    𝟏𝟒. `{bedsbroken_ranking_2_list[13][0]}` - {bedsbroken_ranking_2_list[13][1]}:hammer:\n\
    𝟏𝟓. `{bedsbroken_ranking_2_list[14][0]}` - {bedsbroken_ranking_2_list[14][1]}:hammer:\n\
    𝟏𝟔. `{bedsbroken_ranking_2_list[15][0]}` - {bedsbroken_ranking_2_list[15][1]}:hammer:\n\
    𝟏𝟕. `{bedsbroken_ranking_2_list[16][0]}` - {bedsbroken_ranking_2_list[16][1]}:hammer:\n\
    𝟏𝟖. `{bedsbroken_ranking_2_list[17][0]}` - {bedsbroken_ranking_2_list[17][1]}:hammer:\n\
    𝟏𝟗. `{bedsbroken_ranking_2_list[18][0]}` - {bedsbroken_ranking_2_list[18][1]}:hammer:\n\
    𝟐𝟎. `{bedsbroken_ranking_2_list[19][0]}` - {bedsbroken_ranking_2_list[19][1]}:hammer:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

    #===========================================================================================================================================
    #3send
        elif (m=="/베워우승3s" or m=="/배워우승3s" or m=="/베워승리3s" or m=="/배워승리3s"or m=="/ㅂㅇㅇㅅ3s" or m=="/ㅂㅇㅅㄹ3s" or\
        m=="/베워우승3" or m=="/배워우승3" or m=="/베워승리3" or m=="/배워승리3"or m=="/ㅂㅇㅇㅅ3" or m=="/ㅂㅇㅅㄹ3" or\
            m=="/qddt3" or m=="/qdtf3" or m=="/krbw3s_wins"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{wins_ranking_3_list[0][0]}` - {wins_ranking_3_list[0][1]}:trophy:\n\
    :second_place: `{wins_ranking_3_list[1][0]}` - {wins_ranking_3_list[1][1]}:trophy:\n\
    :third_place: `{wins_ranking_3_list[2][0]}` - {wins_ranking_3_list[2][1]}:trophy:\n\
    :medal: `{wins_ranking_3_list[3][0]}` - {wins_ranking_3_list[3][1]}:trophy:\n\
    :medal: `{wins_ranking_3_list[4][0]}` - {wins_ranking_3_list[4][1]}:trophy:\n\
    𝟞. `{wins_ranking_3_list[5][0]}` - {wins_ranking_3_list[5][1]}:trophy:\n\
    𝟟. `{wins_ranking_3_list[6][0]}` - {wins_ranking_3_list[6][1]}:trophy:\n\
    𝟠. `{wins_ranking_3_list[7][0]}` - {wins_ranking_3_list[7][1]}:trophy:\n\
    𝟡. `{wins_ranking_3_list[8][0]}` - {wins_ranking_3_list[8][1]}:trophy:\n\
    𝟙𝟘. `{wins_ranking_3_list[9][0]}` - {wins_ranking_3_list[9][1]}:trophy:\n\
    𝟏𝟏. `{wins_ranking_3_list[10][0]}` - {wins_ranking_3_list[10][1]}:trophy:\n\
    𝟏𝟐. `{wins_ranking_3_list[11][0]}` - {wins_ranking_3_list[11][1]}:trophy:\n\
    𝟏𝟑. `{wins_ranking_3_list[12][0]}` - {wins_ranking_3_list[12][1]}:trophy:\n\
    𝟏𝟒. `{wins_ranking_3_list[13][0]}` - {wins_ranking_3_list[13][1]}:trophy:\n\
    𝟏𝟓. `{wins_ranking_3_list[14][0]}` - {wins_ranking_3_list[14][1]}:trophy:\n\
    𝟏𝟔. `{wins_ranking_3_list[15][0]}` - {wins_ranking_3_list[15][1]}:trophy:\n\
    𝟏𝟕. `{wins_ranking_3_list[16][0]}` - {wins_ranking_3_list[16][1]}:trophy:\n\
    𝟏𝟖. `{wins_ranking_3_list[17][0]}` - {wins_ranking_3_list[17][1]}:trophy:\n\
    𝟏𝟗. `{wins_ranking_3_list[18][0]}` - {wins_ranking_3_list[18][1]}:trophy:\n\
    𝟐𝟎. `{wins_ranking_3_list[19][0]}` - {wins_ranking_3_list[19][1]}:trophy:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워파킬3s" or m=="/배워파킬3s" or m=="/베워파이널킬3s" or m=="/배워파이널킬3s" or\
            m=="/배워파이널3s" or m=="/베워파이널3s" or m=="/ㅂㅇㅍㅋ3s" or m=="/ㅂㅇㅍㅇㄴㅋ3s" or m=="/ㅂㅇㅍㅇㄴ3s" or \
                m=="/베워파킬3" or m=="/배워파킬3" or m=="/베워파이널킬3" or m=="/배워파이널킬3" or\
            m=="/배워파이널3" or m=="/베워파이널3" or m=="/ㅂㅇㅍㅋ3" or m=="/ㅂㅇㅍㅇㄴㅋ3" or m=="/ㅂㅇㅍㅇㄴ3" or\
                m=="/qdvz3" or m=="/qdvdsz3" or m=="/krbw3s_finalkills"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{finalkills_ranking_3_list[0][0]}` - {finalkills_ranking_3_list[0][1]}:bow_and_arrow:\n\
    :second_place: `{finalkills_ranking_3_list[1][0]}` - {finalkills_ranking_3_list[1][1]}:bow_and_arrow:\n\
    :third_place: `{finalkills_ranking_3_list[2][0]}` - {finalkills_ranking_3_list[2][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_3_list[3][0]}` - {finalkills_ranking_3_list[3][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_3_list[4][0]}` - {finalkills_ranking_3_list[4][1]}:bow_and_arrow:\n\
    𝟞. `{finalkills_ranking_3_list[5][0]}` - {finalkills_ranking_3_list[5][1]}:bow_and_arrow:\n\
    𝟟. `{finalkills_ranking_3_list[6][0]}` - {finalkills_ranking_3_list[6][1]}:bow_and_arrow:\n\
    𝟠. `{finalkills_ranking_3_list[7][0]}` - {finalkills_ranking_3_list[7][1]}:bow_and_arrow:\n\
    𝟡. `{finalkills_ranking_3_list[8][0]}` - {finalkills_ranking_3_list[8][1]}:bow_and_arrow:\n\
    𝟙𝟘. `{finalkills_ranking_3_list[9][0]}` - {finalkills_ranking_3_list[9][1]}:bow_and_arrow:\n\
    𝟏𝟏. `{finalkills_ranking_3_list[10][0]}` - {finalkills_ranking_3_list[10][1]}:bow_and_arrow:\n\
    𝟏𝟐. `{finalkills_ranking_3_list[11][0]}` - {finalkills_ranking_3_list[11][1]}:bow_and_arrow:\n\
    𝟏𝟑. `{finalkills_ranking_3_list[12][0]}` - {finalkills_ranking_3_list[12][1]}:bow_and_arrow:\n\
    𝟏𝟒. `{finalkills_ranking_3_list[13][0]}` - {finalkills_ranking_3_list[13][1]}:bow_and_arrow:\n\
    𝟏𝟓. `{finalkills_ranking_3_list[14][0]}` - {finalkills_ranking_3_list[14][1]}:bow_and_arrow:\n\
    𝟏𝟔. `{finalkills_ranking_3_list[15][0]}` - {finalkills_ranking_3_list[15][1]}:bow_and_arrow:\n\
    𝟏𝟕. `{finalkills_ranking_3_list[16][0]}` - {finalkills_ranking_3_list[16][1]}:bow_and_arrow:\n\
    𝟏𝟖. `{finalkills_ranking_3_list[17][0]}` - {finalkills_ranking_3_list[17][1]}:bow_and_arrow:\n\
    𝟏𝟗. `{finalkills_ranking_3_list[18][0]}` - {finalkills_ranking_3_list[18][1]}:bow_and_arrow:\n\
    𝟐𝟎. `{finalkills_ranking_3_list[19][0]}` - {finalkills_ranking_3_list[19][1]}:bow_and_arrow:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워침대3" or m=="/배워침대3" or m=="/베워베드3" or m=="/배워배드3" or m=="/베워침대파괴3" or m=="/배워침대파괴3" or m=="/베워배드3" or \
            m=="/배워베드3" or m=="/ㅂㅇㅊㄷ3" or m=="/ㅂㅇㅂㄷ3" or \
                m=="/베워침대3s" or m=="/배워침대3s" or m=="/베워베드3s" or m=="/배워배드3s" or m=="/베워침대파괴3s" or m=="/배워침대파괴3s" or m=="/베워배드3s" or \
            m=="/배워베드3s" or m=="/ㅂㅇㅊㄷ3s" or m=="/ㅂㅇㅂㄷ3s" or m=="/qdce3" or m=="/qdqe3" or m=="/krbw3s_bedsbroken"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{bedsbroken_ranking_3_list[0][0]}` - {bedsbroken_ranking_3_list[0][1]}:hammer:\n\
    :second_place: `{bedsbroken_ranking_3_list[1][0]}` - {bedsbroken_ranking_3_list[1][1]}:hammer:\n\
    :third_place: `{bedsbroken_ranking_3_list[2][0]}` - {bedsbroken_ranking_3_list[2][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_3_list[3][0]}` - {bedsbroken_ranking_3_list[3][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_3_list[4][0]}` - {bedsbroken_ranking_3_list[4][1]}:hammer:\n\
    𝟞. `{bedsbroken_ranking_3_list[5][0]}` - {bedsbroken_ranking_3_list[5][1]}:hammer:\n\
    𝟟. `{bedsbroken_ranking_3_list[6][0]}` - {bedsbroken_ranking_3_list[6][1]}:hammer:\n\
    𝟠. `{bedsbroken_ranking_3_list[7][0]}` - {bedsbroken_ranking_3_list[7][1]}:hammer:\n\
    𝟡. `{bedsbroken_ranking_3_list[8][0]}` - {bedsbroken_ranking_3_list[8][1]}:hammer:\n\
    𝟙𝟘. `{bedsbroken_ranking_3_list[9][0]}` - {bedsbroken_ranking_3_list[9][1]}:hammer:\n\
    𝟏𝟏. `{bedsbroken_ranking_3_list[10][0]}` - {bedsbroken_ranking_3_list[10][1]}:hammer:\n\
    𝟏𝟐. `{bedsbroken_ranking_3_list[11][0]}` - {bedsbroken_ranking_3_list[11][1]}:hammer:\n\
    𝟏𝟑. `{bedsbroken_ranking_3_list[12][0]}` - {bedsbroken_ranking_3_list[12][1]}:hammer:\n\
    𝟏𝟒. `{bedsbroken_ranking_3_list[13][0]}` - {bedsbroken_ranking_3_list[13][1]}:hammer:\n\
    𝟏𝟓. `{bedsbroken_ranking_3_list[14][0]}` - {bedsbroken_ranking_3_list[14][1]}:hammer:\n\
    𝟏𝟔. `{bedsbroken_ranking_3_list[15][0]}` - {bedsbroken_ranking_3_list[15][1]}:hammer:\n\
    𝟏𝟕. `{bedsbroken_ranking_3_list[16][0]}` - {bedsbroken_ranking_3_list[16][1]}:hammer:\n\
    𝟏𝟖. `{bedsbroken_ranking_3_list[17][0]}` - {bedsbroken_ranking_3_list[17][1]}:hammer:\n\
    𝟏𝟗. `{bedsbroken_ranking_3_list[18][0]}` - {bedsbroken_ranking_3_list[18][1]}:hammer:\n\
    𝟐𝟎. `{bedsbroken_ranking_3_list[19][0]}` - {bedsbroken_ranking_3_list[19][1]}:hammer:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

    #===========================================================================================================================================
    #4send
        elif (m=="/베워우승4s" or m=="/배워우승4s" or m=="/베워승리4s" or m=="/배워승리4s"or m=="/ㅂㅇㅇㅅ4s" or m=="/ㅂㅇㅅㄹ4s" or\
        m=="/베워우승4" or m=="/배워우승4" or m=="/베워승리4" or m=="/배워승리4"or m=="/ㅂㅇㅇㅅ4" or m=="/ㅂㅇㅅㄹ4" or\
            m=="/qddt4" or m=="/qdtf4" or m=="/krbw4s_wins"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{wins_ranking_4_list[0][0]}` - {wins_ranking_4_list[0][1]}:trophy:\n\
    :second_place: `{wins_ranking_4_list[1][0]}` - {wins_ranking_4_list[1][1]}:trophy:\n\
    :third_place: `{wins_ranking_4_list[2][0]}` - {wins_ranking_4_list[2][1]}:trophy:\n\
    :medal: `{wins_ranking_4_list[3][0]}` - {wins_ranking_4_list[3][1]}:trophy:\n\
    :medal: `{wins_ranking_4_list[4][0]}` - {wins_ranking_4_list[4][1]}:trophy:\n\
    𝟞. `{wins_ranking_4_list[5][0]}` - {wins_ranking_4_list[5][1]}:trophy:\n\
    𝟟. `{wins_ranking_4_list[6][0]}` - {wins_ranking_4_list[6][1]}:trophy:\n\
    𝟠. `{wins_ranking_4_list[7][0]}` - {wins_ranking_4_list[7][1]}:trophy:\n\
    𝟡. `{wins_ranking_4_list[8][0]}` - {wins_ranking_4_list[8][1]}:trophy:\n\
    𝟙𝟘. `{wins_ranking_4_list[9][0]}` - {wins_ranking_4_list[9][1]}:trophy:\n\
    𝟏𝟏. `{wins_ranking_4_list[10][0]}` - {wins_ranking_4_list[10][1]}:trophy:\n\
    𝟏𝟐. `{wins_ranking_4_list[11][0]}` - {wins_ranking_4_list[11][1]}:trophy:\n\
    𝟏𝟑. `{wins_ranking_4_list[12][0]}` - {wins_ranking_4_list[12][1]}:trophy:\n\
    𝟏𝟒. `{wins_ranking_4_list[13][0]}` - {wins_ranking_4_list[13][1]}:trophy:\n\
    𝟏𝟓. `{wins_ranking_4_list[14][0]}` - {wins_ranking_4_list[14][1]}:trophy:\n\
    𝟏𝟔. `{wins_ranking_4_list[15][0]}` - {wins_ranking_4_list[15][1]}:trophy:\n\
    𝟏𝟕. `{wins_ranking_4_list[16][0]}` - {wins_ranking_4_list[16][1]}:trophy:\n\
    𝟏𝟖. `{wins_ranking_4_list[17][0]}` - {wins_ranking_4_list[17][1]}:trophy:\n\
    𝟏𝟗. `{wins_ranking_4_list[18][0]}` - {wins_ranking_4_list[18][1]}:trophy:\n\
    𝟐𝟎. `{wins_ranking_4_list[19][0]}` - {wins_ranking_4_list[19][1]}:trophy:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워파킬4s" or m=="/배워파킬4s" or m=="/베워파이널킬4s" or m=="/배워파이널킬4s" or\
            m=="/배워파이널4s" or m=="/베워파이널4s" or m=="/ㅂㅇㅍㅋ4s" or m=="/ㅂㅇㅍㅇㄴㅋ4s" or m=="/ㅂㅇㅍㅇㄴ4s" or \
                m=="/베워파킬4" or m=="/배워파킬4" or m=="/베워파이널킬4" or m=="/배워파이널킬4" or\
            m=="/배워파이널4" or m=="/베워파이널4" or m=="/ㅂㅇㅍㅋ4" or m=="/ㅂㅇㅍㅇㄴㅋ4" or m=="/ㅂㅇㅍㅇㄴ4" or\
                m=="/qdvz4" or m=="/qdvdsz4" or m=="/krbw4s_finalkills"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{finalkills_ranking_4_list[0][0]}` - {finalkills_ranking_4_list[0][1]}:bow_and_arrow:\n\
    :second_place: `{finalkills_ranking_4_list[1][0]}` - {finalkills_ranking_4_list[1][1]}:bow_and_arrow:\n\
    :third_place: `{finalkills_ranking_4_list[2][0]}` - {finalkills_ranking_4_list[2][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_4_list[3][0]}` - {finalkills_ranking_4_list[3][1]}:bow_and_arrow:\n\
    :medal: `{finalkills_ranking_4_list[4][0]}` - {finalkills_ranking_4_list[4][1]}:bow_and_arrow:\n\
    𝟞. `{finalkills_ranking_4_list[5][0]}` - {finalkills_ranking_4_list[5][1]}:bow_and_arrow:\n\
    𝟟. `{finalkills_ranking_4_list[6][0]}` - {finalkills_ranking_4_list[6][1]}:bow_and_arrow:\n\
    𝟠. `{finalkills_ranking_4_list[7][0]}` - {finalkills_ranking_4_list[7][1]}:bow_and_arrow:\n\
    𝟡. `{finalkills_ranking_4_list[8][0]}` - {finalkills_ranking_4_list[8][1]}:bow_and_arrow:\n\
    𝟙𝟘. `{finalkills_ranking_4_list[9][0]}` - {finalkills_ranking_4_list[9][1]}:bow_and_arrow:\n\
    𝟏𝟏. `{finalkills_ranking_4_list[10][0]}` - {finalkills_ranking_4_list[10][1]}:bow_and_arrow:\n\
    𝟏𝟐. `{finalkills_ranking_4_list[11][0]}` - {finalkills_ranking_4_list[11][1]}:bow_and_arrow:\n\
    𝟏𝟑. `{finalkills_ranking_4_list[12][0]}` - {finalkills_ranking_4_list[12][1]}:bow_and_arrow:\n\
    𝟏𝟒. `{finalkills_ranking_4_list[13][0]}` - {finalkills_ranking_4_list[13][1]}:bow_and_arrow:\n\
    𝟏𝟓. `{finalkills_ranking_4_list[14][0]}` - {finalkills_ranking_4_list[14][1]}:bow_and_arrow:\n\
    𝟏𝟔. `{finalkills_ranking_4_list[15][0]}` - {finalkills_ranking_4_list[15][1]}:bow_and_arrow:\n\
    𝟏𝟕. `{finalkills_ranking_4_list[16][0]}` - {finalkills_ranking_4_list[16][1]}:bow_and_arrow:\n\
    𝟏𝟖. `{finalkills_ranking_4_list[17][0]}` - {finalkills_ranking_4_list[17][1]}:bow_and_arrow:\n\
    𝟏𝟗. `{finalkills_ranking_4_list[18][0]}` - {finalkills_ranking_4_list[18][1]}:bow_and_arrow:\n\
    𝟐𝟎. `{finalkills_ranking_4_list[19][0]}` - {finalkills_ranking_4_list[19][1]}:bow_and_arrow:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/베워침대4" or m=="/배워침대4" or m=="/베워베드4" or m=="/배워배드4" or m=="/베워침대파괴4" or m=="/배워침대파괴4" or m=="/베워배드4" or \
            m=="/배워베드4" or m=="/ㅂㅇㅊㄷ4" or m=="/ㅂㅇㅂㄷ4" or \
                m=="/베워침대4s" or m=="/배워침대4s" or m=="/베워베드4s" or m=="/배워배드4s" or m=="/베워침대파괴4s" or m=="/배워침대파괴4s" or m=="/베워배드4s" or \
            m=="/배워베드4s" or m=="/ㅂㅇㅊㄷ4s" or m=="/ㅂㅇㅂㄷ4s" or m=="/qdce4" or m=="/qdqe4" or m=="/krbw4s_bedsbroken"):
            try:
                await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎】`\n\n\
    :first_place: `{bedsbroken_ranking_4_list[0][0]}` - {bedsbroken_ranking_4_list[0][1]}:hammer:\n\
    :second_place: `{bedsbroken_ranking_4_list[1][0]}` - {bedsbroken_ranking_4_list[1][1]}:hammer:\n\
    :third_place: `{bedsbroken_ranking_4_list[2][0]}` - {bedsbroken_ranking_4_list[2][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_4_list[3][0]}` - {bedsbroken_ranking_4_list[3][1]}:hammer:\n\
    :medal: `{bedsbroken_ranking_4_list[4][0]}` - {bedsbroken_ranking_4_list[4][1]}:hammer:\n\
    𝟞. `{bedsbroken_ranking_4_list[5][0]}` - {bedsbroken_ranking_4_list[5][1]}:hammer:\n\
    𝟟. `{bedsbroken_ranking_4_list[6][0]}` - {bedsbroken_ranking_4_list[6][1]}:hammer:\n\
    𝟠. `{bedsbroken_ranking_4_list[7][0]}` - {bedsbroken_ranking_4_list[7][1]}:hammer:\n\
    𝟡. `{bedsbroken_ranking_4_list[8][0]}` - {bedsbroken_ranking_4_list[8][1]}:hammer:\n\
    𝟙𝟘. `{bedsbroken_ranking_4_list[9][0]}` - {bedsbroken_ranking_4_list[9][1]}:hammer:\n\
    𝟏𝟏. `{bedsbroken_ranking_4_list[10][0]}` - {bedsbroken_ranking_4_list[10][1]}:hammer:\n\
    𝟏𝟐. `{bedsbroken_ranking_4_list[11][0]}` - {bedsbroken_ranking_4_list[11][1]}:hammer:\n\
    𝟏𝟑. `{bedsbroken_ranking_4_list[12][0]}` - {bedsbroken_ranking_4_list[12][1]}:hammer:\n\
    𝟏𝟒. `{bedsbroken_ranking_4_list[13][0]}` - {bedsbroken_ranking_4_list[13][1]}:hammer:\n\
    𝟏𝟓. `{bedsbroken_ranking_4_list[14][0]}` - {bedsbroken_ranking_4_list[14][1]}:hammer:\n\
    𝟏𝟔. `{bedsbroken_ranking_4_list[15][0]}` - {bedsbroken_ranking_4_list[15][1]}:hammer:\n\
    𝟏𝟕. `{bedsbroken_ranking_4_list[16][0]}` - {bedsbroken_ranking_4_list[16][1]}:hammer:\n\
    𝟏𝟖. `{bedsbroken_ranking_4_list[17][0]}` - {bedsbroken_ranking_4_list[17][1]}:hammer:\n\
    𝟏𝟗. `{bedsbroken_ranking_4_list[18][0]}` - {bedsbroken_ranking_4_list[18][1]}:hammer:\n\
    𝟐𝟎. `{bedsbroken_ranking_4_list[19][0]}` - {bedsbroken_ranking_4_list[19][1]}:hammer:\n\n\
    `최근 갱신 : {level_kor_time.year}년 {level_kor_time.month}월 {level_kor_time.day}일 {level_kor_time.hour}시 {level_kor_time.minute}분`")
            except:
                await message.channel.send(f"봇이 실행중입니다. 잠시만 기다려주세요.\n남은 작업 ({i}/{len_player_lists})")

        elif (m=="/업데이트" or m=="/업데이트내역" or m=="/ㅇㄷㅇㅌ" or m=="/dedx"):
            await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐔𝐩𝐝𝐚𝐭𝐞 𝐇𝐢𝐬𝐭𝐨𝐫𝐲】`\n\n\
    `2021-06-09`\n\
    𝟏. 플레이어 목록 업데이트\n\n\
    𝟐. 개인 메세지를 통한 명령어 사용 차단\n\n\
    모든 업데이트 내역: http://kbwstatswiki.kro.kr/")

        elif (message.content.startswith("/krbwcommand")):
            m = m.replace("/krbwcommand","")
            await message.channel.send(f"[{m}]")
            try:
                if "access" in m or "token" in m:
                    pass
                else:
                    str_temp = ""
                    for numup in range(0,50):
                        str_temp = str((numup+1)) + ". " + str(eval(f'{m}[{numup}][0]')) + " - " + str(eval(f'{m}[{numup}][1]' + "\n"))
                        str_temp += str_temp
                    await message.channel.send(str_temp)
            except:
                await message.channel.send(f"ERROR")
        
        elif (message.content.startswith("/베워") or message.content.startswith("/배워") or message.content.startswith("/ㅂㅇ") or\
            message.content.startswith("/qd")):
            await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐋𝐢𝐬𝐭】`\n\n\
    `/베워 레벨` - 𝐋𝐞𝐯𝐞𝐥 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/베워 우승` - 𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 파킬` - 𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 침대` - 𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/베워 우승 1` - 𝐒𝐨𝐥𝐨 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 파킬 1` - 𝐒𝐨𝐥𝐨 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 침대 1` - 𝐒𝐨𝐥𝐨 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/베워 우승 2` - 𝐃𝐨𝐮𝐛𝐥𝐞 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 파킬 2` - 𝐃𝐨𝐮𝐛𝐥𝐞 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 침대 2` - 𝐃𝐨𝐮𝐛𝐥𝐞 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/베워 우승 3` - 𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 파킬 3` - 𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 침대 3` - 𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/베워 우승 4` - 𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 파킬 4` - 𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 침대 4` - 𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/베워 우승 44` - 𝟒𝐯𝟒 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 파킬 44` - 𝟒𝐯𝟒 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/베워 침대 44` - 𝟒𝐯𝟒 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/업데이트` - 𝐔𝐩𝐝𝐚𝐭𝐞 𝐇𝐢𝐬𝐭𝐨𝐫𝐲")

        elif (message.content.startswith("/krbw")):
            await message.channel.send(f"`𝐇𝐲𝐩𝐢𝐱𝐞𝐥 𝐊𝐨𝐫𝐞𝐚 𝐁𝐞𝐝𝐰𝐚𝐫𝐬 𝐑𝐚𝐧𝐤𝐢𝐧𝐠`\n`【𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐋𝐢𝐬𝐭】`\n\n\
    `/krbw level` - 𝐋𝐞𝐯𝐞𝐥 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/krbw wins` - 𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw finalkills` - 𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw bedsbroken` - 𝐎𝐯𝐞𝐫𝐚𝐥𝐥 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/krbw solo_wins` - 𝐒𝐨𝐥𝐨 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw solo_finalkills` - 𝐒𝐨𝐥𝐨 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw solo_bedsbroken` - 𝐒𝐨𝐥𝐨 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/krbw double_wins` - 𝐃𝐨𝐮𝐛𝐥𝐞 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw double_finalkills` - 𝐃𝐨𝐮𝐛𝐥𝐞 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw double_bedsbroken` - 𝐃𝐨𝐮𝐛𝐥𝐞 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/krbw 3s_wins` - 𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw 3s_finalkills` - 𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw 3s_bedsbroken` - 𝟑𝐯𝟑𝐯𝟑𝐯𝟑 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/krbw 4s_bedsbroken` - 𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw 4s_finalkills` - 𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw 4s_bedsbroken` - 𝟒𝐯𝟒𝐯𝟒𝐯𝟒 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎\n\n\
    `/krbw 4v4_wins` - 𝟒𝐯𝟒 𝐖𝐢𝐧𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw 4v4_finalkills` - 𝟒𝐯𝟒 𝐅𝐢𝐧𝐚𝐥𝐊𝐢𝐥𝐥𝐬 𝐓𝐎𝐏𝟐𝟎\n\
    `/krbw 4v4_bedsbroken` - 𝟒𝐯𝟒 𝐁𝐞𝐝𝐬𝐁𝐫𝐨𝐤𝐞𝐧 𝐓𝐎𝐏𝟐𝟎") 

    elif message.author != client.user:
        try:
            await message.channel.send("개인 메세지는 허용되지 않습니다.")
        except:
            pass

#-------------------------------------------------------------------------------------------------------------------------------------------
level_ranking_dict = dict()
level_ranking_list = list()
wins_ranking_dict = dict()
wins_ranking_list = list()
finalkills_ranking_dict = dict()
finalkills_ranking_list = list()
bedsbroken_ranking_dict = dict()
bedsbroken_ranking_list = list()
wins_ranking_44_dict = dict()
wins_ranking_44_list = list()
finalkills_ranking_44_dict = dict()
finalkills_ranking_44_list = list()
bedsbroken_ranking_44_dict = dict()
bedsbroken_ranking_44_list = list()
wins_ranking_1_dict = dict()
wins_ranking_1_list = list()
finalkills_ranking_1_dict = dict()
finalkills_ranking_1_list = list()
bedsbroken_ranking_1_dict = dict()
bedsbroken_ranking_1_list = list()
wins_ranking_2_dict = dict()
wins_ranking_2_list = list()
finalkills_ranking_2_dict = dict()
finalkills_ranking_2_list = list()
bedsbroken_ranking_2_dict = dict()
bedsbroken_ranking_2_list = list()
wins_ranking_3_dict = dict()
wins_ranking_3_list = list()
finalkills_ranking_3_dict = dict()
finalkills_ranking_3_list = list()
bedsbroken_ranking_3_dict = dict()
bedsbroken_ranking_3_list = list()
wins_ranking_4_dict = dict()
wins_ranking_4_list = list()
finalkills_ranking_4_dict = dict()
finalkills_ranking_4_list = list()
bedsbroken_ranking_4_dict = dict()
bedsbroken_ranking_4_list = list()


def loop():
    while not client.is_closed():  
        try:
            global level_ranking_dict
            level_ranking_dict.clear()
            global wins_ranking_dict
            wins_ranking_dict.clear()
            global finalkills_ranking_dict
            finalkills_ranking_dict.clear()
            global bedsbroken_ranking_dict
            bedsbroken_ranking_dict.clear()
            global wins_ranking_44_dict
            wins_ranking_44_dict.clear()
            global finalkills_ranking_44_dict
            finalkills_ranking_44_dict.clear()
            global bedsbroken_ranking_44_dict
            bedsbroken_ranking_44_dict.clear()
            global wins_ranking_1_dict
            wins_ranking_1_dict.clear()
            global finalkills_ranking_1_dict
            finalkills_ranking_1_dict.clear()
            global bedsbroken_ranking_1_dict
            bedsbroken_ranking_1_dict.clear()
            global wins_ranking_2_dict
            wins_ranking_2_dict.clear()
            global finalkills_ranking_2_dict
            finalkills_ranking_2_dict.clear()
            global bedsbroken_ranking_2_dict
            bedsbroken_ranking_2_dict.clear()
            global wins_ranking_3_dict
            wins_ranking_3_dict.clear()
            global finalkills_ranking_3_dict
            finalkills_ranking_3_dict.clear()
            global bedsbroken_ranking_3_dict
            bedsbroken_ranking_3_dict.clear()
            global wins_ranking_4_dict
            wins_ranking_4_dict.clear()
            global finalkills_ranking_4_dict
            finalkills_ranking_4_dict.clear()
            global bedsbroken_ranking_4_dict
            bedsbroken_ranking_4_dict.clear()
            global first_load

            webpage = requests.get(access_list)
            soup = BeautifulSoup(webpage.content, "html.parser")
            player_lists = str(soup.p.string).split()
            global i
            i = 0
            global len_player_lists
            len_player_lists = len(player_lists)
            for player_list in player_lists:
                while True:
                    try:
                        player_data = requests.get(f"{access_api}={player_list}").json()
                        break
                    except:
                        time.sleep(0.1)
                        continue
                i += 1
                player_name = str(player_data["player"]["displayname"])
                print(player_name)
                player_level_int = int(player_data["player"]["achievements"]["bedwars_level"])
                try:
                    exp = player_data["player"]["stats"]["Bedwars"]["Experience"]
                except:
                    exp = 0
                exp_len = len(str(exp))
                exp_float = float(exp) * float(0.1**exp_len)
                player_level = float(player_level_int) + float(exp_float)
                #0
                try:
                    player_wins = int(player_data["player"]["stats"]["Bedwars"]["wins_bedwars"])
                except:
                    player_wins = 0
                try:
                    player_finalkills = int(player_data["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
                except:
                    player_finalkills = 0
                try:
                    player_bedsbroken = int(player_data["player"]["stats"]["Bedwars"]["beds_broken_bedwars"])
                except:
                    player_bedsbroken = 0
                level_ranking_dict[player_name] = player_level
                wins_ranking_dict[player_name] = player_wins
                finalkills_ranking_dict[player_name] = player_finalkills
                bedsbroken_ranking_dict[player_name] = player_bedsbroken
                #44
                try:
                    player_44_wins = int(player_data["player"]["stats"]["Bedwars"]["two_four_wins_bedwars"])
                except:
                    player_44_wins = 0
                try:
                    player_44_finalkills = int(player_data["player"]["stats"]["Bedwars"]["two_four_final_kills_bedwars"])
                except:
                    player_44_finalkills = 0
                try:
                    player_44_bedsbroken = int(player_data["player"]["stats"]["Bedwars"]["two_four_beds_broken_bedwars"])
                except:
                    player_44_bedsbroken = 0
                wins_ranking_44_dict[player_name] = player_44_wins
                finalkills_ranking_44_dict[player_name] = player_44_finalkills
                bedsbroken_ranking_44_dict[player_name] = player_44_bedsbroken
                #1
                try:
                    player_1_wins = int(player_data["player"]["stats"]["Bedwars"]["eight_one_wins_bedwars"])
                except:
                    player_1_wins = 0
                try:
                    player_1_finalkills = int(player_data["player"]["stats"]["Bedwars"]["eight_one_final_kills_bedwars"])
                except:
                    player_1_finalkills = 0 
                try:
                    player_1_bedsbroken = int(player_data["player"]["stats"]["Bedwars"]["eight_one_beds_broken_bedwars"])
                except:
                    player_1_bedsbroken = 0
                wins_ranking_1_dict[player_name] = player_1_wins
                finalkills_ranking_1_dict[player_name] = player_1_finalkills
                bedsbroken_ranking_1_dict[player_name] = player_1_bedsbroken
                #2
                try:
                    player_2_wins = int(player_data["player"]["stats"]["Bedwars"]["eight_two_wins_bedwars"])
                except:
                    player_2_wins = 0
                try:
                    player_2_finalkills = int(player_data["player"]["stats"]["Bedwars"]["eight_two_final_kills_bedwars"])
                except:
                    player_2_finalkills = 0
                try:
                    player_2_bedsbroken = int(player_data["player"]["stats"]["Bedwars"]["eight_two_beds_broken_bedwars"])
                except:
                    player_2_bedsbroken = 0
                wins_ranking_2_dict[player_name] = player_2_wins
                finalkills_ranking_2_dict[player_name] = player_2_finalkills
                bedsbroken_ranking_2_dict[player_name] = player_2_bedsbroken
                #3
                try:
                    player_3_wins = int(player_data["player"]["stats"]["Bedwars"]["four_three_wins_bedwars"])
                except:
                    player_3_wins = 0
                try:
                    player_3_finalkills = int(player_data["player"]["stats"]["Bedwars"]["four_three_final_kills_bedwars"])
                except:
                    player_3_finalkills = 0
                try:
                    player_3_bedsbroken = int(player_data["player"]["stats"]["Bedwars"]["four_three_beds_broken_bedwars"])
                except:
                    player_3_bedsbroken = 0
                wins_ranking_3_dict[player_name] = player_3_wins
                finalkills_ranking_3_dict[player_name] = player_3_finalkills
                bedsbroken_ranking_3_dict[player_name] = player_3_bedsbroken
                #4
                try:
                    player_4_wins = int(player_data["player"]["stats"]["Bedwars"]["four_four_wins_bedwars"])
                except:
                    player_4_wins = 0
                try:
                    player_4_finalkills = int(player_data["player"]["stats"]["Bedwars"]["four_four_final_kills_bedwars"])
                except:
                    player_4_finalkills = 0
                try:
                    player_4_bedsbroken = int(player_data["player"]["stats"]["Bedwars"]["four_four_beds_broken_bedwars"])
                except:
                    player_4_bedsbroken = 0
                wins_ranking_4_dict[player_name] = player_4_wins
                finalkills_ranking_4_dict[player_name] = player_4_finalkills
                bedsbroken_ranking_4_dict[player_name] = player_4_bedsbroken
            # 시간 time
            utcnow= datetime.datetime.utcnow()
            time_gap= datetime.timedelta(hours=9)
            global level_kor_time
            level_kor_time= utcnow+ time_gap
            #0
            global level_ranking_list
            level_ranking_list = sorted(level_ranking_dict.items(),reverse=True,key=lambda item:item[1])
            global wins_ranking_list
            wins_ranking_list = sorted(wins_ranking_dict.items(),reverse=True,key=lambda item:item[1])
            global finalkills_ranking_list
            finalkills_ranking_list = sorted(finalkills_ranking_dict.items(),reverse=True,key=lambda item:item[1])
            global bedsbroken_ranking_list
            bedsbroken_ranking_list = sorted(bedsbroken_ranking_dict.items(),reverse=True,key=lambda item:item[1])
            #print("Overall 갱신됨")
            #44
            global wins_ranking_44_list
            wins_ranking_44_list = sorted(wins_ranking_44_dict.items(),reverse=True,key=lambda item:item[1])
            global finalkills_ranking_44_list
            finalkills_ranking_44_list = sorted(finalkills_ranking_44_dict.items(),reverse=True,key=lambda item:item[1])
            global bedsbroken_ranking_44_list
            bedsbroken_ranking_44_list = sorted(bedsbroken_ranking_44_dict.items(),reverse=True,key=lambda item:item[1])
            #print("44 갱신됨")
            #1
            global wins_ranking_1_list
            wins_ranking_1_list = sorted(wins_ranking_1_dict.items(),reverse=True,key=lambda item:item[1])
            global finalkills_ranking_1_list
            finalkills_ranking_1_list = sorted(finalkills_ranking_1_dict.items(),reverse=True,key=lambda item:item[1])
            global bedsbroken_ranking_1_list
            bedsbroken_ranking_1_list = sorted(bedsbroken_ranking_1_dict.items(),reverse=True,key=lambda item:item[1])
            #print("1 갱신됨")
            #2
            global wins_ranking_2_list
            wins_ranking_2_list = sorted(wins_ranking_2_dict.items(),reverse=True,key=lambda item:item[1])
            global finalkills_ranking_2_list
            finalkills_ranking_2_list = sorted(finalkills_ranking_2_dict.items(),reverse=True,key=lambda item:item[1])
            global bedsbroken_ranking_2_list
            bedsbroken_ranking_2_list = sorted(bedsbroken_ranking_2_dict.items(),reverse=True,key=lambda item:item[1])
            #print("2 갱신됨")
            #3
            global wins_ranking_3_list
            wins_ranking_3_list = sorted(wins_ranking_3_dict.items(),reverse=True,key=lambda item:item[1])
            global finalkills_ranking_3_list
            finalkills_ranking_3_list = sorted(finalkills_ranking_3_dict.items(),reverse=True,key=lambda item:item[1])
            global bedsbroken_ranking_3_list
            bedsbroken_ranking_3_list = sorted(bedsbroken_ranking_3_dict.items(),reverse=True,key=lambda item:item[1])
            #print("3 갱신됨")
            #4
            global wins_ranking_4_list
            wins_ranking_4_list = sorted(wins_ranking_4_dict.items(),reverse=True,key=lambda item:item[1])
            global finalkills_ranking_4_list
            finalkills_ranking_4_list = sorted(finalkills_ranking_4_dict.items(),reverse=True,key=lambda item:item[1])
            global bedsbroken_ranking_4_list
            bedsbroken_ranking_4_list = sorted(bedsbroken_ranking_4_dict.items(),reverse=True,key=lambda item:item[1])
            #print("4 갱신됨")
            first_load = 1
            
        except:
            #print("오류 발생 1초 기다리기")
            print("오류 발생")
            time.sleep(1)
#-------------------------------------------------------------------------------------------------------------------------------------------


@tasks.loop(seconds=3)
async def loop2():
    if first_load == 1:
        global level_kor_time
        await client.change_presence(status = discord.Status.online, activity = discord.Activity(type=discord.ActivityType.watching, name = f"/베워 ({level_kor_time.hour}시 {level_kor_time.minute}분 갱신)"))

client.run(token)
