# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 18:29
# @Author   : Ole211
# @Site     : 
# @File     : bitwise_and.py    
# @Software : PyCharm

import cv2
import os
import numpy as np
os.chdir('d:\\img\\')

img1 = cv2.imread('cat.png')
img2 = cv2.imread('game.jpg')
print(img1.shape, img2.shape)

rows, cols, channels = img1.shape
roi = img2[0:rows, 0:cols]

img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

img1_fg = cv2.bitwise_and(img1, img1, mask=mask)

dst = cv2.add(img2_bg, img1_fg)
img2[0:rows, 0:cols] = dst

cv2.imshow('result', img2)
cv2.imwrite('game_cat.jpg', img2)
cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)
cv2.waitKey()
cv2.destroyAllWindows()