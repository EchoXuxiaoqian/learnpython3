# -*- coding:utf-8 -*-
from collections import Iterator

print(isinstance('abc',Iterator)) # 判断对象是否是迭代器对象
print(isinstance(12,Iterator))
print(isinstance(['abc'],Iterator))
print(isinstance(('abc'),Iterator))
print(isinstance({'abc'},Iterator))
print(isinstance({'abc':12},Iterator))
print(isinstance([x*x for x in range(10)], Iterator))
print(isinstance((x*x for x in range(10)),Iterator)) #生成器是迭代器对象
print(isinstance(iter([x*x for x in range(10)]), Iterator)) # iter() convert iterable to iterator