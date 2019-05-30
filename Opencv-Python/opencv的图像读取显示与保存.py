# _*_ coding: utf-8 _*_
# @Time     : 2019/3/15 11:50
# @Author   : Ole211
# @Site     : 
# @File     : opencv的图像读取显示与保存.py    
# @Software : PyCharm

import cv2 as cv
import os
os.chdir('d:\\img\\')
import numpy as np

'''
    1. cv2.imread(文件名， 标记) 读入图片
       cv2.IMREAD_COLOR(): 读入彩色图片
       cv2.IMREAD_GRAYSCALE(): 以灰度模式读入
    2. cv2.imshow() 显示图片
       cv2.waitKey() 等待键盘输入， 为毫秒级
       cv2.destroyAllWindows() 可以轻易删除任何我们建立的窗口， 
       括号内输入想删除的窗口名
       cv2.namedWindow('image', cv2.WINDOW_NORMAL)
       cv2.WINDOW_NORMAL 可以调整窗口大小
       cv2.WINDOW_AUTOSIZE 自动尺寸
'''

# 加载一个灰度图片， 显示图片， 按下s键保存后提出， 或者按下ESC键退出
# img = cv.imread('game.jpg', 0)
# cv.imshow('img', img)
# k = cv.waitKey(0) & 0xFF
# if k == 27:
#     cv.destroyAllWindows()
# elif k == ord('s'):
#     cv.imwrite('game.png', img)
#     print('save sucess')
#     cv.destroyAllWindows()

import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('demo.png', 0)
plt.imshow(img, cmap='gray', interpolation = 'bicubic')
# plt.xticks([])
# plt.yticks([])
plt.axis('off')
plt.show()