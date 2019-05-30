# _*_ coding: utf-8 _*_
# @Time     : 2019/3/2 23:42
# @Author   : Ole211
# @Site     : 
# @File     : 通道的拆分合并.py    
# @Software : PyCharm
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir('d:\\img\\')

img = cv2.imread('lena.jpg')
b, g, r = cv2.split(img)
r = cv2.merge([r, g, b])
cv2.imshow('origial', img)
cv2.imshow('hist', r)
cv2.waitKey()

cv2.destroyAllWindows()