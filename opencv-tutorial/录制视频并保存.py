# _*_ coding: utf-8 _*_
# @Time     : 2019/3/5 20:17
# @Author   : Ole211
# @Site     : 
# @File     : 录制视频并保存.py    
# @Software : PyCharm
'''
这里主要注意的是正在使用的编解码器， 以及在while循环之前定义的输出信息， 然后在while循环中，
我们使用out.write()来输出帧。最后， 在while 选混之外， 在我们释放摄像头之后
我们也释放out
'''

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir('e:\\MP4\\')
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(True):
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    out.write(frame)
    cv.imshow('gray', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()
