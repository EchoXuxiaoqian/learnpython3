# -*- coding:utf-8 -*-

f = map(lambda x:x*x,range(1,11))
print(list(f))

f = lambda x:x*x
print(f)
print(f(1))

def is_odd(n):
    return n%2 == 1
L = list(filter(is_odd,range(1,11)))
print(L)
print(list(filter(lambda x:x%2 == 1,range(1,11))))