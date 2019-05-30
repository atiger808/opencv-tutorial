# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 20:42
# @Author   : Ole211
# @Site     :
# @File     : change_colorspaces.py
# @Software : PyCharm

import cv2
import numpy as np
import os
os.chdir('d:\\img\\')

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

# BGR转HSV
green = np.uint8([[[0, 255, 0]]])
blue = np.uint8([[[255, 0, 0]]])
red = np.uint8([[[0, 0, 255]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
print('hsv_blue: ', hsv_blue)
print('hsv_green: ', hsv_green)
print('hsv_red: ', hsv_red)

# Object Tracking 目标跟踪
cap = cv2.VideoCapture(0)
while(1):
    # 取每一帧
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义蓝色的范围
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 阈值使图像只得到蓝色
    mask  = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_not(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF == ord('q')
    if k:
        break

cv2.destroyAllWindows()