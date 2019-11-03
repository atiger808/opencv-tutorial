# _*_ coding: utf-8 _*_
# @Time     : 2019/9/4 14:12
# @Author   : Ole211
# @Site     : 
# @File     : opencv+PIL实现录屏.py
# @Software : PyCharm

from PIL import ImageGrab
import numpy as np
import cv2
import time

screenshot = ImageGrab.grab()
w, h = screenshot.size
print(w, h)
k = np.zeros((200, 200), np.uint8)
kwindow = cv2.namedWindow('k', cv2.WINDOW_AUTOSIZE)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 10
filename = 'd:\\video\\record_'+str(int(time.time())) + '.mp4'
video = cv2.VideoWriter(filename, fourcc, fps, (w, h), True)

print('5秒后开始录屏')
for i in range(5):
    print(i)
    time.sleep(1)

while True:
    img = ImageGrab.grab()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    video.write(img)
    cv2.imshow(kwindow, k)
    time.sleep(int(1/fps))
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
video.release()
cv2.destroyAllWindows()