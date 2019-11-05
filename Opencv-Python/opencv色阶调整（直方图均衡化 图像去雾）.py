# _*_ coding: utf-8 _*_
# @Time     : 2019/8/29 0:17
# @Author   : Ole211
# @Site     : 
# @File     : opencv色阶调整（直方图均衡化 图像去雾）.py    
# @Software : PyCharm

import cv2
import numpy as np
import os
from run_time import run_time as run
os.chdir('d:\\img\\img1\\')

'''
文章目录
一、色阶调整( Levels Adjustment )原理
二、自动色阶图像处理算法
三、色阶调整( Levels Adjustment )原理
色阶：就是用直方图描述出的整张图片的明暗信息。如图
从左至右是从暗到亮的像素分布，
黑色三角代表最暗地方（纯黑—黑点值为０），
白色三角代表最亮地方（纯白—白点为 255）。
灰色三角代表中间调。（灰点为1.00）
'''

# 1 直方图均值化， 读取的必须为灰度图像
# img = cv2.imread('flog2.png', 0)
# equ = cv2.equalizeHist(img)
#
# res = np.hstack((img, equ))
# cv2.imshow('res', res)

'''
二、自动色阶图像处理算法
cv2.createCLAHE() 对比度有限自适应直方图均衡
直方图均衡后背景对比度有所改善。但导致亮度过高，我们丢失了大部分信息。这是因为它的直方图并不局限于特定区域。
因此，为了解决这个问题，使用自适应直方图均衡。在此，图像被分成称为“图块”的小块（在OpenCV中，tileSize默认为8x8）。
然后像往常一样对这些块中的每一个进行直方图均衡。所以在一个小区域内，直方图会限制在一个小区域（除非有噪音）。如果有噪音，它会被放大。
为避免这种情况，应用对比度限制。如果任何直方图区间高于指定的对比度限制（在OpenCV中默认为40），
则在应用直方图均衡之前，将这些像素剪切并均匀分布到其他区间。均衡后，为了去除图块边框中的瑕疵，应用双线性插值。
'''
# img2 = cv2.imread('flog1.png', 0)
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# cl1 = clahe.apply(img)
#
# cv2.imshow('cl1', cl1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''
三，自适应色阶去雾气
'''
import numpy as np
import cv2
import os


def ComputeHist(img):
    h, w = img.shape
    hist, bin_edge = np.histogram(img.reshape(1, w * h), bins=list(range(257)))
    return hist


def ComputeMinLevel(hist, rate, pnum):
    sum = 0
    for i in range(256):
        sum += hist[i]
        if (sum >= (pnum * rate * 0.01)):
            return i


def ComputeMaxLevel(hist, rate, pnum):
    sum = 0
    for i in range(256):
        sum += hist[255 - i]
        if (sum >= (pnum * rate * 0.01)):
            return 255 - i


def LinearMap(minlevel, maxlevel):
    if (minlevel >= maxlevel):
        return []
    else:
        newmap = np.zeros(256)
        for i in range(256):  # 获取阈值外的像素值 i< minlevel，i> maxlevel
            if (i < minlevel):
                newmap[i] = 0
            elif (i > maxlevel):
                newmap[i] = 255
            else:
                newmap[i] = (i - minlevel) / (maxlevel - minlevel) * 255
        return newmap

@run
def CreateNewImg(img):
    h, w, d = img.shape
    newimg = np.zeros([h, w, d])
    for i in range(d):
        imgmin = np.min(img[:, :, i])
        imgmax = np.max(img[:, :, i])
        imghist = ComputeHist(img[:, :, i])
        minlevel = ComputeMinLevel(imghist, 8.3, h * w)
        maxlevel = ComputeMaxLevel(imghist, 2.2, h * w)
        newmap = LinearMap(minlevel, maxlevel)
        if (newmap.size == 0):
            continue
        for j in range(h):
            newimg[j, :, i] = newmap[img[j, :, i]]
    return newimg.astype('uint')


def videoConvert(videofile):
    cap = cv2.VideoCapture(videofile)
    # 视频宽高
    w, h = int(cap.get(3)), int(cap.get(4))
    # 视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 视频编码
    fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
    # 定义输出
    out = cv2.VideoWriter('d:\\video\\dst\\road4_nofog.avi', fourcc, fps, (w, h), True)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            newframe = CreateNewImg(frame)
            newframe = newframe.astype('uint8')
            cv2.imshow('frame', frame)
            cv2.imshow('dst', newframe)
            print(frame.dtype)
            print(newframe.dtype)
            out.write(newframe)
            if cv2.waitKey(20) & 0xff == ord('q'):
                break
        else:
            print('no frame')
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    img = cv2.imread('d:\\img\\flog2.jpg')
    dst = CreateNewImg(img)
    dst = dst.astype('uint8')
    merge = np.hstack((img, dst))
    print(dst.shape)
    cv2.imshow('merge', merge)
    # cv2.imwrite('d:\\img\\road2_dst.jpg', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # videoConvert('d:\\video\\src\\road4.mp4')

if __name__ == '__main__':
    main()
