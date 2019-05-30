# _*_ coding: utf-8 _*_
# @Time     : 2019/4/24 9:24
# @Author   : Ole211
# @Site     : 
# @File     : 18旋转文本校正.py    
# @Software : PyCharm

import cv2
import numpy as np
import os

os.chdir('d:\\img\\')

def rotated(src):
    # base_img = cv2.imread('paper_base.jpg', 0)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # diff_gray = cv2.absdiff(base_img, gray)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    # thresh = cv2.erode(thresh, kernel, iterations=1)
    # thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    coords = np.column_stack(np.where(thresh>0))
    cv2.imshow('coords', coords)
    angle = cv2.minAreaRect(coords)[-1]
    print(angle)


    if angle < -45:
        angle = -(90+angle)
    else:
        angle = angle

    h, w = src.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(src, M, (w, h),flags = cv2.INTER_CUBIC,
                                            borderMode = cv2.BORDER_REFLECT)
    # cv2.putText(rotated, 'Angle:')

    cv2.imshow('src', src)
    cv2.imshow('rotated', rotated)
    # cv2.imshow('diff', diff_gray)
    cv2.imshow('thresh', thresh)



if __name__ == '__main__':
    src = cv2.imread('circle3.jpg')
    cv2.imshow('src', src)
    rotated(src)
    print('ok')
    cv2.waitKey()
    cv2.destroyAllWindows()