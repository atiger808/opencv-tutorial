# _*_ coding: utf-8 _*_
# @Time     : 2019/9/2 16:48
# @Author   : Ole211
# @Site     : 
# @File     : 鼠标框选指定区域马赛克效果.py    
# @Software : PyCharm


from tkinter import filedialog
import tkinter as tk
import cv2
import time
import os

"""
1. 通过操作鼠标框选图片指定区域， 实现马赛克效果
2. 鼠标左键按一下并滑动: 开始框选
3. 鼠标左键松开: 框选成功
4. 鼠标中键按一下：清除框选
5. 按下s键：保存替换好的图片
6. 按下a键：保存框选图片
"""

mode = True
drawing = False
ix, iy = -1, -1
status = [None, None]
pts = []
img = None
rect = None
temp_img = None


def imageMosaic(image, step=10):
    """
    图片马赛克效果函数
    :param image: 输入图片
    :param step: 马赛克的步幅
    :return: 返回马赛克后的图片
    """""
    img = image.copy()
    w, h = img.shape[:2]
    for i in range(w - step):
        for j in range(h - step):
            if i % step == 0 and j % step == 0:
                for m in range(step):
                    for n in range(step):
                        img[i + m, j + n] = img[i, j]
    return img


def draw(event, x, y, flags, param):
    """画图函数"""
    global mode, drawing, ix, iy, pts, img, status, rect, temp_img
    if event == cv2.EVENT_LBUTTONDOWN:
        status.append(1)
        drawing = True
        ix, iy = x, y
        cv2.circle(img, (ix, iy), 5, (0, 0, 0), -1)
        print('down--', ix, iy)
    elif event == cv2.EVENT_LBUTTONUP:
        status.append(0)
        if drawing == True and ix != x and iy != y:
            if mode == True and status[-1] == 0:
                print(status)
                status.clear()
                cv2.rectangle(img, (ix, iy), (x, y), (255, 100, 100), 2)
                cv2.circle(img, (x, y), 5, (0, 0, 0), -1)
                pts = [(ix, iy), (x, y)]
                start_point = min(pts)
                end_point = max(pts)
                rect = o[start_point[1]:end_point[1], start_point[0]:end_point[0]]
                mosaic = imageMosaic(rect)
                img[start_point[1]:end_point[1], start_point[0]:end_point[0]] = mosaic
                temp_img[start_point[1]:end_point[1], start_point[0]:end_point[0]] = mosaic
                cv2.imshow('rect', rect)
                drawing = False
                print('up', x, y)
                print('--' * 30)
                print(pts)
    elif mode == 's':
        filename = filedialog.asksaveasfilename(title='保存',
            filetypes=[("图片文件", "*.jpg")])
        cv2.imwrite(filename, temp_img)
        print('马赛克保存成功')
        mode = True
    elif mode == 'a':
        filename = filedialog.asksaveasfilename(title='保存',
            filetypes=[("图片文件", "*.jpg")])
        cv2.imwrite(filename, rect)
        print('框选保存成功')
        mode = True
    elif event == cv2.EVENT_MBUTTONUP:
        img = o.copy()
        temp_img = o.copy()
        status.clear()


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    print(filename)
    if os.path.splitext(filename)[-1] not in ['.jpg', '.png', '.JPG', '.bmp']:
        print('fail')
    else:
        o = cv2.imread(filename)
        print(type(o))
        img = o.copy()
        temp_img = o.copy()
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('image', draw)
        while (1):
            cv2.imshow('image', img)
            k = cv2.waitKey(1)
            if k == ord('q'):
                break
            elif k == ord('s'):
                mode = 's'
            elif k == ord('a'):
                mode = 'a'
        cv2.destroyAllWindows()
