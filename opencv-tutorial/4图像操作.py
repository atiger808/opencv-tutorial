# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 20:48
# @Author   : Ole211
# @Site     : 
# @File     : 4图像操作.py    
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

img = cv.imread('lena.jpg', cv.IMREAD_COLOR)
# 现在我们可以引用实际的像素
px = img[50:100, 50:100]
# 下面我们可以实际修改像素
img[10:100, 50:100] = [255, 255, 255]
# 之后重新引用
px = img[55, 55]
print(px)

cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()