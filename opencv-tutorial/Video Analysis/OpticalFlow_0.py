# _*_ coding: utf-8 _*_
# @Time     : 2019/9/16 17:30
# @Author   : Ole211
# @Site     : 
# @File     : OpticalFlow_0.py    
# @Software : PyCharm

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# 查找shi-tomasi角点需要的参数
feature_params = dict(
    maxCorners=100,  # 最大角点数
    qualityLevel=0.3,  # 角点的质量阈值
    minDistance=7,  # 相邻角点间最小距离
    blockSize=7  # 邻域大小
)
# 调用Lucas kanade函数需要的参数
lk_params = dict(
    winSize=(15, 15),  # 邻域大小
    maxLevel=2,  # 图像金字塔层数
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)  # 迭代终止条件
)
# 设置随机颜色
color = np.random.randint(0, 255, (100, 3))

ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
# 找到角点
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
# 创建一个掩膜
mask = np.zeros_like(old_frame)

while (1):
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 执行calcOpticalFlowPyrLK函数， 返回新的角点，角点状态
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    # 选择找到的角点
    good_new = p1[st == 1]
    good_old = p0[st == 1]
    # 画框
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        frame = cv2.circle(frame, (a, b), 5, (0, 0, 255), -1)
    img = cv2.add(frame, mask)
    rows, cols = img.shape[:2]
    # 90度旋转
    M = cv2.getRotationMatrix2D((cols // 2, rows // 2), -90, 1)
    img = cv2.warpAffine(img, M, (cols, rows))

    # img = cv2.flip(img, -1) # 翻转

    cv2.imshow('frame', img)
    k = cv2.waitKey(20) & 0xff
    if k == 27:
        break

    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
cap.release()
cv2.destroyAllWindows()
