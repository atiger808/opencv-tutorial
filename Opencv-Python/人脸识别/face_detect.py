# _*_ coding: utf-8 _*_
# @Time     : 2019/8/29 16:36
# @Author   : Ole211
# @Site     : 
# @File     : face_detect.py    
# @Software : PyCharm
import cv2
import time
from datetime import datetime

def face_dect(imgfile):
    img = cv2.imread(imgfile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if faces is not None:
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,255), 2)
        cv2.imshow('result', img)
        cv2.imwrite('people_out.jpg', img)
    else:
        print('no face')



cap = cv2.VideoCapture(0)
cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
# 截图文件名记录列表
record_screenshot = []
# 帧记录列表
record_frame = []
# 是否有异常状态
status_state = False
status_list = [None, None]
while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    if faces is not None:
        status = 1
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
    else:
        print('no face')
    now = datetime.now()
    text = now.strftime('%Y-%m-%d-%H:%M:%S')
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
        # out.write(frame)
        record_frame.append(frame)
        if len(record_frame) == 1 and status_state:
            screenshot = './image/' + file_name + '.jpg'
            cv2.imwrite(screenshot, frame)
            # 发送给微信
            # send_msg(screenshot)
            status_state = False
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())
        record_screenshot.append(file_name)
        record_frame.clear()


    cv2.imshow('dst', frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
cap.release()
cv2.waitKey()
cv2.destroyAllWindows()