# _*_ coding: utf-8 _*_
# @Time     : 2019/3/6 0:30
# @Author   : Ole211
# @Site     : 
# @File     : 12GrabCut 前景提取.py    
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

'''
OpenCV提供了函数cv.grabCut()。
grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None)
img: 输入图像，必须是8位3通道图像，在处理过程中不会被修改
mask: 掩码图像，用来确定哪些区域是背景，前景，可能是背景，可能是前景等。
            GCD_BGD (=0), 背景； GCD_FGD (=1)，前景;GCD_PR_BGD (=2)，可能是背景;GCD_PR_FGD(=3)，可能是前景。
            如果没有手工标记GCD_BGD 或者GCD_FGD,那么结果只会有GCD_PR_BGD和GCD_PR_FGD
rect: 包含前景的矩形，格式为（x, y, w, h）
bdgModel,fgdModel: 算法内部使用的数组，只需要创建两个大小为（1，65），数据类型为np.float64的数组

iterCount: 算法迭代的次数
mode: 用来指示grabCut函数进行什么操作：
            cv.GC_INIT_WITH_RECT (=0)，用矩形窗初始化GrabCut；
            cv.GC_INIT_WITH_MASK (=1)，用掩码图像初始化GrabCut。

--------------------- 
作者：云net 
来源：CSDN 
原文：https://blog.csdn.net/qq_36387683/article/details/80509817 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''


img = cv.imread('messi.jpg')

# 转成rgb格式
b, g, r = cv.split(img)
img[:, :, 0] = r
img[:, :, 2] = b
print(img.shape)
cv.imshow('o', img)
mask = np.zeros(img.shape[:2], np.uint8)

bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)

w, h = img.shape[:2]
rect = (0, 0, w, h)
cv.grabCut(img, mask, rect, bgModel, fgModel, 5, cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]

cv.imshow('original', img)
cv.waitKey()
cv.destroyAllWindows()