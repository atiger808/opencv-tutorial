# _*_ coding: utf-8 _*_
# @Time     : 2019/8/26 17:12
# @Author   : Ole211
# @Site     : 
# @File     : baidu_OCR.py    
# @Software : PyCharm

from aip import AipOcr
import os
import tkinter as tk
from tkinter import filedialog

APP_ID = '14661593'
API_KEY = 'a1oiSUfK3pmnUkay7zP5cbIy'
SECRET_KEY = 'yp6ogvjeZkoYBqLiB5UkWAyEpKKcgBdI'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filepath):
    with open(filepath, 'rb') as f:
        img = f.read()
    return client.basicAccurate(img)

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    text = get_file_content(filename)['words_result']
    text = ''.join([i['words'] for i in text])
    print(text)
    text = text.split('=')[0]
    if '-' in text:
        a = text.split('-')[0]
        b = text.split('-')[1]
        result = int(a)-int(b)
    elif '+' in text:
        a = text.split('+')[0]
        b = text.split('+')[1]
        result = int(a) + int(b)
    print(result)




