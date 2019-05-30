# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 17:25
# @Author   : Ole211
# @Site     : 
# @File     : capture_video_save_video.py    
# @Software : PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('e:\\MP4\\')

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame, 1)  # 参数1指水平方向，0是指相反反向
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
