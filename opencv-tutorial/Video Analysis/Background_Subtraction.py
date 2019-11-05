# _*_ coding: utf-8 _*_
# @Time     : 2019/9/3 3:11
# @Author   : Ole211
# @Site     : 
# @File     : Background_Subtraction.py    
# @Software : PyCharm

import numpy as np
import cv2

cap = cv2.VideoCapture('d:\\video\\src\\road2.mp4')

# fgbg = cv2.bgsegm.createBackgroundSubstractorMOG()
# fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()

while 1:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

'''

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
'''
