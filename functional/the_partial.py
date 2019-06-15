# -*- coding:utf-8 -*-
import functools

print(int('12345'))
print(int('110',base=2)) # 转换2进制字符串为十进制数字

def int2(x):
    return int(x,base=2)
print(int2('110'))

int2 = functools.partial(int,base=2) #利用functools.partial创建偏函数
print(int2('111'))

max2 = functools.partial(max,10) #此处固定的不是关键字参数，所以10是可变参数的一部分
print(max2(1,6,7))
print(max2(1))

for i in range(10):
    print(i)