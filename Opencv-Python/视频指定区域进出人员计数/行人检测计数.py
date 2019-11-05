# _*_ coding: utf-8 _*_
# @Time     : 2019/9/3 18:50
# @Author   : Ole211
# @Site     : 
# @File     : 行人检测计数.py    
# @Software : PyCharm

import cv2
import numpy as np

cap = cv2.VideoCapture('d:\\video\\src\\road.mp4')
size = int(cap.get(3)), int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
out = cv2.VideoWriter('d:\\video\\dst\\test_00.avi', fourcc, fps, (640, 480), True)


# 背景抽离
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
counts = 0
display = False
status_list = [None, None]
track_window = None
roi_hist = None
while 1:
    print('-'*40)
    ret, frame = cap.read()
    status = 0
    frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_AREA)
    H, W = frame.shape[:2]
    upline = (W//2-110, H//12*7), (W//2+110, H//12*7)
    downline= (W//2-110, H//4*3), (W//2+110, H//4*3)
    cv2.line(frame, upline[0],  upline[1], (0, 255, 255), 2)
    cv2.line(frame, downline[0], downline[1], (0, 0, 255), 2)
    # 创建蒙版
    roi = frame[H//12*7:H//4*3, W//2-110:W//2+110]
    mask = roi.copy()
    mask[:,:] = [0, 255, 0]
    dst = cv2.addWeighted(roi, 0.8, mask, 0.2, 0)
    frame[H // 12 * 7:H // 4 * 3, W // 2 - 110:W // 2 + 110] = dst
    cv2.imshow('mask', dst)
    fgmask = fgbg.apply(frame)
    cv2.imshow('fgmask', fgmask)
    blur = cv2.GaussianBlur(fgmask, (5, 5), 0)

    # 泛洪填充
    # w, h = frame.shape[:2]
    # print(w, h)
    # mask = np.zeros((w+2, h+2), np.uint8)
    # cv2.floodFill(blur, mask, (w-1, h-1), (255, 255, 255), (2, 2, 2), (3, 3, 3), 8)

    # ret, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
    # cv2.imshow('thresh', thresh)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    erode = cv2.erode(blur, kernel, iterations=2)
    dilate = cv2.dilate(erode, kernel, iterations=2)

    ret, thresh = cv2.threshold(dilate, 150, 255, cv2.THRESH_BINARY)
    opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    cv2.imshow('threth', thresh)
    cv2.imshow('opened', opened)

    cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print('cnts----', len(cnts))
    for cnt in cnts:
        cntarea = cv2.contourArea(cnt)

        if (300>cntarea > 70):
            x, y, w, h = cv2.boundingRect(cnt)
            M = cv2.moments(cnt)
            cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])

            if (downline[0][1] > cy > upline[0][1]) and (upline[1][0]>cx>upline[0][0]):
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                status = 1

            else:
                status = 0
        status_list.append(status)
        status_list = status_list[-2:]
        if status_list[-1] == 1 and status_list[-2] == 0:
            counts += 1
            display = not display
    text = 'Counts:%s' % counts
    cv2.putText(frame, text, (upline[0][0] + 5, upline[0][1]), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255),
                3, cv2.LINE_AA)

    #
    #             track_window = x, y, w, h
    #             roi_w = frame[y:y+h, x:x+w]
    #             hsv_roi = cv2.cvtColor(roi_w, cv2.COLOR_BGR2HSV)
    #             mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180., 255., 255.)))
    #             # 颜色直方图
    #             roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
    #             # 归一化
    #             cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    #
    # term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    # if track_window and roi_hist.all:
    #     print('up--',track_window)
    #     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #     # 直方图反向投影
    #     dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    #     # 返回迭代次数和更新后的边框
    #     ret1, track_window = cv2.meanShift(dst, track_window, term_crit)
    #     print('down--', track_window)
    #     x, y, w, h = track_window
    #     centerpoint = (x + w//2, y+h//2)
    #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    #     cv2.circle(frame, (x + w // 2, y + h // 2), 5, (0, 255, 0), -1)
    cv2.imshow('frame', frame)
    k = cv2.waitKey() & 0xff
    if k == 27:
        break
    else:
        cv2.imwrite('d:\\video\\dst\\test.jpg', frame)
cap.release()
cv2.destroyAllWindows()





