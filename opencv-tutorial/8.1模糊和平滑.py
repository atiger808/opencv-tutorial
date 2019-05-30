# _*_ coding: utf-8 _*_
# @Time     : 2019/4/23 16:27
# @Author   : Ole211
# @Site     : 
# @File     : 8.1模糊和平滑.py    
# @Software : PyCharm

import cv2
import numpy as np
import os
import random
os.chdir('d:\\img\\')

img = cv2.imread('game.jpg')
low_pix = img < 20
img[low_pix] = random.randint(200, 255)
cv2.imshow('origianl', img)

w, h = img.shape[:2]
center_x, center_y = w//2, h//2

x, y = np.ogrid[:w, :h]
distance_from_center = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

if h<w:
    radius = h//2
else:
    radius = w//2
circular_img = distance_from_center > radius
img[circular_img] = 0
cv2.imshow('dst', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 双向模糊
bilateral = cv2.bilateralFilter(img, 25, 75, 75)
cv2.imshow('bilaterL', bilateral)

cv2.waitKey()
cv2.destroyAllWindows()