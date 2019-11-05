# _*_ coding: utf-8 _*_
# @Time     : 2019/8/15 16:41
# @Author   : Ole211
# @Site     : 
# @File     : 鼠标事件图像指定区域替换.py    
# @Software : PyCharm

import cv2
import time
import os
import tkinter as tk
from tkinter import filedialog
import numpy as np

os.chdir('d:\\img\\')

# 通过操作鼠标替换两张相同尺寸的图片指定区域
# 鼠标框选指定区域，进行替换
# 鼠标左键按一下并滑动: 开始框选
# 鼠标左键松开: 框选成功
# 鼠标中键按一下：清除框选
# 按下s键：保存替换好的图片
# 按下a键：保存框选图片

mode = True
drawing = False
ix, iy = -1, -1
status = [None, None]
pts = []
img = None
temp_t = None
rect = None


def draw(event, x, y, flags, param):
    global mode, drawing, ix, iy, pts, img, status, rect
    if event == cv2.EVENT_LBUTTONDOWN:
        status.append(1)
        drawing = True
        ix, iy = x, y
        cv2.circle(img, (ix, iy), 5, (0, 0, 0), -1)
        print('down--', ix, iy)

    elif event == cv2.EVENT_LBUTTONUP:
        status.append(0)
        if drawing == True and ix != x and iy != y:
            if mode == True and status[-1] == 0:
                print(status)
                status.clear()
                cv2.rectangle(img, (ix, iy), (x, y), (255, 100, 100), 2)
                cv2.circle(img, (x, y), 5, (0, 0, 0), -1)
                pts = [(ix, iy), (x, y)]
                start_point = min(pts)
                end_point = max(pts)
                rect = o[start_point[1]:end_point[1], start_point[0]:end_point[0]]
                temp_t[start_point[1]:end_point[1], start_point[0]:end_point[0]] = rect
                cv2.imshow('rect', rect)
                drawing = False
                print('up', x, y)
                print('--' * 30)
                print(pts)

    elif mode == 's':
        cv2.imwrite('dst.jpg', temp_t)
        print('保存成功')
        mode = True
    elif mode == 'a':
        imgname = str(int(time.time())) + '.jpg'
        cv2.imwrite(imgname, rect)
        print('框选保存成功')
        mode = True
    elif event == cv2.EVENT_MBUTTONUP:
        img = o.copy()
        status.clear()


def clear(event, x, y, flags, param):
    global temp_t
    if event == cv2.EVENT_MBUTTONUP:
        temp_t = temp.copy()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    imgname = filedialog.askopenfilename()
    o = cv2.imread(imgname)
    img = o.copy()
    w, h = o.shape[:2]
    temp = np.zeros_like(o)
    temp[:,:,:] = [255, 255, 255]
    cv2.imwrite('blank.jpg', temp)
    temp_t = temp.copy()
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('temp', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('image', draw)
    cv2.setMouseCallback('temp', clear)

    while (1):
        cv2.imshow('image', img)
        cv2.imshow('temp', temp_t)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
        elif k == ord('s'):
            mode = 's'
        elif k == ord('a'):
            mode = 'a'
    cv2.destroyAllWindows()
