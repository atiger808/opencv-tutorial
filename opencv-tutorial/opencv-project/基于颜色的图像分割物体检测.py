# _*_ coding: utf-8 _*_
# @Time     : 2019/4/2 1:43
# @Author   : Ole211
# @Site     : 
# @File     : 基于颜色的图像分割物体检测.py    
# @Software : PyCharm
import cv2
import numpy as np
import os
os.chdir('d:\\img\\')

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey()
    cv2.destroyAllWindows()

def grayscale_17_levels(gray):
    high = 255
    while(1):
        low = high - 15
        col_to_be_changed_low = np.array([low])
        col_to_be_changed_high = np.array([high])
        curr_mask = cv2.inRange(gray,
                col_to_be_changed_low, col_to_be_changed_high)
        gray[curr_mask>0] = (high)
        high -= 15
        if(low==0):
            break

def get_area_of_each_level(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output = []
    first = True
    high = 255
    while(1):
        low = high - 15
        if(first == False):
            to_be_black_again_low = np.array([high])
            to_be_black_again_high = np.array([255])
            curr_mask = cv2.inRange(image, to_be_black_again_low,
                                    to_be_black_again_high)
            image[curr_mask>0] = [0]
        ret, threshold = cv2.threshold(image, low, 255, 0)
        im, contours, hirerchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        if(len(contours)>0):
            output.append([cv2.contourArea(contours[0])])
            cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
            cv2.imshow('img', img)
        high -= 15
        first = False
        if(low==0):
            break
    cv2.waitKey()
    cv2.destroyAllWindows()
    return output
if __name__ == '__main__':

    img = cv2.imread('leaf.jpg')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    viewImage(hsv_img)

    green_low = np.array([45, 100, 50])
    green_high = np.array([75, 255, 255])
    curr_mask = cv2.inRange(hsv_img, green_low, green_high)
    hsv_img[curr_mask>0] = ([75, 255, 200])
    viewImage(hsv_img)

    RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(RGB_again, cv2.COLOR_BGR2GRAY)
    viewImage(gray)

    ret, threshold = cv2.threshold(gray, 90, 255, 0)
    viewImage(threshold)

    _, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_area_list = [(cv2.contourArea(cnt), cnt) for cnt in contours]
    contour_area_list_sort = sorted(contour_area_list, key=lambda x:x[0])
    max_contour = contour_area_list_sort[-1][1]
    # print(contour_area_list)
    print(contour_area_list_sort[-1][0])
    cv2.drawContours(img, max_contour, -1, (0, 0, 255), 3)

    M = cv2.moments(max_contour)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    x, y, w, h = cv2.boundingRect(max_contour)
    cv2.circle(img, (cx, cy),20, (0, 0, 255), -1)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
    box = cv2.minAreaRect(max_contour)
    print(box)
    viewImage(img)



    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # grayscale_17_levels(gray)
    # viewImage(gray)
    # output = get_area_of_each_level(img)
    # print(output)
