# _*_ coding: utf-8 _*_
# @Time     : 2019/8/27 1:54
# @Author   : Ole211
# @Site     : 
# @File     : 鼠标操作几何矫正.py    
# @Software : PyCharm

import cv2
import os
import numpy as np
os.chdir('d:\\img\\')

mode = True
drawing = False
ix,iy = -1, -1
status = [None, None]
pts = []
img = None
temp_t = None
rect = None

def draw(event, x, y, flags, param):
    global mode,drawing,ix, iy, pts, img, status, rect
    if event == cv2.EVENT_FLAG_LBUTTON:
        status.append(1)
        drawing = True
        ix, iy = x, y
        cv2.circle(img, (ix, iy), 5, (50, 0, 250), -1)
        pts.append([x, y])
        print(pts)
        print('down--', ix, iy)

    elif event == cv2.EVENT_RBUTTONUP:
        status.append(0)
        if drawing == True and ix!=x and iy!=y and len(pts)%4==0:
            if mode == True and status[-1] == 0:
                print(status)
                status.clear()
                points = np.int32(pts[:4])
                cv2.polylines(img, [points], True, (0,255,255))
                pts.clear()
                cv2.circle(img, (x, y), 5, (0, 0, 0), -1)
                points = np.float32(points)
                points2 = np.float32([[0, 0], [0, w], [h, w], [h, 0]])
                M = cv2.getPerspectiveTransform(points, points2)
                dst = cv2.warpPerspective(o, M, (h, w))
                cv2.imshow('dst', dst)
                drawing = False
                print(points)
    elif event == cv2.EVENT_MBUTTONUP:
        img = o.copy()
        status.clear()
        pts.clear()

if __name__ == '__main__':
    o = cv2.imread('card77.jpg')
    h, w = o.shape[:2]
    print(h, w)
    img = o.copy()
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('image', draw)

    while 1:
        cv2.imshow('image', img)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    cv2.destroyAllWindows()
