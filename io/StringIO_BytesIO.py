#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO,BytesIO

f = StringIO()
f.write('hello')
print(f.getvalue())
print(f.tell())
f.seek(0) # 将流的位置移动到初始则可用read方法获取内容
print(f.tell())
for x in f.readlines():
    print(x.strip())

f = StringIO('HELLO WORLD\nTEST')
print(f.tell())
print(f.getvalue()) # 不影响流的位置
print(f.tell())
for x in f.readlines():
    print(x.strip())
print(f.tell())

b = BytesIO()
b.write('中文1323dswe'.encode('utf-8'))
print(b.getvalue())

b = BytesIO(b'\xe4\xb8\xad\xe6\x96\x871323dswe')
print(b.read())