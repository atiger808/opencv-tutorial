# _*_ coding: utf-8 _*_
# @Time     : 2019/3/21 14:41
# @Author   : Ole211
# @Site     : 
# @File     : paper_detect.py    
# @Software : PyCharm

import cv2
import numpy as np
import os
os.chdir('d:\\img\\')

img = cv2.imread('paper.png')
meanShift_img = cv2.pyrMeanShiftFiltering(img, 25, 10)


cv2.imshow('MeanShift', meanShift_img)
cv2.imshow('original', img)
cv2.waitKey()
cv2.destroyAllWindows()