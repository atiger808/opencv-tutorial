# _*_ coding: utf-8 _*_
# @Time     : 2019/9/22 2:29
# @Author   : Ole211
# @Site     : 
# @File     : check_memory.py    
# @Software : PyCharm
import os
import time
def check_memory(path, style='M'):
    '''
    检测文件夹内存大小函数
    :param path:
    :param style:
    :return:
    '''
    total = 0
    for root, dirs, file in os.walk(path):
        for i in file:
            filepath = os.path.join(root, i)
            if (os.path.getsize(filepath)/1024)<200:
                os.remove(filepath)
                print('del----{}'.format(filepath))
            total += os.path.getsize(os.path.join(root, i))
        if style == 'M':
            memory = total / 1024. / 1024.
        else:
            memory = total / 1024. / 1024. / 1024.
            print('%.4f GB' % (memory))
    return memory

def main(path, limt=0.5):
    memory = check_memory(path)
    print('%.4f MB' % (memory))
    if memory>limt:
        files = sorted([i for i in os.listdir(path)],key=lambda x:int(x.split('_')[0]))
        os.remove(os.path.join(path, files[0]))
        print(files[0], 'delete Succuess!')


if __name__ == '__main__':
    print('正在监视文件夹。。。。')
    while True:
        main('./record/')