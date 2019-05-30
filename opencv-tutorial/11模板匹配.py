# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 23:43
# @Author   : Ole211
# @Site     : 
# @File     : 11模板匹配.py
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

img_rgb = cv.imread('messi.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('messi_face.jpg', 0)
w, h = template.shape[::-1]

'''
在这里，我们用img_gray（我们的主图像），模板，
和我们要使用的匹配方法调用matchTemplate，并将返回值称为res。 
我们指定一个阈值，这里是 80%。 然后我们使用逻辑语句，
找到res大于或等于 80% 的位置。
'''

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.6
loc = np.where(res >= threshold)
print('res', res)
'''
最后，我们使用灰度图像中找到的坐标，标记原始图像上的所有匹配：
'''
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 1)

cv.imshow('img_rgb', img_rgb)
cv.imshow('template', template)
print(w, h)
cv.waitKey()
cv.destroyAllWindows()