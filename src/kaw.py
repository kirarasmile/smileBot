import config, feedparser, re, random
from aiocqhttp import MessageSegment
async def kaw(bot, event):     # 提取Konachan Anime Wallpapers日榜的图片
    if event.group_id in config.whilelst: #群组白名单
        data = feedparser.parse(config.rsshub + 'konachan/post/popular_recent/1d')
        id = random.randrange(0, len(data.entries))
        link = data.entries[id].link
        title = data.entries[id].title
        summary = data.entries[id].summary
        pattern = re.compile(r'src="(.*?)"', re.I)
        img = re.findall(pattern,summary)
        await bot.send(event, "tag：" + title + "\n" + link)
        sendimg = MessageSegment.image(img[0])
        await bot.send(event, sendimg)
    else:
        await bot.send(event, "您配吗？")