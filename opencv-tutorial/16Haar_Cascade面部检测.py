# _*_ coding: utf-8 _*_
# @Time     : 2019/3/6 1:58
# @Author   : Ole211
# @Site     : 
# @File     : 16Haar_Cascade面部检测.py    
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')
full_cascade = cv.CascadeClassifier('haarcascade_upperbody.xml')

# 照片人脸检测
img_path = 'f1.jpg'
filename, ext = os.path.splitext(img_path)
img_outpath = filename + '_out' + ext

img = cv.imread(img_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    # 用文字标记出来
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, 'face', (x, y), font, 1, (255, 255, 255), 0, cv.LINE_AA)

    # 眼睛检测0
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        # 用文字标记出来
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(roi_color, 'eye', (ex, ey), font, 1, (255, 255, 255), 1, cv.LINE_AA)
cv.imshow('img', img)
# 图片保存
cv.imwrite(img_outpath, img)

# 视频人脸检测
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('face-detect.mp4', fourcc, 20.0, (640, 480))
while(1):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 检测人脸
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # 用文字标记出来
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame, 'face-detect', (x, y), font, 1, (255, 255, 255), 1, cv.LINE_AA)

        # 检测眼睛
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # 绘制矩形
            cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 1)
            # 绘制圆
            # cv.circle(roi_color, (ex+ew//2, ey+eh//2), int(np.sqrt((ew//2)**2 + (eh//2)**2)), (0, 255, 0), -1)
            # 用文字标记出来
            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(roi_color, 'eye', (ex, ey), font, 1, (255, 255, 255), 1, cv.LINE_AA)
    cv.imshow('frame', frame)
    # 视频保存
    out.write(frame)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()