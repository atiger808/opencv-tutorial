# _*_ coding: utf-8 _*_
# @Time     : 2019/4/3 16:45
# @Author   : Ole211
# @Site     : 
# @File     : autojump.py    
# @Software : PyCharm
import cv2
import numpy as np
import os
import time
import subprocess
import math
# os.chdir('d:\\img\\')

press_coefficient = 1.35

def get_center_coord(img):
    region_lower = int(img.shape[0]*0.3)
    region_upper = int(img.shape[0]*0.7)
    region = img[region_lower:region_upper]

    hsv_img = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    color_lower = np.array([105, 25, 45])
    color_upper = np.array([135, 125, 130])
    color_mask = cv2.inRange(hsv_img, color_lower, color_upper)

    _, contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours)>0:
        max_contour = max(contours, key=cv2.contourArea)
        rect = cv2.boundingRect(max_contour)
        x, y, w, h = rect
        cv2.rectangle(region, (x, y), (x+w, y+h), (0, 255, 0), 3)
        center_coord = (x+int(w/2), y+h-20)
        cv2.circle(region, center_coord, 8, (0, 0, 255), -1)
        cv2.drawContours(region, max_contour, -1, (0, 0, 255), 3)
    # region = cv2.resize(region, (400, 800))
    # cv2.imshow('color_mask', color_mask)
    # cv2.imshow('region', region)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return hsv_img, color_mask, center_coord

def get_box_center(img):
    region_lower = int(img.shape[0] * 0.3)
    region_upper = int(img.shape[0] * 0.7)
    region = img[region_lower:region_upper]
    gray_img = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray_img)
    canny_img = cv2.Canny(gray_img, 75, 150)
    y_top = np.nonzero([max(row) for row in canny_img[:400]])[0][0]
    x_top = int(np.mean(np.nonzero(canny_img[y_top])))
    y_bottom = y_top + 200
    # for row in range(y_bottom, 768):
    #     if canny_img[row, x_top] != 0:
    #         break
    box_center_coord  = (x_top, (y_top + y_bottom)//2)
    cv2.circle(region, box_center_coord, 8, (0, 0, 255), -1)
    return canny_img, region, box_center_coord

def pullScreenshot():
    os.system('adb shell screencap -p /sdcard/autojump.png')
    os.system('adb pull /sdcard/autojump.png .')

def jump(distance):
    press_time = distance * 1.35
    press_time = int(press_time)
    cmd = 'adb shell input swipe 320 410 320 410 ' + str(press_time)
    print(cmd)
    os.system(cmd)

def beginJump():
    while True:
        pullScreenshot()
        time.sleep(2)
        img = cv2.imread('autojump.png')
        color_mask, hsv_img, center_coord = get_center_coord(img)
        canny_img, region, box_center_coord = get_box_center(img)
        distance = math.sqrt((box_center_coord[0] - center_coord[0]) ** 2 + (box_center_coord[1] - center_coord[1]) ** 2)
        w, h = region.shape[:2]
        text = 'press time: %.3f ms' %(max(1.35*distance, 200))
        cv2.putText(region, text, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        text0 = 'distance: %.3f pixels' % (distance)
        cv2.putText(region, text0, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.line(region, center_coord, box_center_coord, (0, 0, 255), 3)
        print('棋子坐标：', center_coord)
        print('盒子坐标：', box_center_coord)
        print('距离：', distance)

        cv2.imwrite('region.png', region)

        # cv2.imshow('color_mask', color_mask)
        # cv2.imshow('hsv_img', hsv_img)
        # cv2.imshow('canny_img', canny_img)
        # cv2.imshow('region', region)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        jump(distance)
        time.sleep(0.2)


if __name__ == '__main__':
    beginJump()
    # pullScreenshot()

# if __name__ == '__main__':
#     get_center_coord()