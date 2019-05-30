# _*_ coding: utf-8 _*_
# @Time     : 2019/3/27 23:40
# @Author   : Ole211
# @Site     : 
# @File     : 平滑图像.py    
# @Software : PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:\\img\\')

img = cv2.imread('lena.jpg')

kernel = np.ones((5, 5), np.float32)/25
kernel2 = np.ones((3, 3), np.int32)/9
dst = cv2.filter2D(img, -1, kernel2)

# 图像模糊（图像平滑）
blur = cv2.blur(img, (5, 5))
cv2.imshow('blur', blur)

# 高斯过滤
gaussian = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('Gaussian', gaussian)

# 中间值过滤
median = cv2.medianBlur(img, 11)
cv2.imshow('median', median)

# 双边过滤
bilate = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('bilate', bilate)

cv2.imshow('dst', dst)
cv2.imshow('original', img)
cv2.waitKey()
cv2.destroyAllWindows()