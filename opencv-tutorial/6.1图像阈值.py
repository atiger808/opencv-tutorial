# _*_ coding: utf-8 _*_
# @Time     : 2019/8/16 0:13
# @Author   : Ole211
# @Site     : 
# @File     : 6.1图像阈值.py    
# @Software : PyCharm

import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
os.chdir('d:\\img\\')

# 1.1 简单阈值
img = cv2.imread('sun.jpg')
ret,thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

title = ['original', 'binary', 'binary_inv', 'trunc', 'tozero', 'tozero_inv']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])
plt.show()


# 1.2 自适应阈值 cv2.adaptiveThreshold(), 参数：
# cv2.ADAPTIVE_THRESH_MEAN_C：阈值取相邻区域的平均值
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 阈值取相邻区域的加权和， 权重为一个高斯窗口
o = cv2.imread('lisa2.jpg', 0)
# 中值滤波
img = cv2.medianBlur(o, 5)
blur_2 = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(blur_2, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(blur_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(blur_2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
titles = ['original', 'medianBlur', 'threshold v=127', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [o,img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
plt.show()
# cv2.imshow('original', o)
# cv2.imshow('medianBlur', img)
# cv2.imshow('blur_2', blur_2)
# cv2.imshow('th1', th1)
# cv2.imshow('th2', th2)
# cv2.imshow('th3', th3)

# 1.3 Otsu 二值化
# 对一副双峰图像自动根据直方图计算出一个阈值
# 函数 cv2.threshold() flag:
# cv2.THRESH_OTSU
img = cv2.imread('result.jpg', 0)
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3
          ]
titles  = ['original', 'histogram', 'thresholding v=127',
            'original', 'histogram', 'otsu thresholding',
            'gaussian filter', 'histogram', 'otsu thresholding'
           ]
for i in range(3):
    plt.subplot(3, 3, i*3+1)
    plt.imshow(images[i*3])
    plt.title(titles[i*3])

    plt.subplot(3, 3, i*3+2)
    plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1])

    plt.subplot(3, 3, i*3+3)
    plt.imshow(images[i*3+2])
    plt.title(titles[i*3+2])
plt.show()
cv2.imshow('gaussian otsu threshold', th3)
cv2.waitKey()
cv2.destroyAllWindows()