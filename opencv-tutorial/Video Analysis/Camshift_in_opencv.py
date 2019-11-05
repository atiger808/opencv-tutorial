# _*_ coding: utf-8 _*_
# @Time     : 2019/9/3 1:16
# @Author   : Ole211
# @Site     : 
# @File     : Camshift_in_opencv.py
# @Software : PyCharm

import numpy as np
import cv2

# road2.mp4 r, h, c, w = 380, 100, 180, 100
# road.mp4
cap = cv2.VideoCapture('d:\\video\\src\\road.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
size = int(cap.get(3)), int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./tmp/output_camshift.mp4', fourcc, fps, size, True)


ret, frame = cap.read()
r, h, c, w = 380, 100, 180, 100
track_window = (c, r, w, h)


roi = frame[r:r+h, c:c+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('roi', roi)
cv2.imshow('hsv_roi', hsv_roi)
cv2.imshow('mask', mask)

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
while 1:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        c, r, w, h = track_window
        roi = frame[r:r + h, c:c + w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask_1 = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
        cv2.imshow('mask_1', mask_1)

        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        img2 = cv2.polylines(frame, [pts], True, [0, 255, 255], 2)
        cv2.imshow('img2', img2)
        k = cv2.waitKey() & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite('./tmp/' + chr(k) + '.jpg', img2)
            out.write(img2)
    else:
        break
cv2.destroyAllWindows()
cap.release()