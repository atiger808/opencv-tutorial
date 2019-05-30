# _*_ coding: utf-8 _*_
# @Time     : 2019/3/20 20:17
# @Author   : Ole211
# @Site     : 
# @File     : opencv中的绘图函数.py    
# @Software : PyCharm

import numpy as np
import cv2
import os

# 创建一个黑色背景的图片
img = np.zeros((512, 512, 3), np.uint8)

# 1.画线
# 需要告诉函数这条线的起点和终点坐标， 颜色，宽度
# 画一条宽度为5像素的蓝线
cv2.line(img, (0, 0), (260, 260), (255, 0, 0 ), 5)

# 2. 画矩形
# 指定左上角顶点和右下角顶点的坐标， 颜色， 宽度
cv2.rectangle(img, (350, 0), (500, 128), (0, 255, 0), 3)

# 3. 画圆
# 指定圆心坐标和半径大小，颜色， 是否填充，参数-1为内填充
cv2.circle(img, (425, 63), 63, (0, 0, 255), -1)

# 4. 画椭圆
# 一个参数是中心点的位置坐标
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)

# 5. 画多边形
# 需要指定每个顶点的坐标， 构建一个大小相等于行数X1X2的数组
# 行数就是点的数目， 这个数组必须为int32
# cv2.polylines()可以用来画很多条线。只把想画的线放在一个列表中将这个列表
# 传给函数就可以了，每条线会独立绘制， 比cv2.lines()一条一条绘制快些
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
# 注意第三个参数若是False， 我们得到的是不闭合的线
cv2.polylines(img, [pts], True, (0, 255, 255))

# 5.2画多边形
SHAPE = (720, 1280)
AREA_POS = np.array([[780, 716], [685, 373], [883, 383], [1280, 636], [1280, 720]])
base = np.zeros(SHAPE + (3, ), dtype='uint8')
area_mask = cv2.fillPoly(base, [AREA_POS], [255, 255, 255])[:, :, 0]
cv2.imshow('mask', area_mask)


# 6.在图片上添加文字
# 需要设置， 文字内容， 绘制位置， 字体类型， 大小， 颜色， 粗细， 类型等，这里推荐linetype=cv2.LINE_AA
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

# 为了演示， 建窗口显示出来
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 定义frame大小
cv2.resizeWindow('image', 1000, 1000)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()