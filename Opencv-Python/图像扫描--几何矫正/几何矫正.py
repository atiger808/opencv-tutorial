# _*_ coding: utf-8 _*_
# @Time     : 2019/8/13 20:57
# @Author   : Ole211
# @Site     : 
# @File     : 几何矫正.py    
# @Software : PyCharm

from imutils.perspective import four_point_transform
import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math


def Get_outline(input_dir):
    image = cv2.imread(input_dir)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 75, 200)
    return image, gray, edged


def Get_cnt(edged):
    cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    doCnt = None

    if len(cnts) > 0:
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        cv2.drawContours(img, cnts, -1, [0, 0, 255], 3)
        for c in cnts:
            # 轮廓周长cv2.arcLength()
            peri = cv2.arcLength(c, True)
            #  cv2.aprroxPolyDP(cnt, epsilon， True)  # 用于获得轮廓的近似值,使用cv2.drawCountors进行画图操作
            # 参数说明：cnt为输入的轮廓值， epsilon为阈值T，通常使用轮廓的周长作为阈值，True表示的是轮廓是闭合的
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            print(len(approx))
            print(approx)
            if len(approx) == 4:
                doCnt = approx
                break
    return doCnt


def calculate_distance(point1, point2):
    d_x = point1[0] - point2[0]
    d_y = point1[1] - point2[1]
    distance = math.sqrt(d_x ** 2 + d_y ** 2)
    return distance


if __name__ == '__main__':
    import os

    os.chdir('d:\\img\\')
    img, gray, edge = Get_outline('gongjiaoka.png')
    doCnt = Get_cnt(edge)
    # 对原始图像进行四点透视变换
    result_img = four_point_transform(img, doCnt.reshape(4, 2))
    # 反转
    # result_img = cv2.flip(result_img, -1)
    # result_img = cv2.transpose(result_img)

    # 改变变换的模式， 公交卡的比例的16:9
    pts1 = np.float32(doCnt.reshape(4, 2))
    p = doCnt.reshape(4, 2)
    if calculate_distance(p[0], p[1]) < calculate_distance(p[0], p[3]):
        pts2 = np.float32([[0, 0], [0, 180], [320, 180], [320, 0]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(img, M, (320, 180))
    else:
        pts2 = np.float32([[0, 0], [0, 320], [180, 320], [180, 0]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(img, M, (180, 320))
    cv2.imwrite('0.png', dst)
    cv2.imshow('dst', dst)

    # 画点
    for point in doCnt.reshape(4, 2):
        cv2.circle(img, tuple(point), 2, (0, 255, 0), 2)
    print(doCnt)
    cv2.imshow('original', img)
    cv2.imshow('gray', gray)
    cv2.imshow('edge', edge)
    cv2.imshow('result_img', result_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
