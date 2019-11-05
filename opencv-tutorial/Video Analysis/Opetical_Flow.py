# _*_ coding: utf-8 _*_
# @Time     : 2019/9/3 2:48
# @Author   : Ole211
# @Site     : 
# @File     : Opetical_Flow.py    
# @Software : PyCharm

import cv2
import numpy as np

cap = cv2.VideoCapture('d:\\video\\src\\t6.mp4')

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

while 1:
    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame2', frame2)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    # elif k  == ord('s'):
    #     cv2.imwrite('opticalfb.png', frame2)
    #     cv2.imwrite('opticalsv.png', bgr)
    # else:
    #     cv2.imshow('opticalsv', bgr)
    cv2.imshow('opticalflow', bgr)
    prvs = next
cap.release()
cv2.destroyAllWindows()