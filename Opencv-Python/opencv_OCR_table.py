# _*_ coding: utf-8 _*_
# @Time     : 2019/4/14 14:01
# @Author   : Ole211
# @Site     : 
# @File     : opencv_OCR_table.py    
# @Software : PyCharm

import cv2
import numpy as np
import os
import pytesseract
from aip import AipOcr

APP_ID = '14661593'
API_KEY = 'a1oiSUfK3pmnUkay7zP5cbIy'
SECRET_KEY = 'yp6ogvjeZkoYBqLiB5UkWAyEpKKcgBdI'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    '''
    读取图片
    :param filePath:
    :return:
    '''
    with open(filePath, 'rb') as fp:
        img = fp.read()
    content = client.basicAccurate(img)['words_result']
    content = '\n'.join([i['words'] for i in content])
    return content


os.chdir('d:\\img\\')

# 横向直线检测
def HorizontalLineDetect(gray_img):
    # 图像二值化
    ret, threshold = cv2.threshold(gray_img, 240, 255, cv2.THRESH_BINARY)
    # 进行两次中值滤波， 模板大小3*3
    blur = cv2.medianBlur(threshold, 3)
    blur = cv2.medianBlur(blur, 3)
    h, w = gray_img.shape
    # 横向直线列表
    horizontal_lines = []
    for i in range(h - 1):
        # 找到两条记录的分割线段， 以相邻两行的平均像素差大于120为标准
        if abs(np.mean(blur[i, :]) - np.mean(blur[i+1, :])) > 120:
            horizontal_lines.append([0, i, w, i])
            # 在图像上绘制线段
            cv2.line(img, (0, i), (w, i), (0, 255, 0), 2)
    horizontal_lines = horizontal_lines[1:]
    return horizontal_lines

# 纵向直线检测
def VerticalLineDetect(gray_img):
    # Canny 边缘检测
    edges = cv2.Canny(gray_img, 30, 240)
    # Hough 直线检测
    minLineLength = 500
    maxLineGap = 30
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap).tolist()
    lines.append([[13, 937, 13, 102]])
    lines.append([[756, 937, 756, 102]])
    sorted_lines = sorted(lines, key=lambda x: x[0])
    # 纵向直线列表
    vertical_lines = []
    for line in sorted_lines:
        for x1, y1, x2, y2 in line:
            print(line)
            # 在图像上绘制纵向直线
            if x1 == x2:
                vertical_lines.append((x1, y1, x2, y2))
                cv2.line(img, (x1, y1),(x2, y2), (0, 255, 0), 2)
    return vertical_lines

# 顶点检测
def VertexDetect(gray_img):
    vertical_lines = VerticalLineDetect(gray_img)
    horizontal_lines = HorizontalLineDetect(gray_img)
    # 顶点列表
    vertex  = []
    for v_line in vertical_lines:
        for h_line in horizontal_lines:
            print(v_line)
            print(h_line)
            vertex.append((v_line[0], h_line[1]))
    # 绘制顶点
    for point in vertex:
        cv2.circle(img, point, 1, (255, 0, 0), 2)
    return vertex

# 寻找单元格区域
def CellDetect(gray_img):
    vertical_lines = VerticalLineDetect(gray_img)
    horizontal_lines = HorizontalLineDetect(gray_img)
    # 顶点列表
    rects = []
    for i in range(0, len(vertical_lines) - 1, 2):
        for j in range(len(horizontal_lines) - 1):
            rects.append((vertical_lines[i][0], horizontal_lines[j][1],
                          vertical_lines[i + 1][0], horizontal_lines[j + 1][1]))
    return rects

# 识别单元格中的文字
def OCR(gray_img):
    rects = CellDetect(gray_img)
    thresh =gray_img
    # 特殊字符列表
    special_char_list = ' `~!@#$%^&*()_-=+[]{}|\;:,.《》、？‘’'
    # all_text = pytesseract.image_to_string(gray_img, config='--psm 7', lang='chi_sim')
    # all_text = ''.join([char for char in all_text if char not in special_char_list])
    # print(all_text)
    for i in range(20):
        try:
            rect1 = rects[i]
            DetectImage1 = thresh[rect1[1]:rect1[3], rect1[0]:rect1[2]]
            # Tesseract所在的路径
            pytesseract.pytesseract.tesseract_cmd = r'c:\Users\Administrator\AppData\Local\Tesseract-OCR\tesseract.exe'
            # 识别数字,每行第一列
            text1 = pytesseract.image_to_string(DetectImage1, config='--psm 10')
            print(text1, end='-->')

            # 识别汉字， 每行第二列
            rect2 = rects[i + 20]
            DetectImage2 = thresh[rect2[1]:rect2[3], rect2[0]:rect2[2]]
            text2 = pytesseract.image_to_string(DetectImage2, config='--psm 7', lang='chi_sim')
            text2 = ''.join([char for char in text2 if char not in special_char_list])
            print(text2, end='-->')

            # 识别汉字 第三列
            rect3 = rects[i + 40]
            DetectImage3 = thresh[rect3[1]:rect3[3], rect3[0]:rect3[2]]
            text3 = pytesseract.image_to_string(DetectImage3, config='--psim 7', lang='chi_sim')
            text3 = ''.join([char for char in text3 if char not in special_char_list])
            print(text3)

        except Exception as e:
            print('error----', e)
            continue


content = get_file_content('AI.jpg')
print(content)


img = cv2.imread('AI.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

HorizontalLineDetect(gray_img)
VerticalLineDetect(gray_img)
VertexDetect(gray_img)
OCR(gray_img)
cv2.imshow('origimal', img)
# cv2.imshow('edges', edges)
cv2.waitKey()
cv2.destroyAllWindows()

