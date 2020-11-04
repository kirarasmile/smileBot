# bot.py
#  uvicorn --host 0.0.0.0 --port 8080 bot:bot.asgi
from aiocqhttp import CQHttp, Event, Message, MessageSegment
import requests
import json
import config
import feedparser
from src.wyy import wyy
from src.setu import setu
from src.steam import steam
from src.kaw import kaw
from src.pixiv import pixivday, pixivweek, pixivmonth, pixivmale
from src.epicfree import epicfree
from src.manongweek import manongweek
from src.searchanime import searchanime
from src.bothelp import bothelp
import re

bot = CQHttp(api_root='http://0.0.0.0:5700')


@bot.on_message('private')
async def _(event: Event):
    # await bot.send(event, '你发了：')
    # print(event.message)
    # 搜番只支持图片格式
    if event.message[0] =='番' and event.message[1] =='剧':
        await searchanime(bot, event)
    elif event.message == 'bot救救我':
        await bothelp(bot, event)
    # elif event.message == '1':
    #     await bot.send(event, '你发了：')
    #     return {'reply': event.message}
    # elif event.message == '色图来！': # 色图bot
    #     await setu(bot, event)
    # elif event.message == '到点了': # 网抑云bot
    #     await wyy(bot, event)
    # elif event.message == 'steam促销':  # steam促销
    #     await steam(bot, event)
    # elif event.message == 'kaw日榜': # 提取Konachan Anime Wallpapers日榜的图片
    #     await kaw(bot, event)
    # elif event.message == '来张日榜图': # 随机提取pixiv日榜的图片
    #     await pixivday(bot, event)
    # elif event.message == '来张月榜图': # 随机提取pixiv月榜的图片
    #     await pixivmonth(bot, event)
    # elif event.message == '来张周榜图': # 随机提取pixiv周榜的图片
    #     await pixivweek(bot, event)
    # elif event.message == '男性向日榜': # 随机提取pixiv男性向日榜的图片
    #     await pixivmale(bot, event)
    # elif event.message == 'epic白嫖': # 本周epic白送游戏
    #     await epicfree(bot, event) 
    # elif event.message == '码农周刊': # 码农周刊
    #     await manongweek(bot, event)

@bot.on_message('group')
async def handle_msg(event):
    # if event.message == '色图来！': # 色图bot,后端还在写，暂不使用
    #     await setu(bot, event)
    # 搜番只支持图片格式
    if event.message[0] =='番' and event.message[1] =='剧':
        await searchanime(bot, event)
    if event.message == '到点了': # 网抑云bot
        await wyy(bot, event)
    # elif event.message == 'steam促销':  # steam促销,因为xml有问题，暂不使用
    #     await steam(bot, event)
    elif event.message == 'kaw日榜': # 提取Konachan Anime Wallpapers日榜的图片
        await kaw(bot, event)
    elif event.message == '来张日榜图': # 随机提取pixiv日榜的图片
        await pixivday(bot, event)
    elif event.message == '来张月榜图': # 随机提取pixiv月榜的图片
        await pixivmonth(bot, event)
    elif event.message == '来张周榜图': # 随机提取pixiv周榜的图片
        await pixivweek(bot, event)
    elif event.message == '男性向日榜': # 随机提取pixiv男性向日榜的图片
        await pixivmale(bot, event)
    # elif event.message == '来张r18色图': # 随机提取pixivR18日榜的图片，该api不可用
    #     await pixivr18(bot, event)
    elif event.message == 'epic白嫖': # 本周epic白送游戏
        await epicfree(bot, event) 
    elif event.message == '码农周刊': # 码农周刊
        await manongweek(bot, event)
    elif event.message == 'bot救救我':
        await bothelp(bot, event)


# bot.run(host='0.0.0.0', port=8080)