# _*_ coding: utf-8 _*_
# @Time     : 2019/3/4 22:53
# @Author   : Ole211
# @Site     : 
# @File     : 霍夫变换圆检测.py    
# @Software : PyCharm

'''
霍夫变换圆检测步骤
1，执行均值偏移滤波，消除噪声
2，转换成灰度图
3，canny边缘检测
4，执行霍夫圆检测
5，绘制出检测到的圆
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:\\img\\')

def Hough_circle_detect(img):
    # 均值偏移滤波
    dst = cv2.pyrMeanShiftFiltering(img, 10, 120)
    cv2.imshow('filter', dst)
    # 转换成灰度
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    # Canny边缘检测
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    cv2.imshow('canny', edges)
    # 霍夫圆检测
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    # 绘制出检测出的圆
    for i in circles[0,:]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 1)
        cv2.circle(img, (i[0], i[1]), 2, (0, 255, 0), 2)
    cv2.imshow('circles', img)

if __name__ == '__main__':
    img = cv2.imread('water_coins.jpg')
    cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('img', img)
    Hough_circle_detect(img)

    cv2.waitKey()
    cv2.destroyAllWindows()