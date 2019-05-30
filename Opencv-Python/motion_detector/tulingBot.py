# _*_ coding: utf-8 _*_
# @Time     : 2019/4/26 16:52
# @Author   : Ole211
# @Site     : 
# @File     : tulingBot.py    
# @Software : PyCharm

from wxpy import Bot, Tuling, embed, ensure_one
import os
import time

bot = Bot(cache_path=True)

def send_msg(filename, record_screenshot):
    try:
        my_friend = bot.friends().search(u'道法自然')[0]
        warningTime = os.path.splitext(os.path.split(filename)[-1])[0]
        print('---waring--', warningTime)

        # 发送文本
        my_friend.send(f'{warningTime}')

        # 发送截图
        my_friend.send_image(filename)

        # 发送视频
        # if record_screenshot:
        #     print('文件名--', record_screenshot[-1])
        #     my_friend.send_video('./record/' + record_screenshot[-1] + '.mp4')
    except Exception as e:
        print(e)
        pass

if __name__ == '__main__':
    pass
    # send_msg('./image/2019-04-26 17-21-27.jpg')
