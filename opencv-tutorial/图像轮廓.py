# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 2:39
# @Author   : Ole211
# @Site     :
# @File     : 图像轮廓.py
# @Software : PyCharm
import cv2
import numpy as np
import os

os.chdir('d:\\img\\')

o = cv2.imread('demo.png')
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
binary = cv2.dilate(binary, kernel=np.ones((5, 5), np.uint8), iterations=2)
binary = cv2.erode(binary, kernel=np.ones((5, 5), np.uint8), iterations=2)
# binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel=np.ones((5, 5), np.uint8))
image, contour, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour = sorted(contour, key=lambda x:cv2.contourArea(x), reverse=True)

co = o.copy()
r = cv2.drawContours(co, contour[:2], -1, (255, 0, 0), -1)
cv2.imshow('original', o)
cv2.imshow('result', r)
cv2.waitKey()
cv2.destroyAllWindows()