# -*-coding:utf-8-*-
from functools import reduce
from math import pow

def f(x):
    return x*x

r = map(f,range(1,10))
print(list(r))
    
r = map(str,range(1,10))
print(list(r))

def add(x,y):
    return x+y

r = reduce(add,range(1,10))
print(r)

def concat(x,y):
    return str(x)+str(y)
r = reduce(concat,range(1,10))
print(r)
print(isinstance(r,int))

# convert str to int
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(c):
        return DIGITS[c]
    return reduce(fn,map(char2num,s))
print(str2int('12343'))
print(isinstance(str2int('12343'),int))

# lambda表达式，定义匿名函数，即没有函数名的函数，函数体只有一个返回结果语句
def str2int2(s):
    return reduce(lambda x,y:x*10+y,map(lambda c:DIGITS[c],s))
print(str2int('00123'))
print(isinstance(str2int('00123'),int))
print(int('00123'))

# 把不规范的用户名修改为首字母大写，其他小写
def normalize(name):
    return name[0].upper()+name[1:].lower()
r = map(lambda s:s[0].upper()+s[1:].lower(),['adam', 'LISA', 'barT','a'])
print(list(r))

# 对list求积
def prod(l):
    return reduce(lambda x,y:x*y,l)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
# convert str to float
def str2float(s):
    def fn(x,y):
        return x*10+y
    def char2num(c):
        return DIGITS[c]
    return reduce(fn,map(char2num,[x for x in s if x != '.']))/pow(10, (len(s)-s.find('.')-1))  

print('str2float(\'1234.56\') =', str2float('1234.56'))
if abs(str2float('1234.56') - 1234.56) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')