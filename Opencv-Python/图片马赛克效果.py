# _*_ coding: utf-8 _*_
# @Time     : 2019/8/23 17:51
# @Author   : Ole211
# @Site     : 
# @File     : 图片马赛克效果.py    
# @Software : PyCharm

import cv2
import os

os.chdir('d:\\img\\')


def imageMosaic(inputfile, outputfile, step=5):
    '''
    图片马赛克效果
    :param inputfile:
    :param outputfile:
    :return:
    '''
    o = cv2.imread(inputfile)
    img = o.copy()
    w, h = img.shape[:2]
    for i in range(w - step):
        for j in range(h - step):
            if i % step == 0 and j % step == 0:
                for m in range(step):
                    for n in range(step):
                        img[i + m, j + n] = img[i, j]

    cv2.imwrite(outputfile, img)
    cv2.imshow('o', o)
    cv2.imshow('dst', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    imageMosaic('me.jpg', 'dst.jpg')
