import json, config, requests, random
from aiocqhttp import MessageSegment
async def setu(bot, event):
    if event.group_id in config.whilelst: #群组白名单
        id = random.randrange(12, 131)
        url = config.url + "%d"%id
        res = requests.get(url=url)
        pic = json.loads(res.content)['data']
        await bot.send(event, ""+ pic['title'] + "\n" + "url：" + pic['url'])
        img = MessageSegment.image("https://pixiv.cat/%d"%pic['pid'] + ".jpg")
        await bot.send(event, img)
    else:
        await bot.send(event, "您配吗？")