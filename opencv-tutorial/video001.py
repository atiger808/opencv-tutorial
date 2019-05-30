# _*_ coding: utf-8 _*_
# @Time     : 2019/3/2 23:13
# @Author   : Ole211
# @Site     : 
# @File  i   : video001.py
# @Software : PyCharm

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    # 读物视频中的每一帧
    ret, frame = cap.read()
    # 将图片从RGB空间转到BRG空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义在hsv空间中蓝色的范围
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 根据以上定义的蓝色的阈值得到蓝色的部分
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()