# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 18:34
# @Author   : Ole211
# @Site     : 
# @File     : capture_video_from_file1.py    
# @Software : PyCharm

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('e:\\MP4\\')

cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('gray', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
