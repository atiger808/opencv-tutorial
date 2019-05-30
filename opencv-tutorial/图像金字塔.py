# _*_ coding: utf-8 _*_
# @Time     : 2019/3/4 21:15
# @Author   : Ole211
# @Site     : 
# @File     : 图像金字塔.py    
# @Software : PyCharm
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:\\img\\')

# 下采样
def pyramid_down_demo(img):
    # 迭代次数
    level = 3
    temp = img.copy()
    pyramid_down_imgs = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        pyramid_down_imgs.append(dst)
        cv2.imshow('pyramid_down:'+str(i), dst)
        temp = dst
    return pyramid_down_imgs

# 上采样
def pyramid_up_demo(img):
    pyramid_down_imgs  = pyramid_down_demo(img)
    level = len(pyramid_down_imgs)
    for i in range(level-1, -1, -1):
        if (i-1) < 0:
            expand = cv2.pyrUp(pyramid_down_imgs[i], dstsize=img.shape[:2])
            lpls = cv2.subtract(img, expand)
            cv2.imshow('pyramid_up_'+str(i), lpls)
        else:
            expand = cv2.pyrUp(pyramid_down_imgs[i], dstsize=pyramid_down_imgs[i-1].shape[:2])
            lpls = cv2.subtract(pyramid_down_imgs[i-1], expand)
            cv2.imshow('pyramid_up_'+str(i), lpls)

if __name__ == '__main__':
    img = cv2.imread('cat.png')
    cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
    pyramid_up_demo(img)

    cv2.waitKey()
    cv2.destroyAllWindows()