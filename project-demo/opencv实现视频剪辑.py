# _*_ coding: utf-8 _*_
# @Time     : 2019/9/4 16:33
# @Author   : Ole211
# @Site     : 
# @File     : opencv实现视频剪辑.py    
# @Software : PyCharm

import cv2
import tkinter as tk
from tkinter import filedialog



cap = cv2.VideoCapture('d:\\video\\test.mp4')
w, h = int(cap.get(3)), int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
out = cv2.VideoWriter('./output.mp4', fourcc, fps, (w, h))

def saveVideo(records):
    filename = filedialog.asksaveasfilename(title='保存',
                filetypes=[('视频文件', '*.mp4')])
    out = cv2.VideoWriter(filename, fourcc, fps, (w, h))
    for i in records:
        out.write(i)

status = False
records = []
while 1:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    k = cv2.waitKey(300) & 0xff
    if k == ord('a'):
        print('开始录制...')
        status = True
    if status == True:
        records.append(frame)
    if k == ord('s'):
        saveVideo(records)
        print('保存成功')
        records.clear()
        status = False
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
