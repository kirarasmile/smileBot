import config, feedparser, re
async def steam(bot, event):
    data = feedparser.parse(config.rsshub + 'xiaoheihe/discount/pc')
    for i in range(0, 5):
        entries = data.entries[i]
        title = entries.title
        link = entries.link
        item = entries.summary
        moneypattern = re.compile(r'原价: (.*?)<', re.I)
        salepattern = re.compile(r'当前价格: (.*?)<', re.I)
        imgpattern = re.compile(r'src="(.*?)"', re.I)
        money = re.findall(moneypattern, item)
        sale = re.findall(salepattern, item)
        await bot.send(event, "sabi小黑盒的xml似乎有点问题，真实价格请点入链接查看" + "\n" + "游戏名：" + title + "\n" + "原价：" + money[0] + "\n" + "现价:"+ sale[0] + "\n" + "链接：" + link)