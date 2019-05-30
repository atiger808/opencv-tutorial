# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 21:48
# @Author   : Ole211
# @Site     : 
# @File     : 6阈值.py    
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

img = cv.imread('me.jpg')

# 直接阈值
ret, binary = cv.threshold(img, 12, 255, cv.THRESH_BINARY)
cv.imshow('img', img)
cv.imshow('binary', binary)

# 灰度化图像， 然后使用阈值
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# 直方图均值化
hist_img = cv.equalizeHist(gray)
cv.imshow('hist_img', hist_img)

# 高斯模糊
# hist_img = cv.GaussianBlur(hist_img, (21, 21), 0)
# cv.imshow('Gaussian', hist_img)

# 中值模糊
hist_img = cv.medianBlur(hist_img, 21)
cv.imshow('median', hist_img)

# 二值化
ret2, binary2 = cv.threshold(hist_img, 10, 255, cv.THRESH_BINARY)
cv.imshow('binary2', binary2)

# 自适应阈值
th = cv.adaptiveThreshold(hist_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
cv.imshow('Adaptive threshold', th)

# 大津阈值
ret, binary3 = cv.threshold(hist_img, 125, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow('Otsu', binary3)

cv.waitKey()
cv.destroyAllWindows()