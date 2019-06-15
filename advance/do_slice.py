# -*- coding:utf-8 -*-
L = ['Tom','Jerry','Music','Sing']
print(L[0:2]) #从索引0开始，不包括索引2
print(L[:2])    #第一个索引为0时可以省略 
print(L[-2:]) #支持倒数切片

L = list(range(1,101))
print(L[:10]) # 取出list中的前10个数
print(L[-10:]) # 取出list中的后10个数
print(L[10:20]) # 取出前11到20个数
print(L[:10:3]) # 前10个数，每3个取一个
print(L[::10]) # 所有数，每10个获取一次


S = '3423I4U23I4' # 字符串也可以进行切片
print(S[4:7])

def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
            

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
else:
    print('测试成功!')