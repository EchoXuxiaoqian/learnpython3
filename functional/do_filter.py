# -*-coding:utf-8-*-

def is_odd(x):
    return x%2 == 1

r = filter(is_odd,range(1,10))
print(list(r))

def not_empty(s):
    return s and s.strip()
r = list(filter(not_empty,['A', '', 'B', None, 'C', '  ']))
print(r)


def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n
        
def _not_divisible(n):
    return lambda x:x%n >0
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n 
        it = filter(_not_divisible(n),it)
# 获取素数        
for n in primes():
    if n < 20:
        print(n)
    else:
        break;
    
# 筛选回数：指从左向右读和从右向左读都是一样的数
def is_palindrome(n):
    str1 = str(n)
    str2 = str1[::-1]
    return str1 == str2
         
    
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')