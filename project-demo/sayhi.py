# _*_ coding: utf-8 _*_
# @Time     : 2019/9/21 9:16
# @Author   : Ole211
# @Site     : 
# @File     : sayhi.py    
# @Software : PyCharm

import os
import pygame

pygame.mixer.init()
track = pygame.mixer.music.load(r'E:\mp3\云朵 - 我的楼兰.mp3')
track.play()