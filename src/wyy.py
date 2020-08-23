import requests
async def wyy(bot, event):
    data = requests.get(url="https://nd.2890.ltd/api/?format=text")
    if data.status_code == 502 or data.status_code == 520:
        await bot.send(event, "网抑云裂开啦！")
    elif data.status_code == 200:
        await bot.send(event, data.text)