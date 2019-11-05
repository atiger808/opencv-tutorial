# _*_ coding: utf-8 _*_
# @Time     : 2019/8/15 22:47
# @Author   : Ole211
# @Site     : 
# @File     : 18几何变换.py    
# @Software : PyCharm

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
os.chdir('D:\\img\\')

# 1.1 扩展缩放
img = cv2.imread('messi.jpg')
# 下面 None 本应该是输出的图像尺寸， 但是因为后边设置了缩放因子
# 因此这里设置为 None
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# or
# 这里直接设置输出图像的尺寸， 所以不用设置缩放因子
h, w = img.shape[:2]
res2 = cv2.resize(img, (2*w, 2*h), interpolation=cv2.INTER_CUBIC)
cv2.imshow('img', img)
cv2.imshow('res', res)
cv2.imshow('res2', res2)

# 1.2 平移

# 1.3 旋转， 构建旋转矩阵函数：cv2.getRotationMatrix2D()
rows, cols = img.shape[:2]
# 第一个参数为旋转中心
# 第二个参数为旋转角度
# 第三个参数为缩放因子
# 可以设置旋转中心，缩放因子，以及窗口大小来防止旋转 后超出边界的问题
M = cv2.getRotationMatrix2D((cols//2, rows//2), 45, 0.6)
dst = cv2.warpAffine(img, M, (2*cols, 1*rows))
cv2.imshow('dst3', dst)

# 1.4 仿射变换
# 在仿射变换中， 原图中所有的平行线在结果图像中同样平行， 为了创建这个矩阵我们
# 需要从原图中找到三个点，以及他们在输出图像中的位置。
# 然后用cv2.getAffineTransform()函数创建一个2*3的矩阵，
# 最后把这个矩阵传给函数cv2.warpAffine()
img = cv2.imread('paper_text.jpg')
rows, cols, ch = img.shape
pts1 = np.float32([[10, 100], [600, 3], [70, 400]])
pts2 = np.float32([[46, 75], [626, 47], [51, 351]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('dst4', dst)

# 1.5 透视变换
# 透视变换， 需要建立一个3*3变换矩阵。 在变换后直线还是直线
# 要构建这个变换矩阵， 需要在输入图像上找4个点， 以及他们在
# 输出图像对应的位置。这四个点的任意三个点不能共线。这个变化
# 矩阵由函数cv2.getPerspectiveTransform()构建。然后把这个矩阵
# 传给函数cv2.warpPerspective()
img = cv2.imread('road1.jpg')
rows, cols = img.shape[:2]
pts1 = np.float32([[421,319], [586, 319], [955, 400], [175, 400]])
pts2 = np.float32([[0, 0], [cols, 0], [cols, rows], [0, rows]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (cols, rows))
plt.subplot(121)
plt.imshow(img)
plt.title('input')
plt.subplot(122)
plt.imshow(dst)
plt.title('output')

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

