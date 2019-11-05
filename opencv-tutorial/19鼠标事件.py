# _*_ coding: utf-8 _*_
# @Time     : 2019/8/15 15:39
# @Author   : Ole211
# @Site     : 
# @File     : 19鼠标事件.py    
# @Software : PyCharm
'''
鼠标事件：
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON',
'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY',
'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP',
'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP',
'EVENT_MOUSEHWHEEL', 'EVENT_MOUSEMOVE', 'EVENT_MOUSEWHEEL',
'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
'''
import cv2
import os
import time
import numpy as np
os.chdir('d:\\img\\')

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# mouse callback function

# def draw_circle(envent, x, y, flags, param):
#     # cv2.EVENT_LBUTTONDBLCLK 左键双击
#     if envent == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
#
# # 创建图像与窗口，并将窗口与回调函数绑定
# img = np.zeros((500, 500, 3), np.uint8)
# cv2.namedWindow('image')
# cv2.setMouseCallback('image', draw_circle)
#
# while(1):
#     cv2.imshow('image', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cv2.destroyAllWindows()


# 当鼠标按下时为True
drawing = False
# 如果mode为True是绘制矩形， 按下'm'变成绘制曲线
mode = True
ix, iy = -1, -1

# 创建回调函数
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                print(x, y)
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing == False

# 下面将回调函数与OpenCV窗口绑定一起，在主循环中将'm'键与模式转换绑定一起
# img = np.zeros((500, 500, 3), np.uint8)
img = cv2.imread('card01.jpg')
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if k == ord('m'):
        mode = not mode
    elif k == ord('s'):
        mode = 's'
    elif k == ord('q'):
        break
cv2.destroyAllWindows()