# _*_ coding: utf-8 _*_
# @Time     : 2019/4/23 23:53
# @Author   : Ole211
# @Site     : 
# @File     : 17验证码识别.py    
# @Software : PyCharm
import cv2
import numpy as np
import os
os.chdir('d:\\img\\')

def recognize_ocr(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    bin1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    cv2.imshow('binary', thresh)
    cv2.imshow('gray', gray)

if __name__ == '__main__':
    src = cv2.imread('timg.jpg')
    cv2.imshow('src', src)
    recognize_ocr(src)
    cv2.waitKey()
    cv2.destroyAllWindows()