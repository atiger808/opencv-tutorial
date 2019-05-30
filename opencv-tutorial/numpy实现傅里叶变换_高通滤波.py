# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 1:12
# @Author   : Ole211
# @Site     : 
# @File     : numpy实现傅里叶变换_高通滤波.py    
# @Software : PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:\\img\\')

o = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)
f = np.fft.fft2(o)
fshift = np.fft.fftshift(f)
w, h = o.shape
crow, ccol = int(w/2), int(h/2)
fshift[crow-50:crow+50, ccol-50:ccol+50] = 0

ifshift = np.fft.ifftshift(fshift)
io = np.fft.ifft2(ifshift)
io = np.abs(io)
diff = io-o

plt.subplot(221)
plt.imshow(o, cmap='gray')
plt.subplot(222)
plt.imshow(io, cmap='gray')
plt.subplot(223)
plt.imshow(io)
plt.subplot(224)
plt.imshow(diff, cmap='gray')
plt.show()
print(fshift)