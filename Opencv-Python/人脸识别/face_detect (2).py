# _*_ coding: utf-8 _*_
# @Time     : 2019/8/29 16:36
# @Author   : Ole211
# @Site     : 
# @File     : face_detect.py    
# @Software : PyCharm
import cv2
import time
from datetime import datetime

def zh_ch(string):
    return string.encode('gbk').decode(errors='ignore')

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
cv2.namedWindow(zh_ch('动态人脸监测'), cv2.WINDOW_NORMAL)
while (cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    now = datetime.now()
    text = now.strftime('%Y-%m-%d %H:%M:%S')
    cv2.putText(frame, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    if faces is not None:
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 200, 200), 2)
        start_time = datetime.now()
        filename = './image/' + now.strftime('%Y-%m-%d %H:%M:%S')+'.jpg'
        cv2.imwrite(filename, frame)
        print('shoot done')
    else:
        print('no face')
    cv2.imshow(zh_ch('动态人脸监测'), frame)
    k = cv2.waitKey(20) & 0xff
    if k == 27:
        break
cap.release()
cv2.waitKey()
cv2.destroyAllWindows()
