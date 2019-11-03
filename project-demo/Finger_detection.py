# _*_ coding: utf-8 _*_
# @Time     : 2019/9/17 18:09
# @Author   : Ole211
# @Site     : 
# @File     : Finger_detection.py    
# @Software : PyCharm

import numpy as np
import cv2
import copy
import math

# variables
isBgCaptured = 0   # bool, whether the background captured
triggerSwitch = False

def nothing(x):
    print('threshold: ' + str(x))


def calculateFingers(res, drawing):  # -> finished bool, cnt: finger count
    #  convexity defect
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(res, hull)
        if type(defects) != type(None):  # avoid crashing.   (BUG not found)

            cnt = 0
            for i in range(defects.shape[0]):  # calculate the angle
                s, e, f, d = defects[i][0]
                start = tuple(res[s][0])
                end = tuple(res[e][0])
                far = tuple(res[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                    cnt += 1
                    cv2.circle(drawing, far, 8, [211, 84, 0], -1)
            return True, cnt
    return False, 0


cap = cv2.VideoCapture(0)
cap.set(10, 200)
cv2.namedWindow('trackbar')
cv2.createTrackbar('trh1', 'trackbar', 60, 100, nothing)
fgbg = cv2.createBackgroundSubtractorMOG2(0, 50)

while True:
    ret, frame = cap.read()
    threshold = cv2.getTrackbarPos('trh1', 'trackbar')
    frame = cv2.bilateralFilter(frame, 5, 50, 100)
    frame = cv2.flip(frame, 1)
    w, h = frame.shape[:2]
    cv2.rectangle(frame, (int(0.5 * h), 0), (h, int(0.8 * w)), (255, 0, 0), 2)
    cv2.imshow('frame', frame)

    fgmask = fgbg.apply(frame)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    img = cv2.bitwise_and(frame, frame, mask=fgmask)
    img = img[0:int(0.8 * w), int(0.5 * h):h]
    cv2.imshow('mask', img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (41, 41), 0)
    cv2.imshow('blur', blur)
    ret, thresh = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow('thresh', thresh)

    thresh1 = copy.deepcopy(fgmask)
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    length = len(contours)
    maxArea = -1
    if length > 0:
        contours = sorted(contours, key=cv2.contourArea, reverse=True)
        res = contours[0]
        hull = cv2.convexHull(res)
        drawing = np.zeros(img.shape, np.uint8)
        cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
        cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

        isFinishCal, cnt = calculateFingers(res, drawing)
        if triggerSwitch is True:
            if isFinishCal is True and cnt <= 2:
                print(cnt)
                # app('System Events').keystroke(' ')  # simulate pressing blank space
    cv2.imshow('ouput', drawing)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
