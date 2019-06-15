# -*- coding:utf-8 -*-

L = [x*x for x in range(10)]
print(L)

G = (x*x for x in range(3))
print(G)
print(next(G))
print(next(G))
print(next(G))
#print(next(G)) # 没有更多元素时，抛出StopIteration错误
G = (x*x for x in range(2))
for x in G:
    print(x )
    
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        a,b = b,a+b
        n = n+1
        yield a
    return "done"

for x in fib(6):
    print(x)
    
# 怎么拿generator的返回值
g = fib(6)
while True:
    try:
        next(g)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break
    
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    
a = odd()
print(next(a))
print(next(a))

#杨辉三角
def triangles():
    b = [1]
    for x in range(100):
        yield b
        b.append(0)
        b = [b[i]+b[i-1] for i in range(len(b))]
for t in triangles():
    print(t)
    
def triangles2():
    L = [1]
    while True:
        yield L
        L = [1] + [L[x]+L[x+1] for x in range(len(L)-1)] + [1]
        if len(L) > 10:
            return;
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t[:]) # 复制list
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')