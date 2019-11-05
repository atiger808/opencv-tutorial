# _*_ coding: utf-8 _*_
# @Time     : 2019/9/3 17:54
# @Author   : Ole211
# @Site     : 
# @File     : calc_counts_from_video.py    
# @Software : PyCharm

import numpy as np
import cv2

cap = cv2.VideoCapture('d:\\video\\output.mp4')
FPS = cap.get(cv2.CAP_PROP_FPS)
SIZE = int(cap.get(3)), int(cap.get(4))
W, H = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('d:\\video\\dst\\output_calc_counts.mp4', fourcc, FPS, SIZE, True)

# 获取视频的第一帧
ret, frame = cap.read()
# 设置初始化窗口位置
# road2.mp4 r, h, c, w = 380, 100, 180, 100
# road.mp4 r, h, c, w =
r, h, c, w = 340, 100, 500, 100
track_window = (c, r, w, h)
# 设置跟踪初始兴趣区域
roi = frame[r:r + h, c:c + w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('roi1', roi)
cv2.imshow('hsv_roi1', hsv_roi)
cv2.imshow('mask1', mask)
cv2.imshow('frame1', frame)

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
counts = 0
display = False
status_list = [None, None]
while 1:
    ret, frame = cap.read()
    if ret == True:
        status = 0
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret1, track_window = cv2.meanShift(dst, track_window, term_crit)
        x, y, w, h = track_window

        roi = frame[y:y + h, x:x + w]
        hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
        cv2.imshow('mask', mask)

        img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        lineLeft = (W // 4, 0), (W // 4, H)
        lineRight = (W // 4 * 3, 0), (W // 4 * 3, H)
        centerpoint = (x + w // 2, y + h // 2)
        if lineRight[0][0] > centerpoint[0] > lineLeft[0][0]:
            status = 1
        else:
            status = 0
        status_list.append(status)
        status_list = status_list[-2:]
        if status_list[-1] == 1 and status_list[-2] == 0:
            counts += 1
            display = not display
        # if status_list[-1] == 0 and status_list[-2] == 1:
        #     counts -= 1
        text = 'Counts:%s' % counts
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.line(frame, lineLeft[0], lineLeft[1], (0, 0, 255), 2)
        cv2.line(frame, lineRight[0], lineRight[1], (0, 0, 255), 2)
        cv2.circle(frame, centerpoint, 5, (0, 0, 255), -1)
        print(centerpoint)
        print(ret1)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(24) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite('./tmp/' + chr(k) + '.jpg', frame)
            out.write(frame)
    else:
        break

cap.release()
cv2.waitKey()
cv2.destroyAllWindows()
