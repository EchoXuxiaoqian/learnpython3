# -*- coding:utf-8 -*-
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum # 返回的是函数名

f = lazy_sum(1,2,3,4)
print(f)

print(f()) # 调用函数的时候才真正进行计算

f1 = lazy_sum(1,2,3,4)
f2 = lazy_sum(1,2,3,4)
print(f1 == f2)

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f) # f函数中引用了变量i，i后面都是3，所以返回时9，9，9而不是1，4，9
    return fs

f1,f2,f3 = count()
print(f1(),f2(),f3())

# fixd variable in return function
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1,f2,f3 = count()
print(f1(),f2(),f3())

def createCounter():
    n = 0
    def counter():
        # global n # 引用全局变量
        nonlocal n # 引用外层(非全局)变量
        n = (n+1)
        return n
    return counter

    
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')