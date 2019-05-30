# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 0:42
# @Author   : Ole211
# @Site     : 
# @File     : numpy实现傅里叶逆变换.py
# @Software : PyCharm
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
os.chdir('d:\\img\\')

o = cv2.imread('lena.jpg', 0)
# 傅里叶变换
f = np.fft.fft2(o)
fshift = np.fft.fftshift(f)
# 逆傅里叶变换
ifshift = np.fft.ifftshift(fshift)
io = np.fft.ifft2(ifshift)
io = np.abs(io)

plt.subplot(121)
plt.imshow(o, cmap='gray')
plt.title('original')
plt.subplot(122)
plt.imshow(io, cmap='gray')
plt.title('result')
plt.show()