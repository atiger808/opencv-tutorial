# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 1:52
# @Author   : Ole211
# @Site     : 
# @File     : sobel算子.py    
# @Software : PyCharm
import cv2
import os
os.chdir('d:\\img\\')
o = cv2.imread('demo.png', cv2.IMREAD_GRAYSCALE)
dx = cv2.Sobel(o, cv2.CV_64F, 1, 0)
dx = cv2.convertScaleAbs(dx)
dy = cv2.Sobel(o, cv2.CV_64F, 0, 1)
dy = cv2.convertScaleAbs(dy)
dst = cv2.addWeighted(dx, 0.5, dy, 0.5, 0)
cv2.imshow('original', o)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()