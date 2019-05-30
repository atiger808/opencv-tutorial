# _*_ coding: utf-8 _*_
# @Time     : 2019/3/4 16:21
# @Author   : Ole211
# @Site     : 
# @File     : template_match.py    
# @Software : PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:\\img\\')

img = cv2.imread('game_cat.jpg', 0)
img2 = img.copy()
template = cv2.imread('cat.png', 0)
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, 255, 2)

    plt.subplot(121)
    plt.imshow(res, cmap='gray')
    plt.title('Matching Result')
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(img, cmap='gray')
    plt.title('Detect Point')
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    plt.suptitle(meth)
    plt.show()