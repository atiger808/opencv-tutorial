# _*_ coding: utf-8 _*_
# @Time     : 2019/4/23 23:02
# @Author   : Ole211
# @Site     : 
# @File     : 15分水岭算法.py    
# @Software : PyCharm

import cv2
import numpy as np
import os
os.chdir('d:\\img\\')

def watershed(src):
    # h, w= src.shape[:2]
    # src = cv2.resize(src, (int(w // 2), int(h // 2)))
    blured = cv2.pyrMeanShiftFiltering(src, 10, 100)
    gray = cv2.cvtColor(blured, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)


    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=1)
    binary = cv2.dilate(binary, kernel, iterations=1)

    dist = cv2.distanceTransform(binary, cv2.DIST_L2, 3)
    dist_output = cv2.normalize(dist, 0, 1.0, cv2.NORM_MINMAX)
    cv2.imshow('distance-t', dist_output*255)
    print(dist_output)
    print(dist.max())

    ret, surface = cv2.threshold(dist, dist.max()*0.8, 255, cv2.THRESH_BINARY)
    cv2.imshow('surface-bin', surface)

    surface_fg = np.uint8(surface)
    unknown = cv2.subtract(binary, surface_fg)
    ret, markers = cv2.connectedComponents(surface_fg)
    print(ret)

    markers = markers + 1
    markers[unknown==255] = 0
    markers = cv2.watershed(src, markers=markers)
    src[markers==-1] = [0, 255, 255]


    cv2.imshow('binary', binary)
    cv2.imshow('original', src)
    cv2.imshow('blur', blured)

src = cv2.imread('water_coins.jpg')
watershed(src)
cv2.waitKey()
cv2.destroyAllWindows()