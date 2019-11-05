# _*_ coding: utf-8 _*_
# @Time     : 2019/9/2 10:53
# @Author   : Ole211
# @File     : Meanshift_in_opencv.py
# @Software : PyCharm

'''
cv2.calcHist()的使用
定义
cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate ]]) ->hist

images:输入的图像
channels:选择图像的通道
mask:掩膜，是一个大小和image一样的np数组，其中把需要处理的部分指定为1，不需要处理的部分指定为0，一般设置为None，表示处理整幅图像
histSize:使用多少个bin(柱子)，一般为256
ranges:像素值的范围，一般为[0,255]表示0~255
后面两个参数基本不用管。
注意，除了mask，其他四个参数都要带[]号。
'''

import numpy as np
import cv2


cap = cv2.VideoCapture('d:\\video\\src\\road.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
size = int(cap.get(3)), int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./tmp/output_camshift.mp4', fourcc, fps, size, True)

# 获取视频的第一帧
ret, frame = cap.read()
# 设置初始化窗口位置
r, h, c, w = 380, 100, 180, 100
track_window = (c, r, w, h)
# 设置跟踪初始兴趣区域
roi = frame[r:r + h, c:c + w]
# 转为hsv格式
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
# 颜色直方图
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
# 归一化
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# 确定窗口搜索停止的准则， 迭代次数达到设置的最大值， 或者窗口中心的漂移值小于设定值
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
while 1:
    ret, frame = cap.read()
    if ret is True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # 直方图反向投影
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        # 返回迭代次数和更新后的边框
        ret1, track_window = cv2.meanShift(dst, track_window, term_crit)
        print(ret)
        x, y, w, h = track_window
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.circle(frame, (x + w // 2, y + h // 2), 5, (0, 0, 255), -1)
        cv2.imshow('frame', frame)
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite('./tmp/' + chr(k) + '.jpg', frame)
            out.write(frame)
    else:
        break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
cap = cv2.VideoCapture('d:\\video\\road2.mp4')
FPS = cap.get(cv2.CAP_PROP_FPS)
SIZE = int(cap.get(3)), int(cap.get(4))
W, H = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./tmp/output_meanshift.mp4', fourcc, FPS, SIZE, True)
'''
