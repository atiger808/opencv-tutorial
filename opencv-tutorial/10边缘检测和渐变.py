# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 23:25
# @Author   : Ole211
# @Site     : 
# @File     : 10边缘检测和渐变.py    
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

    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.GaussianBlur(frame, (15, 15), 0)
    frame = cv.equalizeHist(frame)
    ret, frame = cv.threshold(frame, 60, 255, cv.THRESH_BINARY)
    # laplacian算子，边缘检测
    laplacian = cv.Laplacian(frame, cv.CV_64F)
    # sobel算子
    sobelx = cv.Sobel(frame, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(frame, cv.CV_64F, 0, 1, ksize=5)
    cv.imshow('origunal', frame)
    cv.imshow('mask', mask)
    cv.imshow('laplacian', laplacian)
    cv.imshow('sobelx', sobelx)
    cv.imshow('sobely', sobely)

    # Canny算子，边缘检测
    edges = cv.Canny(frame, 100, 200)
    cv.imshow('Canny edges', edges)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()