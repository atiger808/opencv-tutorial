# _*_ coding: utf-8 _*_
# @Time     : 2019/3/2 23:51
# @Author   : Ole211
# @Site     : 
# @File     : 直方图统计.py
# @Software : PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('d:\\img\\')

o =cv2.imread('lena.jpg')
# 返回直方图统计
hist_b = cv2.calcHist([o], [0], None, [256], [0, 255])
hist_g = cv2.calcHist([o], [1], None, [256], [0, 255])
hist_r = cv2.calcHist([o], [2], None, [256], [0, 255])

plt.hist(o.ravel(), 256)
plt.figure()
plt.plot(hist_b, color='b')
plt.plot(hist_g, color='g')
plt.plot(hist_r, color='r')
plt.legend('equal')
plt.show()
cv2.imshow('o', o)
cv2.waitKey()
cv2.destroyAllWindows()