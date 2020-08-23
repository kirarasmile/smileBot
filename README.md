# smileBot
## 简介
临时起意写的qqbot，使用go-cqhttp+aiocqhttp，主要功能为订阅rss获取资讯，自带图库目前懒得部署，写是写完了~有空再弄上去
## 功能
* 主体功能暂时都在群聊中使用
* 获取pixiv日/周/月/男性日榜，R18日榜暂时有点问题
* 获取epic的白嫖游戏表
* 获取kaw(Konachan Anime Wallpapers)日榜
* 网抑云time（该api无法在国外服务器访问）
* 获取最新的码农周刊link
## 使用组件
* <a href="https://aiocqhttp.nonebot.dev/#/">aiocqhttp</a>
* <a href="https://github.com/howmanybots/onebot/blob/master/README.md#/API">go-cqhttp</a>
## 部署须知
* 在config.py里填写信息
    * setuAPI暂时没启用所以不用理
    * 白名单按list形式填入群号(暂时也可以不用理，因为要白名单的功能暂时都挂了)
    * rsshub是你自己部署的rsshub服务的服务器域名，<a href="https://docs.rsshub.app/install/" >部署指南</a>
* 启动你的cqhttp服务
* 启动bot
    * pip install -r requitements.txt
    * 
        * 第一种，直接上
            * 将bot.py最后一行取消注释
            * python bot.py
        * 第二种
            * 安装uvicorn
            * uvicorn --host 0.0.0.0 --port 8080 bot:bot.asgi
                * 这里的8080以及bot.py最后一行那个注释的8080都是你的跟你cqhttp中的post_url端口一致
        * (其实我写了dockefile，那份dockerfile是能用的)

## todo
* <del>白名单</del>
* <del>网抑云</del>
* steam促销
* 接入setuAPI
* 历史上的今天
* <del>RSS读取</del>
* 修复R18日榜没反应问题
* 修复网抑云用不了的问题
* 搜图功能
* 缓存功能