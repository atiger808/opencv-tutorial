# _*_ coding: utf-8 _*_
# @Time     : 2019/3/20 20:52
# @Author   : Ole211
# @Site     : 
# @File     : opencv处理鼠标事件.py    
# @Software : PyCharm
import cv2
import numpy as np

'''
EVENT_FLAG_ALTKEY
EVENT_FLAG_CTRLKEY
EVENT_FLAG_LBUTTON
EVENT_FLAG_MBUTTON
EVENT_FLAG_RBUTTON
EVENT_FLAG_SHIFTKEY
EVENT_LBUTTONDBLCLK
EVENT_LBUTTONDOWN
EVENT_LBUTTONUP
EVENT_MBUTTONDBLCLK
EVENT_MBUTTONDOWN
EVENT_MBUTTONUP
EVENT_MOUSEHWHEEL
EVENT_MOUSEMOVE
EVENT_MOUSEWHEEL
EVENT_RBUTTONDBLCLK
EVENT_RBUTTONDOWN
EVENT_RBUTTONUP
'''
# 查看所有支持的鼠标事件
events = [i for i in dir(cv2) if 'EVENT' in i]
for e in events:
    print(e)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

# 创建图像与窗口并将窗口与回调函数绑定
img = np.zeros((500, 500, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()