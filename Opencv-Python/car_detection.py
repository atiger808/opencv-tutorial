# _*_ coding: utf-8 _*_
# @Time     : 2019/3/20 16:02
# @Author   : Ole211
# @Site     : 
# @File     : car_detection.py    
# @Software : PyCharm

import cv2 as cv
import numpy as np
import os

os.chdir('d:\\video\\src\\')

# 1, 加载视频
cap = cv.VideoCapture('road.mp4')
# 背景分离
fgbg = cv.createBackgroundSubtractorMOG2()
kernelOp = np.ones((3, 3), np.uint8)
kernelCl = np.ones((5, 5), np.uint8)
areaTH = 1000
cars = []
max_p_age = 5
pid = 1
w = cap.get(3)
h = cap.get(4)
mx = int(w/2)
my = int(h/2)
count = 9
while(cap.isOpened()):
    ret, frame = cap.read()
    w, h = frame.shape[:2]
    roi = frame[int(w/2):w, 0:h]
    fgmask = fgbg.apply(roi)
    try:
        # 选出高亮区域
        area_pos = np.array([[h // 2 - 100, w // 2], [h // 2 + 100, w // 2], [h, w], [0, w]])
        base = np.zeros(frame.shape, dtype='uint8')
        area_mask = cv.fillPoly(base, [area_pos], [100, 0, 0])
        cv.imshow('area_mask', area_mask)
        # area_mask = cv.bitwise_and(frame, frame, mask=area_mask)
        cv.addWeighted(area_mask, 1.0, frame, 1.0, 0, frame)

        # 显示文字
        count = count + 1
        text = 'Statistika UII ' + str(count)
        cv.putText(frame, text, (0, my), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv.LINE_AA)
        # cv.imshow('Frame', frame)

        # 形态转换
        ret, imBin = cv.threshold(fgmask, 200, 255, cv.THRESH_BINARY)
        # # 开运算
        mask = cv.morphologyEx(imBin, cv.MORPH_OPEN, kernelOp)
        # # 闭运算
        mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernelCl)
        cv.imshow('Background Subtraction', fgmask)
        cv.imshow('mask', mask)

        # 寻找轮廓
        contours0, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        for cnt in contours0:
            # 获取轮廓的面积
            area = cv.contourArea(cnt)
            if area > 500 and area < 600:
                M = cv.moments(cnt)
                # 获取轮廓的重心坐标
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                # 获取轮廓的起始点x, y坐标，以及长宽w, h
                x, y, w, h = cv.boundingRect(cnt)
                # 将轮廓以红点标记
                cv.circle(roi, (cx, cy), 5, (0, 0, 255), -1)
                # 将轮廓外接画矩形框
                img = cv.rectangle(roi, (x, y), (x+w, y+h), (0, 255, 0), 2)

                print(area)
                # 画出轮廓
                # cv.drawContours(roi, cnt, -1, (0, 255, 0), 3, 8)base)
            cv.imshow('Contours', frame)

        # frame2 = frame
    except Exception as e:
        print(e)
        print('EOF')
        break


    # 画线段
    # line1 = np.array([[100, 100], [300, 100], [350, 200]], np.int32).reshape((-1, 1, 2))
    # line2 = np.array([[0, my+20], [w, my+20]], np.int32).reshape((-1, 1, 2))
    # frame2 = cv.polylines(frame2, [line1], False, (255, 0, 0), thickness=2)
    # frame2 = cv.polylines(frame2, [line2], True, (255, 0, 0), thickness=2)
    # cv.imshow('Frame 2', frame2)
    k = cv.waitKey() & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
