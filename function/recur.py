# -*- coding:utf-8 -*-

# 利用递归计算阶乘 n! = 1 x 2 x 3 x ... x n

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)*n
    
    
print(fact(5))


# 汉诺塔，将圆盘从一根柱子移动到另一个柱子上，且大的圆盘不可以放在小的圆盘上面。
# 无论多少个圆块，可以抽象成为同一套思路：就是想办法把(n-1)个a柱上的圆块先移动到b柱，然后把最底部最大的一个圆块移动到c柱，最后把b柱上的(n-1)个圆块移动到c柱
def move(n,a,b,c):
    if n == 1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
        
move(3,'A','B','C')