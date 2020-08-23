import config, feedparser, re, random
async def manongweek(bot, event):     # 本周的码农周刊
    data = feedparser.parse(config.rsshub + 'manong-weekly')
    link = data.entries[0].link
    title = data.entries[0].title
    await bot.send(event, title + "\n" + link)