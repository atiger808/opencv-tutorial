# _*_ coding: utf-8 _*_
# @Time     : 2019/3/4 20:35
# @Author   : Ole211
# @Site     : 
# @File     : 物体追踪.py    
# @Software : PyCharm
'''
读取图像， 获取BGR格式的像素值， 然后转换乘hsv格式， 再利用inRange函数进行
颜色分离， 标记出来

HSV的颜色取值范围
H： Hue通道， 色调， 颜色种类
S： Saturation 饱和度， 颜色浓淡
V:  Value 明亮度， 颜色明亮度
H: 0-180
S: 0-255
V: 0-255
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('e:\\MP4\\')

cap = cv2.VideoCapture('vtest.avi')
while(1):
    ret, frame = cap.read()
    # 把每一帧的图像转换成hsv格式
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 确定颜色空间
    lower_hsv = np.array([11, 43, 46])
    upper_hsv = np.array([25, 255, 255])

    # 进行颜色分离
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    # 在图像上标记
    dst = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('video', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()