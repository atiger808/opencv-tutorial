# _*_ coding: utf-8 _*_
# @Time     : 2019/8/30 22:03
# @Author   : Ole211
# @Site     : 
# @File     : qq_record_wordcloud.py    
# @Software : PyCharm
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba

def get_qq_Record(filename):
    word = []
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.readlines()
    for line in content:
        tmp = line[:4]
        if (tmp == '消息记录' or tmp == '消息分组' or
           tmp == '2018' or tmp == '2019' or
           tmp == '消息对象' or
            '消息记录' in line or '=' in line):
           continue
        word.append(line)
    text = str(word).replace('[表情]', '').replace('[图片]', '')
    return text

def splitWord(text):
    '''jieba分词'''
    word_jieba = jieba.cut(text, cut_all=True)
    return ' '.join(word_jieba)

def drawImage(word_split, back_image):
    '''绘制云图'''
    color_mask = np.array(Image.open(back_image))
    wc = WordCloud(
        background_color = 'black',
        max_words = 2000,
        mask = color_mask,
        max_font_size = 40,
        font_path = r'C:\Windows\Fonts\msyh.ttf'
    )
    wc.generate(word_split)
    wc.to_file('d:\\qq_wc.png')

if __name__ == '__main__':
    text = get_qq_Record('d:\\Python Vip 13班.txt')
    word_split = splitWord(text)
    drawImage(word_split, 'd:\\img\\ff.jpg')