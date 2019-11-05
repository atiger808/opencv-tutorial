# _*_ coding: utf-8 _*_
# @Time     : 2019/9/17 20:07
# @Author   : Ole211
# @Site     : 
# @File     : Contours More Functions.py
# @Software : PyCharm
'''
查找轮廓的不同特征，例如面积，周长，重心，边界框等

1.矩：cv.moments()
2.轮廓面积：cv.contourArea()
3.轮廓周长：cv.arcLength()
4.轮廓近似：cv.approxPolyDp()
5.边界矩形：cv.boundingRect()
6.最小外接矩形: cv.minAreaRect() cv.boxPoints()
7.最小外接圆:cv.minEnclosingCircle()
8.椭圆拟合:cv.ellipse()
9.直线拟合：cv.fitLine()
10.凸包检测：cv.convexHull()
11.凸包缺陷检测：cv.convexityDefects()
12.点到轮廓的距离：cv.pointPolygonTest()
13.两个轮廓比较：cv.matchShapes()
'''
import numpy as np
import cv2

img = cv2.imread('d:\\img\\img1\\star.png')
# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, thresh = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY)
# 获取轮廓
cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    cnt = cnts[0]
    # 1.图像的矩， 可以计算重心， 面积等， 返回一个字典
    M = cv2.moments(cnt)
    # 重心坐标
    cx = M['m10'] / M['m00']
    cy = M['m01'] / M['m00']
    cv2.circle(img, (np.int(cx), np.int(cy)), 10, (0, 0, 255), -1)
    # 2.面积
    area = cv2.contourArea(cnt)
    print('area:', area)
    # 3.周长
    perimeter = cv2.arcLength(cnt, True)
    # 4.轮廓近似
    epsilon = 0.001 * perimeter
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.polylines(img, [approx], True, (0, 255, 255), 2)
    # 5.外接矩形
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # 6.最小外接矩形
    rect = cv2.minAreaRect(cnt)
    print('最小外接矩形的四个顶点：', rect)
    # 获取到最小外接矩形的四个顶点box：[[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
    # 7.最小外接圆
    (x, y), radius = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(img, center, radius, (0, 255, 0), 2)
    # 8.椭圆拟合
    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img, ellipse, (0, 255, 0), 2)
    # 9.直线拟合
    rows, cols = img.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    left_y = int((-x*vy/vx)+y)
    right_y = int(((cols-x)*vy/vx)+y)
    cv2.line(img, (cols-1, right_y), (0, left_y), (255, 255, 0), 2)
    # 10.获取凸包, 如果需要检测凸缺陷时， 第二个参数returnPoints = False 必须为False
    hull = cv2.convexHull(cnt, returnPoints=False)
    # 11.轮廓缺陷,cv2.drawContours(img, [hull], 0, (0, 255, 0), 3)
    # 它会返回一个数组，每一行的值为[起点，终点，最远的点，到最远点的近似距离]
    defects = cv2.convexityDefects(cnt, hull)
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        cv2.line(img, start, end, [0, 255, 255], 2)
        cv2.circle(img, far, 5, [0, 255, 255], -1)
        print(start, end, far, d)
    # 12. 函数cv2.pointPolygonTest(cnt, point, True)
    # 此函数用于查找图像中的点与轮廓之间的最短距离。
    # 当点在轮廓外时返回负距离，
    # 当点在轮廓内时返回正距离，当点在轮廓上时返回零距离。
    dist = cv2.pointPolygonTest(cnt, (50, 50), True)
    print(dist)

cv2.imshow('img', img)

cv2.waitKey()
cv2.destroyAllWindows()
