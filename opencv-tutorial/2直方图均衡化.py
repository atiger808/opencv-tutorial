# _*_ coding: utf-8 _*_
# @Time     : 2019/3/2 22:51
# @Author   : Ole211
# @Site     : 
# @File     : 2直方图均衡化.py    
# @Software : PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir('d:\\img\\')

o = cv2.imread('result.jpg', cv2.IMREAD_GRAYSCALE)
o_hist = cv2.equalizeHist(o)
cv2.imshow('original',o)
cv2.imshow('o_hist',o_hist)
cv2.waitKey()
cv2.destroyAllWindows()