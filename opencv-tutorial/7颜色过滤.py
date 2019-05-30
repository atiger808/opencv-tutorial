# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 22:16
# @Author   : Ole211
# @Site     : 
# @File     : 7颜色过滤.py
# @Software : PyCharm
'''
我们首先把帧转换成HSV， 接下来我们为红色指定一些HSV值。
我们使用inRange函数， 为我们特定范围的创建掩膜。这是真或假，黑色或白色
接下来，我们通过执行按位操作来恢复我们的红色。基本上，我们显示了frame and mask.
掩膜的白色部分是红色范围， 被转换为纯白色，而其他一切都变成黑色。
最后我们展示所有东西。我选择了显示原始真， 掩膜和最终结果。
在下一个教程中， 我们将对这个主题做一些介绍， 我们这里还是有些噪音。
东西有颗粒感， 红色中的黑点多， 还有许多其他的小色点， 我们可以
通过模糊和平滑来缓解这个问题。
'''



import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out_res = cv.VideoWriter('color-filter-res.mp4', fourcc, 20.0, (640, 480),)
out_frame = cv.VideoWriter('color-filter-frame.mp4', fourcc, 20.0, (640, 480),)
out_mask = cv.VideoWriter('color-filter-mask.mp4', fourcc, 20.0, (640, 480),)

while(1):
    ret, frame = cap.read()
    # BGR格式转换为HSV 格式
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_red = np.array([30, 150, 50])
    upper_red = np.array([255, 255, 180])
    mask = cv.inRange(hsv, lower_red, upper_red)

    # BGR转灰度图
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 直接阈值二值化
    # ret, threshold = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
    # 自适应阈值
    # threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
    # cv.imshow('threshold', threshold)

    # 边缘检测
    # laplacian算子
    # laplacian = cv.Laplacian(frame, cv.CV_64F)
    # cv.imshow('laplacian', laplacian)

    # Canny算子边缘检测
    edges = cv.Canny(gray, 100, 200)
    cv.imshow('canny', edges)

    res = cv.bitwise_and(frame, frame, mask=mask)
    res_inv = cv.bitwise_not(res)
    cv.imshow('res', res)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)

    out_res.write(res)
    out_frame.write(frame)
    out_mask.write(mask)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()