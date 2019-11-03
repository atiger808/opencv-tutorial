# _*_ coding: utf-8 _*_
# @Time     : 2019/9/27 12:46
# @Author   : Ole211
# @Site     : 
# @File     : 圆形框选人脸.py    
# @Software : PyCharm

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
_, frame = cap.read()
w, h = frame.shape[:2]
bgimg = cv2.imread('d:\\img\\flog7.jpg')
bgimg = cv2.resize(bgimg, (h, w))

while(cap.isOpened()):
    ret, frame = cap.read()
    w, h = frame.shape[:2]
    mask = np.zeros((w, h), 'uint8')
    x, y = np.ogrid[:w, :h]
    cen_x, cen_y = w//2, h//2
    distance_from_center = np.sqrt((x-cen_x)**2 + (y-cen_y)**2)
    radius = (w//2)
    circular_img = distance_from_center < radius
    mask[circular_img] = 255
    mask_inv = cv2.bitwise_not(mask)

    cv2.imshow('frame', frame)
    fg_dst = cv2.bitwise_and(frame, frame, mask=mask)
    bg_dst = cv2.bitwise_and(bgimg, bgimg, mask=mask_inv)
    dst = cv2.add(fg_dst, bg_dst)
    cv2.imshow('dst', dst)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
# cap.release()
cv2.destroyAllWindows()