# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 0:32
# @Author   : Ole211
# @Site     :
# @File     : numpy实现傅里叶变换.py
# @Software : PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('d:\\img\\')

o = cv2.imread('lena.jpg', 0)
# 傅里叶变换
f = np.fft.fft2(o)
fshift = np.fft.fftshift(f)
result = 20*np.log(np.abs(fshift))
plt.subplot(121)
plt.imshow(o, cmap='gray')
plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.show()