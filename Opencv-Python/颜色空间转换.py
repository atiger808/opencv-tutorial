# _*_ coding: utf-8 _*_
# @Time     : 2019/3/20 21:43
# @Author   : Ole211
# @Site     : 
# @File     : 颜色空间转换.py    
# @Software : PyCharm

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # 获取每一帧
    ret, frame = cap.read()
    # 转换到hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 设置蓝色阈值
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # 根据阈值构建掩膜
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # 对原图和掩膜进行运算
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()