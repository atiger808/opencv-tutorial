# _*_ coding: utf-8 _*_
# @Time     : 2019/9/17 23:54
# @Author   : Ole211
# @Site     : 
# @File     : 2.1直方图统计.py    
# @Software : PyCharm
'''
cv2.calcHist()的使用
定义
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate ]]) ->hist

images:输入的图像
channels:选择图像的通道
mask:掩膜，是一个大小和image一样的np数组，其中把需要处理的部分指定为1，不需要处理的部分指定为0，一般设置为None，表示处理整幅图像
histSize:使用多少个bin(柱子)，一般为256
ranges:像素值的范围，一般为[0,255]表示0~255
后面两个参数基本不用管。
注意，除了mask，其他四个参数都要带[]号。
'''
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('d:\\img\\bird.jpg')
colors = ['r', 'g', 'b']
for i in range(3):
    hist = cv2.calcHist([img], [i], None, [255], [0, 255])
    plt.plot(hist, color=colors[i])
    plt.title(colors[i])
    plt.show()

