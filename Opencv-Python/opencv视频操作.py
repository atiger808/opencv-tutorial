# _*_ coding: utf-8 _*_
# @Time     : 2019/3/15 12:10
# @Author   : Ole211
# @Site     : 
# @File     : opencv视频操作.py    
# @Software : PyCharm
import numpy as np
import cv2 as cv
import os
os.chdir('e:\\MP4\\')

# 用摄像头捕获视频
# cv2.VideoCapture(): 0为默认计算机摄像头， 1可以更换来源
cap = cv.VideoCapture(0)
fps = cap.get(cv.CAP_PROP_FPS)
print(fps)
size = cap.get(3), cap.get(4)
w, h = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(size)
print(w, h)

def save_video(frames, filename):
    output_filename = f'{filename}.mp4'
    video = cv.VideoWriter(
        output_filename,
        cv.VideoWriter_fourcc(*'XVID'),
        30.0,
        (w, h))
    for frame in frames[::-1]:
        video.write(frame)
    cap.release()

record_frames = []
start_saving = False

while(True):
    ret, curr_frame = cap.read()
    # frame = cv.flip(curr_frame, 1)
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # for i  in range(18):
    #     print(i, '-----', cap.get(i))
    cv.imshow('frame', curr_frame)
    key = cv.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    if key & 0xFF == ord('s'):
        start_saving = not start_saving
        if start_saving:
            print('start saving...')
        else:
            print('stop saving...')
            save_video(record_frames, 'test')
            record_frames.clear()
    if start_saving:
        record_frames.append(curr_frame)


cap.release()
cv.destroyAllWindows()