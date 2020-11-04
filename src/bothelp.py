from aiocqhttp import MessageSegment

async def bothelp(bot, event):
    await bot.send(event, 
                    "帮助指南" + "\n" + 
                    "搜番：发送“番剧”+图片" +  "\n" + 
                    "kaw日榜：发送“kaw日榜”" +  "\n" +
                    "pixel日/月/周榜：发送“来张日/月/周榜图”" +  "\n" +
                    "pixel男性向日榜：发送“男性向日榜”" +  "\n" +
                    "网抑云：发送“到点了”" +  "\n" + 
                    "epic本周白送游戏：发送“epic白嫖”" +  "\n" + 
                    "码农周刊：发送“码农周刊”")
