# _*_ coding: utf-8 _*_
# @Time     : 2019/8/14 13:22
# @Author   : Ole211
# @Site     : 
# @File     : 噪音下提取图像轮廓.py    
# @Software : PyCharm
import cv2
import os
import math
import numpy as np
import tkinter as tk
from tkinter import filedialog
os.chdir('d:\\img\\')

# 身份证大小为长85.6mm*宽54mm，换算成成像素为240*151像素。
ROWS, COLS = 151, 240
original_img = None

# 计算两点之间距离函数
def calculate_distance(point1, point2):
    d_x = point1[0] - point2[0]
    d_y = point1[1] - point2[1]
    distance = math.sqrt(d_x**2 + d_y**2)
    return int(distance)

def get_four_point(input_dir):
    global original_img
    original_img = cv2.imread(input_dir)
    original_img = cv2.resize(original_img, (0, 0), fx=0.5, fy=0.5)
    img = original_img.copy()
    h, w = img.shape[:2]
    print(h, w)
    cv2.imshow('original', img)

    # 模糊处理
    blured = cv2.blur(img, (5, 5))
    # cv2.imshow('blur', blured)

    # 进行泛洪填充
    mask = np.zeros((h+2, w+2), np.uint8)
    cv2.floodFill(blured, mask, (w-1, h-1), (255, 255, 255), (2, 2, 2), (3, 3, 3), 8)
    cv2.imshow('floodfill', blured)

    # 得到灰度图
    gray = cv2.cvtColor(blured, cv2.COLOR_BGR2GRAY)
    gray = 255 - gray
    cv2.imshow('gray', gray)
    # 形态学转换
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
    opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)


    # 二值化图
    ret, binary = cv2.threshold(opened, 30, 255, cv2.THRESH_BINARY)
    cv2.imshow('binary', binary)

    # 找图像轮廓
    cnts, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    cv2.drawContours(img, cnts[0], -1, (0, 0, 255), 2)

    # 找出轮廓的多边形拟合曲线函数： approxPolyDP(contourMat, approxCurve, 10, true)
    # 第一个参数
    # InputArray
    # curve：输入的点集
    # 第二个参数OutputArray
    # approxCurve：输出的点集，当前点集是能最小包容指定点集的。画出来即是一个多边形。
    # 第三个参数double
    # epsilon：指定的精度，也即是原始曲线与近似曲线之间的最大距离。
    # 第四个参数bool
    peri = cv2.arcLength(cnts[0], True)
    approx = cv2.approxPolyDP(cnts[0], 0.1*peri, 10, True)
    if len(approx) == 4:
        return approx, cnts, img
    return None, cnts, img

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    imgname = filedialog.askopenfilename()
    approx, cnts, img = get_four_point(imgname)
    if approx is None:
        print('fail')
    else:
        pts1 = np.float32(approx.reshape(4, 2))
        rows, cols = calculate_distance(pts1[0], pts1[1]), calculate_distance(pts1[0], pts1[3])
        # 图像透视变换
        if cols>rows:
            cols, rows = COLS, ROWS
            pts2 = np.float32([[0, 0], [0, rows], [cols, rows], [cols, 0]])
            M = cv2.getPerspectiveTransform(pts1, pts2)
            print(pts1)
            print(pts2)
            dst = cv2.warpPerspective(original_img, M, (cols, rows))
        else:
            cols, rows = ROWS, COLS
            pts2 = np.float32([[0, 0], [0, cols], [rows, cols], [rows, 0]])
            pts1 = np.float32([pts1[3], pts1[0], pts1[1], pts1[2]])
            M = cv2.getPerspectiveTransform(pts1, pts2)
            print('*'*30)
            print(pts1)
            print(pts2)
            dst = cv2.warpPerspective(original_img, M, (rows, cols))
        cv2.imshow('dst', dst)
        for point in approx.reshape(4, 2):
            cv2.circle(img, tuple(point), 5, (0, 255, 0), -1)
    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

