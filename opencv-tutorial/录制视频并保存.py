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

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
os.chdir('e:\\MP4\\')
cap = cv2.VideoCapture(0)
# 指定fourcc编解码
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'MJPG')
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20, (640, 480), True)

while(cap.isOpened):
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)
    cv2.imshow('o', frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
