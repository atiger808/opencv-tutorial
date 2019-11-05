# _*_ coding: utf-8 _*_
# @Time     : 2019/4/20 10:03
# @Author   : Ole211
# @Site     : 
# @File     : motion_detect.py
# @Software : PyCharm

# from tulingBot import send_msg
from datetime import datetime
import numpy as np
import pandas
import cv2
import time

import os

# 人脸检测模型
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
fourcc_mask = cv2.VideoWriter_fourcc(*'mp4v')
# out_mask = cv2.VideoWriter('./record/mask.mp4', fourcc_mask, 20.0, (640, 480))


def main():
    first_frame = None
    status_list = [None, None]
    times = []
    df = pandas.DataFrame(columns=['Start', 'End'])
    # 截图文件名记录列表
    record_screenshot = []
    # 帧记录列表
    record_frame = []
    # 是否有异常状态
    status_state = False
    # 打开本地设备摄像头
    cap = cv2.VideoCapture(0)
    count = 0
    while True:
        ret, rframe = cap.read()
        frame = rframe.copy()
        mask = np.zeros(frame.shape[:2], np.uint8)
        status = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 人脸检测
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(rframe, (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            # 用文字标记出来
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, 'face', (x, y), font, 1, (255, 255, 255), 0, cv2.LINE_AA)

            # 眼睛检测0
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                # 用文字标记出来
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(roi_color, 'eye', (ex, ey), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

        gaussian_img = cv2.GaussianBlur(gray, (21, 21), 0)
        hist_img = cv2.equalizeHist(gaussian_img)
        if first_frame is None:
            first_frame = hist_img
            continue
        delta_frame = cv2.absdiff(first_frame, hist_img)
        thresh_delta = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
        thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)
        thresh_delta = cv2.erode(thresh_delta, None, iterations=0)
        cnts, _ = cv2.findContours(thresh_delta.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        if len(cnts)>0:
            res = cnts[0]
            status = 1
            # 矩形框
            x, y, w, h = cv2.boundingRect(res)
            cv2.rectangle(rframe, (x, y), (x + w, y + h), (0, 255, 255), 3)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
            # 实体轮廓
            cv2.drawContours(mask, [res], 0, (255, 255, 255), -1)
            # cv2.imshow('mask', mask)
            # 线条轮廓
            # cv2.drawContours(frame, cnt, -1, [0, 255, 0], 3)


        now = datetime.now()
        text = now.strftime('%Y-%m-%d-%H:%M:%S')
        cv2.putText(rframe, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        status_list.append(status)
        status_list = status_list[-2:]
        if status_list[-1] == 1 and status_list[-2] == 0:
            status_state = not status_state
            start_time = datetime.now()
            times.append(start_time)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            file_name = start_time.strftime('%Y-%m-%d %H_%M_%S')
            out = cv2.VideoWriter('./record/' + file_name + '.mp4', fourcc, 20.0, (640, 480))

        if status_list[-1] == 1 and status_list[-2] == 1:
            out.write(rframe)
            record_frame.append(frame)
            if len(record_frame) == 1 and status_state:
                screenshot = './image/' + file_name + '.jpg'
                cv2.imwrite(screenshot, rframe)
                # 发送给微信
                # send_msg(screenshot)
                status_state = False

        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())
            record_screenshot.append(file_name)
            record_frame.clear()

        dst = cv2.bitwise_and(frame, frame, mask=thresh_delta)
        dst = dst.astype('uint8')
        # out_mask.write(dst)
        cv2.imshow('original', frame)
        # first_frame = hist_img
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    print(status_list)
    print(times)
    for i in range(0, len(times), 2):
        df = df.append({'Start': times[i], 'End': times[i + 1]}, ignore_index=True)
    df.to_csv('Times.csv')
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    time.sleep(2)
    main()
