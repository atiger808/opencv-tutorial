# _*_ coding: utf-8 _*_
# @Time     : 2019/8/27 1:54
# @Author   : Ole211
# @Site     : 
# @File     : 手动几何矫正.py
# @Software : PyCharm

import cv2
import os
import numpy as np
import math
import tkinter as tk
from tkinter import filedialog

os.chdir('d:\\img\\img1\\')
mode = True
drawing = False
ix, iy = -1, -1
status = [None, None]
points = []
img = None
temp_dst = None
rect = None


# 计算两点之间距离函数
def calculate_distance(point1, point2):
    d_x = point1[0] - point2[0]
    d_y = point1[1] - point2[1]
    distance = math.sqrt(d_x ** 2 + d_y ** 2)
    return int(distance)


def draw(event, x, y, flags, param):
    global mode, drawing, ix, iy, points, img, status, rect, temp_dst
    if event == cv2.EVENT_FLAG_LBUTTON:
        status.append(1)
        drawing = True
        ix, iy = x, y
        cv2.circle(img, (ix, iy), 5, (50, 0, 250), -1)
        points.append([x, y])
        print(points)
        if len(points) >= 2:
            cv2.line(img, tuple(points[-2]), tuple(points[-1]), (0, 255, 255), 3)
        if len(points) % 4 == 0:
            cv2.line(img, tuple(points[-4]), tuple(points[-1]), (0, 255, 255), 3)

    elif event == cv2.EVENT_RBUTTONUP:
        status.append(0)
        if drawing == True and ix != x and iy != y and len(points) % 4 == 0:
            if mode == True and status[-1] == 0:
                print(status)
                status.clear()
                pts1 = np.int32(points[:4])
                # cv2.polylines(img, [pts1], True, (0,255,255), 5)
                points.clear()
                cv2.circle(img, (x, y), 5, (0, 0, 0), -1)
                pts1 = np.float32(pts1)
                rows, cols = calculate_distance(pts1[0], pts1[1]), calculate_distance(pts1[0], pts1[3])
                # 透视变换
                if cols > rows:
                    pts2 = np.float32([[0, 0], [0, rows], [cols, rows], [cols, 0]])
                    M = cv2.getPerspectiveTransform(pts1, pts2)
                    dst = cv2.warpPerspective(o, M, (cols, rows))
                else:
                    pts2 = np.float32([[0, 0], [0, cols], [rows, cols], [rows, 0]])
                    M = cv2.getPerspectiveTransform(pts1, pts2)
                    dst = cv2.warpPerspective(o, M, (rows, cols))
                temp_dst = dst
                cv2.imshow('result-image', dst)
                drawing = False
    elif mode == 's' and temp_dst is not None:
        imgname = os.path.splitext(filename)[-2] + '_dst.jpg'
        cv2.imwrite(imgname, temp_dst)
        print('保存成功')
        mode = True
        temp_dst = None
    elif event == cv2.EVENT_MBUTTONUP:
        img = o.copy()
        status.clear()
        points.clear()


if __name__ == '__main__':
    print('选择文件：')
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    if os.path.exists(filename):
        o = cv2.imread(filename)
        h, w = o.shape[:2]
        print(h, w)
        img = o.copy()
        cv2.namedWindow('original-image', cv2.WINDOW_NORMAL)
        cv2.namedWindow('result-image', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('original-image', draw)

        while 1:
            cv2.imshow('original-image', img)
            k = cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                mode = 's'
        cv2.destroyAllWindows()
    else:
        print('文件不存在！')
