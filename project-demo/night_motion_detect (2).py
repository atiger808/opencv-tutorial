# _*_ coding: utf-8 _*_
# @Time     : 2019/9/21 12:04
# @Author   : Ole211
# @Site     :
# @File     : night_motion_detect.py
# @Software : PyCharm

import cv2
import os
from datetime import datetime

cap = cv2.VideoCapture(0)
cv2.namedWindow('Night Detecting', cv2.WINDOW_NORMAL)
print('begining...')
fgbg = cv2.createBackgroundSubtractorMOG2()

status_list = [None, None]
# 帧记录列表
records = []
# 是否有异常状态
state = False
# 截图索引号
shoot_index = 0

if not os.path.exists('./image/'):
    os.mkdir('./image/')
if not os.path.exists('./record/'):
    os.mkdir('./record/')

while 1:
    ret, frame = cap.read()
    status = 0
    fgmask = fgbg.apply(frame)
    blur = cv2.GaussianBlur(fgmask, (7, 7), 0)
    ret, thresh = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))
    dilate = cv2.dilate(thresh, kernel, iterations=4)
    erode = cv2.erode(dilate, kernel, iterations=4)

    # 标记时间
    now = datetime.now()
    text = now.strftime('%Y-%m-%d-%H:%M:%S')
    cv2.putText(frame, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # 检测异常动静，并框选
    cnts, hierachy = cv2.findContours(erode, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            status = 1
    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[0] == 0 and status_list[1] == 1:
        state = True
        start_time = datetime.now()
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        file_name = start_time.strftime('%Y-%m-%d %H_%M_%S')
        out = cv2.VideoWriter('./record/' + file_name + '.mp4', fourcc, 20.0, (640, 480))
    if status_list[0] == 1 and status_list[1] == 1:
        # 写入视频文件
        out.write(frame)
        records.append(frame)
        if len(records) == 2 and state is True:
            start_time = datetime.now()
            file_name = start_time.strftime('%Y-%m-%d %H_%M_%S')
            # 写入图片文件
            cv2.imwrite('./image/' + file_name + '.jpg', frame)
            print('Warning!!!', start_time)
    if status_list[0] == 1 and status_list[1] == 0:
        state = False
        records.clear()
    cv2.imshow('binary',erode)
    cv2.imshow('Night Detecting', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
