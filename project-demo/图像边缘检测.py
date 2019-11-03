# _*_ coding: utf-8 _*_
# @Time     : 2019/8/31 11:04
# @Author   : Ole211
# @Site     : 
# @File     : 图像边缘检测.py    
# @Software : PyCharm

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import os

def nothing(x):
    pass

root = tk.Tk()
root.withdraw()
filename = filedialog.askopenfilename()
o = cv2.imread(filename, 0)
im = cv2.GaussianBlur(o, (3, 3), 0)

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.createTrackbar('minVal', 'img', 0, 255, nothing)
cv2.createTrackbar('maxVal', 'img', 0, 255, nothing)
while 1:
    minval = cv2.getTrackbarPos('minVal', 'img')
    maxval = cv2.getTrackbarPos('maxVal', 'img')
    edge = cv2.Canny(o, minval, maxval)

    dst = np.hstack((o, edge))
    cv2.imshow('img', dst)
    k = cv2.waitKey() & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()