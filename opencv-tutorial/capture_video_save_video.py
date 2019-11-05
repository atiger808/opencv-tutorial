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
import time


'''
这是因为没有编码库造成的原因，去它提示的链接，也就是https://github.com/cisco/openh264/releases，下载对应版的openh264，注意位数不要选错了，比如我的就是64位的Python，Windows，就下载openh264-1.7.0-win64.dll.bz2这个压缩包。下载完之后，解压到你的py文件所在目录，再次运行就不会报错。
————————————————
版权声明：本文为CSDN博主「原我归来是少年」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/DumpDoctorWang/article/details/80515861
'''
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('d:\\video\\output.avi', fourcc, 15.0, (640, 480), True)

time.sleep(3)
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
