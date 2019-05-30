# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 16:29
# @Author   : Ole211
# @Site     : 
# @File     : tree.py    
# @Software : PyCharm
import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
os.chdir('d:\\img\\')

img = cv2.imread('tree.jpg')
cv2.imshow('tree', img)
print('Image type: ', type(img), 'Image Dimension: ', img.shape)
img_copy = img.copy()
im_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)

# 定义颜色阈值
lower_blue = np.array([0, 0, 100])
upper_blue = np.array([120, 100, 255])

# 创建一个Mask
mask = cv2.inRange(img_copy, lower_blue, upper_blue)
plt.imshow(mask, cmap='gray')
plt.show()

masked_img = img_copy.copy()
masked_img[mask != 0] = [0, 0, 0]
plt.imshow(masked_img)

# cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()