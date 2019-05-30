# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 17:59
# @Author   : Ole211
# @Site     : 
# @File     : opencv画图函数.py    
# @Software : PyCharm

import numpy as np
import cv2

# 创建一个黑色背景的图片
img = np.zeros((512, 512, 3), np.uint8)

# 画一条宽度为5像素的蓝色线段
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# 画一个矩形
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 画一个圆
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 画椭圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1 )

# 画多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 255))

# 添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Python', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()