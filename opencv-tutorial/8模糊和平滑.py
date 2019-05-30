# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 22:59
# @Author   : Ole211
# @Site     : 
# @File     : 8模糊和平滑.py    
# @Software : PyCharm


import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

cap = cv.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])
    mask = cv.inRange(hsv, lower_red, upper_red)

    res = cv.bitwise_and(frame, frame, mask=mask)
    # cv.imshow('res', res)

    # 使用一个简单的平滑，牺牲了很多粒度
    # kernel = np.ones((15, 15), np.float32)/225
    # smoothed = cv.filter2D(res, -1, kernel)
    # cv.imshow('smoothed', smoothed)

    # 使用高斯模糊
    # blur = cv.GaussianBlur(res, (15, 15), 0)
    # cv.imshow('Gaussianblur', blur)

    # 中值模糊
    # median = cv.medianBlur(res, 15)
    # cv.imshow('Median Blur', median)

    # 双向模糊
    bilateral = cv.bilateralFilter(res, 15, 75, 75)
    cv.imshow('bilateralBlur', bilateral)

.
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()