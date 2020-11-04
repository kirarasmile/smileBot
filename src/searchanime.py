import requests, re
from aiocqhttp import MessageSegment
async def searchanime(bot, event):  # 搜索番剧截图
    anicount = 0
    pattern = re.compile(r'url=(.*?)]', re.I)
    img = re.findall(pattern,event.message)
    # print(img[0])
    animeimg = img[0]
    searchUrl = "https://trace.moe/api/search?url=" + animeimg
    data = requests.get(url=searchUrl)
    # print(data.json())
    datalen = len(data.json()['docs'])
    for i in range(0, datalen):
        if data.json()['docs'][i]['similarity'] > 0.85:
            anicount += 1
            time = str(data.json()['docs'][i]['from']/60)
            title = data.json()['docs'][i]['title_chinese']
            episode = str(data.json()['docs'][i]['episode'])
            similarity = str(data.json()['docs'][i]['similarity'])
            await bot.send(event, "番剧名：" + title + "\n" + "集数：" + episode + "\n" + "时间戳：" + time + "\n" + "准确率：" + similarity)
            # print(data.json()['docs'][i]['title_chinese'])
            # print(data.json()['docs'][i]['episode'])
        else:
            pass
    if anicount == 0:
        await bot.send(event,"搜不到，爬")