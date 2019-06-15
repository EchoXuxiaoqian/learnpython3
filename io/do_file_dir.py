#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import time

print(os.name)  # 获取操作系统名称
print(os.environ)   # 获取环境变量
print(os.environ.get('JAVA_HOME'))

cur_dir = os.path.abspath('.')
print(cur_dir)
new_dir = os.path.join(cur_dir,'test') # 拼接目录的完整路径
if not os.path.exists(new_dir):
    os.mkdir(new_dir) # 创建目录
# os.rmdir(new_dir) # 删除目录

print(os.path.split(new_dir))
print(os.path.splitext(new_dir)) # 得到文件扩展名

# 列出当前目录下所有文件
ll = list([x for x in os.listdir('.') if not os.path.isdir(x)])
print(ll)
ll = list([x for x in os.listdir('.') if os.path.isfile(x)])
print(ll)

path = os.path.abspath('.')
print('Size  name  last modified time')
print('------------------------------')
for f in os.listdir(path):
    fsize = os.path.getsize(f)
    fname = '%s%s' % (f,'/' if os.path.isdir(f) else '')
    ftime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(f)))
    print('%d  %s  %s' % (fsize,fname,ftime) )
    

def find_files(path,name,results):
    print(path)
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isfile(i) and name in i:
                results.append(i)
            else:
                find_files(os.path.join(path,i),name,results)
    elif os.path.isfile(path):
        if name in path:
            results.append(path)

result = []
find_files(os.path.abspath('G:\\WingIDE5\\Python_Workspace\\learn-python3'),'py',result)
print(result)