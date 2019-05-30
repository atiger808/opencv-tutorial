# _*_ coding: utf-8 _*_
# @Time     : 2019/3/6 16:47
# @Author   : Ole211
# @Site     : 
# @File     : 车道线检测.py    
# @Software : PyCharm
import cv2 as cv
import numpy as np
import os
os.chdir('d:\\img\\')


def img_detection(o):
    img = cv.imread(o)
    w, h = img.shape[:2]
    roi = img[int(w/1.7):int(w*0.9), 0:h]
    gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    gaussian_blur = cv.GaussianBlur(gray, (15, 15), 0)
    ret, binary = cv.threshold(gaussian_blur, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    edges = cv.Canny(gray, 150, 200, apertureSize=3)
    print(img.shape)
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=4)
    print(len(lines))
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv.line(roi, (x1, y1), (x2, y2), (0, 0, 255), 2)

    cv.imshow('original', img)
    cv.imshow('roi', roi)
    cv.imshow('gaussian_blur', gaussian_blur)
    cv.imshow('binary', binary)
    cv.imshow('edges', edges)
    cv.waitKey()
    cv.destroyAllWindows()

def lane_detection():
    cap = cv.VideoCapture('road1.mp4')
    fourcc = cv.VideoWriter_fourcc(*'XAVI')
    out = cv.VideoWriter('road_detect.mp4', fourcc, 20.0, (640, 480))
    # img = cv.imread('road.jpg')
    while(1):
        ret, img = cap.read()
        img = cv.flip(img, 1)
        w, h = img.shape[:2]
        roi = img[int(w/1.8):int(w * 0.9), 0:h]
        roi_img = cv.GaussianBlur(roi, (15, 15), 0)
        roi_gray = cv.cvtColor(roi_img, cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(roi_gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

        edges = cv.Canny(roi_gray, 50, 100, apertureSize=3)
        lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=10, maxLineGap=4)
        if lines is not None:
            for line in lines:
                print(line)
                x1, y1, x2, y2 = line[0]
                cv.line(roi, (x1, y1), (x2, y2), (0, 255, 0), 4)

        cv.imshow('original', img)
        cv.imshow('roi_gray', roi_gray)
        cv.imshow('binary', binary)
        cv.imshow('edges', edges)
        k = cv.waitKey(40) & 0xFF
        if k == 27:
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    # img_detection('road.jpg')
    lane_detection()