import config, feedparser, re, random
from aiocqhttp import MessageSegment
async def pixivday(bot, event):     # 提取pixiv日榜的图片
    data = feedparser.parse(config.rsshub + 'pixiv/ranking/day')
    id = random.randrange(0, len(data.entries))
    link = data.entries[id].link
    title = data.entries[id].title
    summary = data.entries[id].summary
    pattern = re.compile(r'src="(.*?)"', re.I)
    img = re.findall(pattern,summary)
    sendimg = MessageSegment.image(img[0])
    await bot.send(event, "标题：" + title + "\n" + link + "\n" + "原图发送~太慢就等等啦~")
    await bot.send(event, sendimg)

async def pixivweek(bot, event):     # 提取pixiv周榜的图片
    data = feedparser.parse(config.rsshub + 'pixiv/ranking/week')
    id = random.randrange(0, len(data.entries))
    link = data.entries[id].link
    title = data.entries[id].title
    summary = data.entries[id].summary
    pattern = re.compile(r'src="(.*?)"', re.I)
    img = re.findall(pattern,summary)
    sendimg = MessageSegment.image(img[0])
    await bot.send(event, "标题：" + title + "\n" + link + "\n" + "原图发送~太慢就等等啦~")
    await bot.send(event, sendimg)

async def pixivmonth(bot, event):     # 提取pixiv月榜的图片
    data = feedparser.parse(config.rsshub + 'pixiv/ranking/month')
    id = random.randrange(0, len(data.entries))
    link = data.entries[id].link
    title = data.entries[id].title
    summary = data.entries[id].summary
    pattern = re.compile(r'src="(.*?)"', re.I)
    img = re.findall(pattern,summary)
    await bot.send(event, "标题：" + title + "\n" + link + "\n" + "原图发送~太慢就等等啦~")
    # sendimg = MessageSegment.image(img[0])
    sendimg = MessageSegment.image('https://cdn.jsdelivr.net/gh/tydaytygx/NA/NA_icon_report_1080_.png')
    await bot.send(event, sendimg)

async def pixivmale(bot, event):     # 提取pixiv男性向的图片
    data = feedparser.parse(config.rsshub + 'pixiv/ranking/day_male')
    id = random.randrange(0, len(data.entries))
    link = data.entries[id].link
    title = data.entries[id].title
    summary = data.entries[id].summary
    pattern = re.compile(r'src="(.*?)"', re.I)
    img = re.findall(pattern,summary)
    sendimg = MessageSegment.image(img[0])
    await bot.send(event, "标题：" + title + "\n" + link + "\n" + "原图发送~太慢就等等啦~")
    await bot.send(event, sendimg)

# 该api不可用
# async def pixivr18(bot, event):     # 提取pixivR18日榜榜的图片
#     if event.group_id in config.whilelst: #群组白名单
#         data = feedparser.parse(config.rsshub + 'pixiv/ranking/day_r18')
#         id = random.randrange(0, len(data.entries))
#         link = data.entries[id].link
#         title = data.entries[id].title
#         summary = data.entries[id].summary
#         pattern = re.compile(r'src="(.*?)"', re.I)
#         img = re.findall(pattern,summary)
#         sendimg = MessageSegment.image(img[0])
#         await bot.send(event, "标题：" + title + "\n" + link + "\n" + "原图发送~太慢就等等啦~")
#         await bot.send(event, sendimg)
#     else:
#         await bot.send(event, "だめですよ~")