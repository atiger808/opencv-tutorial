# _*_ coding: utf-8 _*_
# @Time     : 2019/8/29 22:35
# @Author   : Ole211
# @Site     : 
# @File     : delete_water.py
# @Software : PyCharm

import cv2
import os
os.chdir('d:\\img\\img1')
cap = cv2.VideoCapture(0)

def get_water():
    src = cv2.imread('wxlogo.jpg')
    cv2.imshow('src', src)
    while(cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
get_water()
cv2.waitKey(0)
cv2.destroyAllWindows()