# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 2:29
# @Author   : Ole211
# @Site     : 
# @File     : canny算子.py
# @Software : PyCharm
import cv2
import os

os.chdir('d:\\img\\')

o = cv2.imread('road.jpg' ,cv2.IMREAD_GRAYSCALE)
r = cv2.Canny(o, 50, 150)
cv2.imshow('original', o)
cv2.imshow('result', r)
cv2.waitKey()
cv2.destroyAllWindows()