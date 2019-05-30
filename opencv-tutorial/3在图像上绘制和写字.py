# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 20:30
# @Author   : Ole211
# @Site     : 
# @File     : 3在图像上绘制和写字.py
# @Software : PyCharm
import os
import cv2 as cv
import numpy as np
os.chdir('d:\\img\\')

img = cv.imread('demo.png', cv.IMREAD_COLOR)
# 绘制直线
cv.line(img, (0, 0), (300, 150), (255, 255, 255), 5)
# 绘制矩形
cv.rectangle(img, (10, 10), (200, 200), (0, 0, 255), 2)
# 绘制圆
cv.circle(img, (300, 300), 100, (0, 255, 0), -1)
# 绘制多边形
pts = np.array([[10, 5], [20, 30], [100, 50], [50,10], [200, 200]], np.int32)
pts2 = np.array([[0, 300], [50, 300], [60, 350], [40, 400], [30, 330]], np.int32)
pts2 = pts2.reshape((-1, 1, 2))
pts = pts.reshape((-1, 1, 2))
# 第三个参数为True, 则为闭合线段
cv.polylines(img, [pts], False, (0, 255, 255), 2)
cv.polylines(img, [pts2], True, (0, 255, 255), 2)
print(pts)

# 图像上写字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (0, 130), font, 1, (200, 255, 155), 2, cv.LINE_AA)

cv.imshow('img', img)

cv.waitKey()
cv.destroyAllWindows()
