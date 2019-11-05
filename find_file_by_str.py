# _*_ coding: utf-8 _*_
# @Time     : 2019/9/27 15:36
# @Author   : Ole211
# @Site     : 
# @File     : find_file_by_str.py    
# @Software : PyCharm

import os
import sys



print(os.path.abspath('./'))
for r, d, f in os.walk(os.path.abspath('./')):
    for i in os.listdir(r):
        if os.path.splitext(i)[-1] == '.py':
            fullpath = os.path.join(r, i)
            with open(fullpath, 'r', errors='ignore') as fp:
                content = fp.read()
                if 'me.jpg' in content:
                    print(fullpath)
            # if os.path.splitext(i)[-1] == '.py':
            #     print(i)
    # for file in f:
    #     if os.path.isfile(file) and os.path.splitext(file)[-1] == '.py':
    #         print(file)