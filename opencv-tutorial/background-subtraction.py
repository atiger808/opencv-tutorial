# _*_ coding: utf-8 _*_
# @Time     : 2019/8/29 23:43
# @Author   : Ole211
# @Site     : 
# @File     : background-subtraction.py    
# @Software : PyCharm

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
# fgbg = cv2.createBackgroundSubtractorKNN()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    cv2.imshow('fgmask', fgmask)

    ret, thresh = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
    # 开闭操作
    kernelOp = np.ones((3, 3), np.uint8)
    kernelCl = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernelOp)
    # closing = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernelCl)

    contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 4000:
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.drawContours(frame, cnt, -1, (0, 255, 255), 3, 8)
    cv2.imshow('closing', opening)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()