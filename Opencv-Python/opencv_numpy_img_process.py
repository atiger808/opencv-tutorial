# _*_ coding: utf-8 _*_
# @Time     : 2019/4/14 11:43
# @Author   : Ole211
# @Site     : 
# @File     : opencv_numpy_img_process.py    
# @Software : PyCharm
import os
import numpy as np
import cv2
import random
import imageio

os.chdir('d:\\img\\')

img = cv2.imread('game.jpg')
print(img.shape)
low_pixel = img<20
if low_pixel.any() == True:
    print(low_pixel.shape)
img[low_pixel] = random.randint(200, 225)
w, h = img.shape[:2]
# 创建矢量
x, y = np.ogrid[:w, :h]
# 获取图像中心值
cen_x, cen_y = w/2, h/2
# 测量从中心到每个边界像素的距离
distance_from_the_center = np.sqrt((x - cen_x) ** 2 + (y - cen_y) ** 2)
# 选择半径值
radius = (h/2)
# 使用逻辑操作符 >
circular_img = distance_from_the_center>radius
# 给所有半径外的像素值分配零值， 即黑色
img[circular_img] = 0

cv2.imshow('original', img)
cv2.waitKey()
cv2.destroyAllWindows()