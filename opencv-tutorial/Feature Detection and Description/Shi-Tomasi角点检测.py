# _*_ coding: utf-8 _*_
# @Time     : 2019/9/17 15:47
# @Author   : Ole211
# @Site     : 
# @File     : Shi-Tomasi角点检测.py    
# @Software : PyCharm
'''
Opencv提供函数cv2.goodFeaturesToTrack().这个函数可以帮助我们使用Shi-Tomasi方法获取图像中的N个最好的角点
goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, corners=None, mask=None, blockSize=None, useHarrisDetector=None, k=None)
image: 输入图像， 一般是灰度图像
maxCorners: 先要检测带的角点数目
qualityLevel: 角点的质量水平， 0-1之间.
              它代表了角点的最低质量， 实际用于过滤角点的最小特征值是qualityLevel与图像中最大特征的乘积，所以qualityLevel的值不应超过1,
              （常用的值为0.1, 0.001）。低于这个值得所有角点都会被忽略
minDistance: 两个角点的最短欧式距离
mask: 是一幅像素值为布尔类型的像素，用于指定输入图像中蚕吐角点计算的像素点。
blockSize：计算导数的自相关矩阵时指定点的领域，默认为3，采用小窗口计算的结果比单点（也就是blockSize为1）计算的效                  果要好。
useHarrisDetector: 默认值为0，若非0，则函数使用Harris的角点定义
K： 当useHarrisDetector非0，则K为用于设置hessian自相关矩阵即对hessian行列式的相对权值的权值系数。
————————————————
版权声明：本文为CSDN博主「云net」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_36387683/article/details/80550964


'''
import cv2
import numpy as np
img = cv2.imread('d:\\img\\bird.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 30, 0.01, 10)
'''
goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, corners=None, mask=None, blockSize=None, useHarrisDetector=None, k=None)
image： 灰度图像
maxCorners: 你想要检测的角点数目
qualityLevel: 角点的质量水平， 取值范围【0-1】， 它指的是角点的最低质量， 低于这个数的所有角点会被忽略
minDistance: 两个角点的最短欧氏距离
'''
# int0 直接把小数后面排期取整， 并不是四舍五入
corners = np.int0(corners)
print(len(corners))
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()