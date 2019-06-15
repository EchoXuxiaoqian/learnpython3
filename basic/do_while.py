# coding:utf-8

#计算100以内所有的奇数和
sum = 0
n = 1
while n < 10:
    sum = sum+n
    n = n+2
print(sum)

sum = 0
n = 0
while n <100:
    n = n + 1
    if (n > 10):
        break;
    if (n%2 == 0):
        continue
    print(n)
    sum = sum + n
print(sum)
