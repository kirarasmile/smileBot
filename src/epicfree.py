import config, feedparser, re
from aiocqhttp import MessageSegment
async def epicfree(bot, event):
    data = feedparser.parse(config.rsshub + 'epicgames/freegames')
    for i in range(0, len(data.entries)):
        title = data.entries[i].title
        summary = data.entries[i].summary
        link = data.entries[i].link
        pattern = re.compile(r'src="(.*?)"', re.I)
        img = re.findall(pattern,summary)
        sendimg = MessageSegment.image(img[0])
        await bot.send(event, sendimg + "\n" + "游戏名：" + title + "\n" + "链接：" + link)