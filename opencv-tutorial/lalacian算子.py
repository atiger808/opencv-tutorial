# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 2:21
# @Author   : Ole211
# @Site     : 
# @File     : lalacian算子.py    
# @Software : PyCharm
import cv2
import os
os.chdir('d:\\img\\')

o = cv2.imread('demo.png', cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(o, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
cv2.imshow('original', o)
cv2.imshow('laplacian', laplacian)
cv2.waitKey()
cv2.destroyAllWindows()