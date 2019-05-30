# _*_ coding: utf-8 _*_
# @Time     : 2019/3/4 22:08
# @Author   : Ole211
# @Site     : 
# @File     : 霍夫变换直线检测.py    
# @Software  : PyCharm

'''
实现霍夫变换直线检测的步骤
1， 灰度化   cv2.cvtColor(img, cv2.COLOR_BGR2GRAY
2， 二值化   cv2.threshold(img, cv2.THRESH_BINARY | cv2.THRESH_OTSU
3， Canny边缘检测  cv2.Canny(img, binary, 50, 150, apertureSize=3)
4， 霍夫直线检测  cv2.HoughLines(edges, 1, np.pi/180, 200)
OpenCV 支持两种不同的霍夫变换： 标准霍夫变换（SHT）， 和累计概率霍夫变换((PPHT)
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:\\img\\')

# 标准霍夫变换
def line_detection(o):

    img = o.copy()
    # 高斯迷糊， 取出噪声
    dst = cv2.GaussianBlur(img, (3, 3), 0)
    # 灰度化
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    # Canny边缘检测
    edges = cv2.Canny(binary, 50, 150, apertureSize=3)
    # 霍夫直线检测
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    # 在原图上标记
    for line in lines:
        print(line)
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow('original', o)
    cv2.imshow('image_lines', img)

# 累计概率霍夫变换
def line_detect_possible_demo(img):
    # 灰度化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('threshold', binary)
    # Canny边缘检测
    edges = cv2.Canny(binary, 50, 150, apertureSize=3)
    # 霍夫直线检测
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=10)
    # 咋原图上标记
    for line in lines:
        print(line)
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('line_detect_possible_demmo', img)


if __name__ == '__main__':
    img = cv2.imread('road.jpg')
    line_detection(img)
    line_detect_possible_demo(img)
    cv2.waitKey()
    cv2.destroyAllWindows()