# import cv2
# # 读取
# i =cv2.imread('d:\\img\\cat.png', cv2.IMREAD_UNCHANGED)
# # 显示
# cv2.imshow('demo', i)
# # 修改像素
# i[100:150, 100:150] = [255, 255, 0]
# cv2.imshow('result', i)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # 保存
# cv2.imwrite('d:\\img\\cat2.png', i)

api_key = 'S1NDVDUgcgHxRjnxodWHo1fk'

'''
图像分类
    二值图像
    灰度图像
    RGB图像

灰度图像：
    读取像素
        img.item(88, 99)
    修改像素
        img.itemset((88, 99), 255)
BGR图像
    读取像素
        img.item(88, 99， 0)
    修改像素
        img.itemset((88, 99， 0), 255)
获取图像属性
    1.形状
        shape 可以获取图像的形状， 返回包含行数， 列数， 通道数的元组
        img.shape
    2.像素数目
        size 可以获取图像的像素数目
            灰度  返回：行数*列数
            彩色  返回：行数*列数*通道数
    3.图像类型
        dtype  返回图像的数据类型
        img.dtype

图像ROI
    ROI (region of interest), 感兴趣的区域
    从被处理的图像 以方框， 圆， 椭圆， 不规则多边形等方式勾勒出需要处理的区域
    可以通过(Operator) 和函数来求得感兴趣的区域ROI, 并进行图像的下一步处理
'''
# 图像ROI
import cv2
import numpy as np
import os
os.chdir('d:\\img\\')

img = cv2.imread('cat.png', cv2.IMREAD_UNCHANGED)
print(img.shape)
face = np.ones((60, 70, 3))
face = img[50:100, 50: 100]
img[0:50, 0:50] = face
cv2.imshow('face', img)


# 直方图均值化
im2 = cv2.imread('opencv-template-matching.jpg', 0)
equ = cv2.equalizeHist(im2)
median = cv2.medianBlur(equ, 5)
# 水平合并
hstack = np.hstack((im2, equ))
hstack1 = np.hstack((im2, median))
# 垂直合并
vstack = np.vstack((im2, equ))
cv2.imshow('hstack', hstack)
cv2.imshow('hstack1', hstack1)

# clahe 有限对比度适应性直方图均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(im2)
cv2.imshow('cl1', cl1)

cv2.waitKey()
cv2.destroyAllWindows()

'''
图像拆分与合并
    b, g, r = cv2.split(img)
    b = cv2.split(img)[0]
    cv2.imshow('B', b)

    bgr = cv2.merge([b, g, r])
    rgb = cv2.merge([r, g, b])
'''