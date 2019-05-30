# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 0:16
# @Author   : Ole211
# @Site     : 
# @File     : 使用掩膜构建直方图.py    
# @Software : PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:\\img\\')

o = cv2.imread('r.bmp', cv2.IMREAD_GRAYSCALE)
mask = np.zeros(o.shape, np.uint8)
mask[200:300, 200:300] = 255
histMI = cv2.calcHist([o], [0], mask, [256], [0, 255])
histO = cv2.calcHist([o], [0], None, [256], [0,255])

cv2.imshow('o', o)
cv2.imshow('mask', mask*o)
# plt.subplot(121)
# plt.plot(histO)
# plt.title('original')
# plt.subplot(122)
# plt.plot(histMI)
# plt.show()
cv2.waitKey()
cv2.destroyAllWindows()