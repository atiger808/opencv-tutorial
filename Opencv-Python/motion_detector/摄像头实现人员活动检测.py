# _*_ coding: utf-8 _*_
# @Time     : 2019/8/14 11:14
# @Author   : Ole211
# @Site     : 
# @File     : 摄像头实现人员活动检测.py    
# @Software : PyCharm

import cv2
import time
import random

cap = cv2.VideoCapture(0)
fps = 24
pre_frame = None

time.sleep(2)
while (1):
    start = time.time()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not ret:
        print('打开视频失败')
        break
    end = time.time()
    seconds = end - start
    if seconds < 1.0 / fps:
        time.sleep(1.0 / fps - seconds)
    gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)

    if pre_frame is None:
        pre_frame = gray_img
    else:
        img_detal = cv2.absdiff(pre_frame, gray_img)
        thresh = cv2.threshold(img_detal, 30, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        # 注：
        # opencv2 返回两个值：contours, hierarchy
        # opencv3 会返回三个值分别是img, contours, hierarchy
        contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        length = len(contours)
        if length > 0:
            contours = sorted(contours, key=cv2.contourArea, reverse = True)
            cnt = contours[0]
            hull_temp = cv2.convexHull(cnt)
            cv2.drawContours(frame, [cnt], 0, (255, 0, 0), 2)
            hull = cv2.convexHull(cnt, returnPoints=False)
            defects = cv2.convexityDefects(cnt, hull)
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                cv2.line(frame, start, end, [0, 0, 255], 2)
                cv2.circle(frame, far, 6, [0, 255, 255], -1)
                print(start, end, far, d)


        # for c in contours:
        #     if cv2.contourArea(c) < 10000:
        #         continue
        #     else:
        #         # 画出矩形
        #         x, y, w, h = cv2.boundingRect(c)
        #         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        #         # 画出线条轮廓
        #         cv2.drawContours(frame, c, -1, (0, 255, 255), 3)
        #         # 保存图像
        #         # print('something~~')
        #         # Time = time.strftime('%Y-%m-%d-%H-%M-%Sq', time.localtime(time.time()))
        #         # cv2.imwrite('./image/'+'JC'+Time+'.jpg', frame)
        cv2.imshow('img_delta', thresh)
        cv2.imshow('result', frame)

    # pre_frame = gray_img
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
