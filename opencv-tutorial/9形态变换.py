# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 23:01
# @Author   : Ole211
# @Site     : 
# @File     : 9形态变换.py    
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

color = cv.imread('color1.jpg')


cap = cv.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    # hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #
    # lower_red = np.array([30, 150, 50])
    # upper_red = np.array([255, 255, 180])
    #
    # mask = cv.inRange(hsv, lower_red, upper_red)
    # res = cv.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (15, 15), 0)
    gray = cv.equalizeHist(gray)
    ret, thresh = cv.threshold(gray, 60, 255, cv.THRESH_BINARY_INV)
    thresh = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)
    # thresh = cv.dilate(thresh, kernel, iterations=1)
    # thresh = cv.erode(thresh, kernel, iterations=1)

    # 背景置换
    mask = thresh
    mask_inv = cv.bitwise_not(mask)
    roi = color[0:480, 0:640]
    img_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
    img_fg = cv.bitwise_and(frame, frame, mask=mask)
    dst = cv.add(img_bg, img_fg)
    cv.imshow('dst', dst)
    cv.imshow('dst1', cv.bitwise_and(img_bg, img_bg, mask=mask_inv))

    # # 腐蚀操作
    # erosion = cv.erode(mask, kernel, iterations=1)
    # cv.imshow('erosion', erosion)
    #
    # # 膨胀操作
    # dilation = cv.dilate(mask, kernel, iterations=1)
    # cv.imshow('dilation', dilation)
    #
    # # 开操作
    # opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    # cv.imshow('opening', opening)
    #
    # 闭操作
    closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    cv.imshow('closing', closing)

    cv.imshow('original', frame)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
