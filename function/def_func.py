# -*- coding:utf-8 -*-

import math     #导入math包，导入之后后续才可引用其中的方法

def my_abs(x):
    if not isinstance(x,(int,float)): # 参数数据类型检查可用内置函数isinstance实现
        raise TypeError('bad operand type')
    if x<0:
        return -x;
    else:
        return x;

def bak_func():
    pass

print(my_abs(-9))
#rint(my_abs('as'))
#print(abs('as'))

def move(x,y,step,angle=0): #参数赋值表示该参数可缺省
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny        # 函数返回多个值，实际上是放在tuple中返回

x,y = move(0,0,10)
print(x,y)

def quadratic(a,b,c):
    if not isinstance (a+b+c,(int,float)):
        raise TypeError('bad operand type')
    m = b**2-4*a*c
    if m < 0 :
        return '无解'
    elif m == 0 :
        return -b/(2*a)
    else:
        x1 = (-b + math.sqrt(m))/(2*a)
        x2 = (-b - math.sqrt(m))/(2*a)
        return round(x1,2),round(x2,2) # round函数可设置保留小数位数，涉及四舍五入不建议使用该函数
    
a =1
b = 7
c = -4
print('%sx**2+%sx+%s 求解：' % (a,b,c),quadratic(a,b,c))
