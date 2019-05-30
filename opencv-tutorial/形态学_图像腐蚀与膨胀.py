# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 3:37
# @Author   : Ole211
# @Site     : 
# @File     : 形态学_图像腐蚀与膨胀.py
# @Software : PyCharm
import cv2
import numpy as np
import os
os.chdir('d:\\img\\')

o = cv2.imread('demo.png')
kernel = np.ones((5, 5), np.uint8)
# 腐蚀操作
erode = cv2.erode(o, kernel, 2)
# 膨化操作
dilate = cv2.dilate(erode, kernel, 2)

cv2.imshow('original', o)
cv2.imshow('erode', erode)
cv2.imshow('dilate', dilate)
cv2.waitKey()
cv2.destroyAllWindows()