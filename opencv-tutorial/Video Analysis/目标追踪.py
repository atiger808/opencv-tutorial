# _*_ coding: utf-8 _*_
# @Time     : 2019/9/17 14:36
# @Author   : Ole211
# @Site     : 
# @File     : 目标追踪.py    
# @Software : PyCharm

import cv2
import numpy as np

img = cv2.imread('d:\\img\\bird.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 30, 0.01, 10)
corners = np.int0(corners)
print(len(corners))
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()