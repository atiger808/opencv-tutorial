# _*_ coding: utf-8 _*_
# @Time     : 2019/9/3 20:10
# @Author   : Ole211
# @Site     : 
# @File     : 20轮廓检测.py    
# @Software : PyCharm

import cv2
import numpy as np


img = cv2.imread('d:\\img\\bird.jpg')
blur = cv2.medianBlur(img, 5)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

edges = cv2.Canny(gray, 50, 150)
cv2.imshow('edges', edges)

ret, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh', thresh)
'''
cv2.findContours()函数
第一个参数是寻找轮廓的图像；

第二个参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
    cv2.RETR_EXTERNAL表示只检测外轮廓
    cv2.RETR_LIST检测的轮廓不建立等级关系
    cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
    cv2.RETR_TREE建立一个等级树结构的轮廓。

第三个参数method为轮廓的近似办法
    cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
    cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
    cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
'''
cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
'''
cv2.drawContours()函数
cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]])  
第一个参数是指明在哪幅图像上绘制轮廓；
第二个参数是轮廓本身，在Python中是一个list。
第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓。后面的参数很简单。其中thickness表明轮廓线的宽度，
如果是-1（cv2.FILLED），则为填充模式。绘制参数将在以后独立详细介绍。
'''
cnts_sort = sorted(cnts, key=lambda x: cv2.contourArea(x), reverse=True)
cv2.drawContours(img, cnts, -1, (0, 0, 255), 2)

'''
x, y, w, h = cv2.boundingRect(img)   
    参数：
    img  是一个二值图
    x，y 是矩阵左上点的坐标，
    w，h 是矩阵的宽和高

cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    img：       原图
    (x，y）：   矩阵的左上点坐标
    (x+w，y+h)：是矩阵的右下点坐标
    (0,255,0)： 是画线对应的rgb颜色
    2：         线宽
'''
x, y, w, h = cv2.boundingRect(cnts_sort[0])
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

'''
4 获取物体最小外界矩阵
使用 cv2.minAreaRect(cnt) ，返回点集cnt的最小外接矩形，cnt是所要求最小外接矩形的点集数组或向量，这个点集不定个数。
其中：cnt = np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4]]) # 必须是array数组的形式

rect = cv2.minAreaRect(cnt) # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
box = np.int0(cv2.boxPoints(rect)) #通过box画出矩形框
'''
# 最小外接矩形
rect = cv2.minAreaRect(cnts_sort[0])
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# 最小外接圆
(x, y), radius = cv2.minEnclosingCircle(cnts_sort[2])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(img, center, radius, (0, 255, 0), 4)

# 最小外接椭圆
ellipse = cv2.fitEllipse(cnts_sort[1])
cv2.ellipse(img, ellipse, (0, 255, 0), 4)

# 拟合直线
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnts_sort[4], cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) +y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img, (cols-1, righty), (0, lefty), (0, 255, 0), 4)


cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
