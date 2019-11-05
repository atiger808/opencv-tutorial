# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 20:58
# @Author   : Ole211
# @Site     : 
# @File     : 5图像算数和逻辑运算.py    
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

# 载入两张图片
base_img = cv.imread('img2.jpg')
print(base_img.shape)
logo_img = cv.imread('logo.jpg')
# 把logo图片放在img2图片左上角， 因此需要创建一个区域
rows, cols, channels = logo_img.shape
roi = base_img[0:rows, 0:cols]
# 现在创建了一个logo的罩子， 再创建一个与他相反的罩子
img2gray = cv.cvtColor(logo_img, cv.COLOR_BGR2GRAY)
# 二值化
ret,mask  = cv.threshold(img2gray, 220, 255, cv.THRESH_BINARY_INV)
cv.imshow('mask_', mask)

# 按位运算
mask_inv = cv.bitwise_not(mask)
img1_bg = cv.bitwise_and(roi,  roi, mask=mask_inv)
img2_fg = cv.bitwise_and(logo_img, logo_img, mask=mask)

# 图像加法
dst = cv.add(img1_bg, img2_fg)
base_img[0:rows, 0:cols] = dst
cv.imwrite('img2_add_logo.jpg', base_img)
cv.imshow('dst', dst)

# 图像混合
im1 = cv.imread('circle.jpg')
im2 = cv.imread('hh3.jpg')
complx_dst = cv.addWeighted(im1, 0.4, im2, 0.7, 0)
cv.imshow('complx', complx_dst)

cv.imshow('base_img', base_img)
cv.imshow('mask_inv', mask_inv)
cv.imshow('mask', mask)

print(logo_img.shape)

cv.waitKey()
cv.destroyAllWindows()