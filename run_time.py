# _*_ coding: utf-8 _*_
# @Time     : 2019/9/18 0:45
# @Author   : Ole211
# @Site     : 
# @File     : run_time.py    
# @Software : PyCharm
import time

def run_time(func):
    def new_func(*args, **kwargs):
        t0 = time.time()
        print('start time: %s' % (time.strftime('%x', time.localtime())))
        back = func(*args, **kwargs)
        print('end time: %s' %(time.strftime('%x', time.localtime())))
        print('waste time: %s' %(time.time() - t0))
        return back
    return new_func

if __name__ == '__main__':
    pass