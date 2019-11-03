# _*_ coding: utf-8 _*_
# @Time     : 2019/8/30 23:02
# @Author   : Ole211
# @Site     : 
# @File     : itchat爬取微信好友信息.py    
# @Software : PyCharm

from wxpy import Bot, embed

bot = Bot(cache_path=True)
embed()
friends = bot.friends()
print(type(friends))
print(len(friends))