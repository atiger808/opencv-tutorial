# _*_ coding: utf-8 _*_
# @Time     : 2019/5/12 17:54
# @Author   : Ole211
# @Site     : 
# @File     : spider.py    
# @Software : PyCharm

'''
获取cookies 获取django 表单验证 csrf
'''

import requests

url = 'http://127.0.0.1:8000/book_add/'
s = requests.session()

print(s.cookies.get_dict())

res = s.get(url)
cookies = s.cookies.get_dict()
print(cookies)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',

}

data = {
    'name': '平凡的世界',
    'author': '路遥',
    'csrfmiddlewaretoken': cookies['csrftoken']
}
res2 = s.post('http://127.0.0.1:8000/book_add/', headers=headers, data=data)

print('----'*30)
# print(res2.text)
print(res2.headers)
print(res2)
print(s.cookies.get_dict())

