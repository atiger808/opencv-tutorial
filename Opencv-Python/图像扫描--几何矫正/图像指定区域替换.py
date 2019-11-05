# _*_ coding: utf-8 _*_
# @Time     : 2019/8/15 13:06
# @Author   : Ole211
# @Site     : 
# @File     : 图像指定区域替换.py    
# @Software : PyCharm

import cv2
import numpy as np
import os

os.chdir('d:\\img\\')
'''
图片规格 1080*1920
支付宝从话费替换区域：[850:850+60, 900:900+160]
x, y , w, h = 900, 850, 160, 60
淘宝价格替换区域：[1100:1100+80, 40:40+150]
x, y, w, h = 30, 1100, 160, 80
'''
x, y, w, h = 30, 1100, 480, 80


def pic_rect_replace(src_path, template_path, rect):
    src = cv2.imread(src_path)
    template = cv2.imread(template_path)
    if src.shape != template.shape:
        print('fail...尺寸不一致')
    else:
        x, y, w, h = rect
        rect1 = template[y:y + h, x:x + w]
        src[y:y + h, x:x + w] = rect1
        dst_name = os.path.splitext(src_path)[-2] + '_' + os.path.splitext(template_path)[-2] + '.jpg'
        print(dst_name)
        # 保存替换后的图片
        cv2.imwrite(dst_name, src)
        cv2.imshow('dst', src)
        cv2.imshow('rect1', rect1)


if __name__ == '__main__':
    rect = x, y, w, h
    src_path = 'bag01.jpg'
    template_path = 'bag03.jpg'
    pic_rect_replace(src_path, template_path, rect)
    cv2.waitKey()
    cv2.destroyAllWindows()
