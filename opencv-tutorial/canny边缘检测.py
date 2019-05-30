# _*_ coding: utf-8 _*_
# @Time     : 2019/3/4 21:45
# @Author   : Ole211
# @Site     : 
# @File     : canny边缘检测.py    
# @Software : PyCharm

'''
Canny 边缘检测步骤：
1， 消除噪声， 使用高斯平滑滤波器卷积降噪， GaussianBlur
2， 灰度转换   cvtColor
3,  计算梯度   Sobel /  Scharr
4， 非最大信号抑制。细化幅值图像中的屋脊带， 即只保留局部变化的点
5， 高低阈值输出二值图像
    高低阈值比例一般为2， 3
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:\\img\\')

def edge_detect(img):
    # 第一步 斯模糊， 取出噪声
    blurred = cv2.GaussianBlur(img, (3, 3), 0)
    # 第二步 转换为灰度图
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    # 第三步 计算梯度
    grad_x =cv2.Sobel(gray, cv2.CV_16S, 1, 0)
    grad_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1)
    # 第四步， 第五步 T2: T1 = 3: 1
    edge_output = cv2.Canny(grad_x, grad_y, 10, 150)
    cv2.imshow('Canny edge', edge_output)

    # 将二值边缘转换成彩色边缘
    dst = cv2.bitwise_and(img, img, mask=edge_output)
    cv2.imshow('Color edge', dst)

if __name__ == '__main__':
    img = cv2.imread('leaf.jpg')
    edge_detect(img)
    cv2.waitKey()
    cv2.destroyAllWindows()