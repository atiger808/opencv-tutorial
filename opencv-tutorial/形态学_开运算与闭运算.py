# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 3:58
# @Author   : Ole211
# @Site     : 
# @File     : 形态学_开运算与闭运算.py.py    
# @Software : PyCharm
import cv2
import os
import numpy as np
os.chdir('d:\\img\\')

o = cv2.imread('demo.png', cv2.IMREAD_UNCHANGED)
k = np.ones((6,6), np.uint8)
# 开运算
r = cv2.morphologyEx(o, cv2.MORPH_OPEN, k)
rr = cv2.morphologyEx(o, cv2.MORPH_CLOSE, k)
cv2.imshow('original', o)
cv2.imshow('open', r)
cv2.imshow('close', rr)
cv2.waitKey()
cv2.destroyAllWindows()