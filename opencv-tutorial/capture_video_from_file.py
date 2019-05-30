# _*_ coding: utf-8 _*_
# @Time     : 2019/3/3 17:04
# @Author   : Ole211
# @Site     : 
# @File     : capture_video_from_file.py    
# @Software : PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('e:\\MP4\\')

cap = cv2.VideoCapture('vtest.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()