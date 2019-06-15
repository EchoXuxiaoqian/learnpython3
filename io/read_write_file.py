#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time

try:
    with open('test.txt', mode='r') as f:
        # content = f.read() #读取全部内容，文件过大会占用太多内存
        for line in f.readlines():   # 一行一行读取
            print(line.strip()) # 删除末尾的换行符
    # f.close()    # with语句自动调用close，不需要使用try...finally这么繁琐
    with open('test.txt',mode='w') as f:
        print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        f.write('Hello,the time is:%s' % 
                time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
except Exception as e:
    print(e)
