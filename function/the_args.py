# -*- coding:utf-8 -*-
# var args
def hello(greeting,*args):
    if (len(args) == 0):
        print('%s!' % greeting)
    else:
        print('%s,%s!' % (greeting,','.join(args))) # 使用，拼接tuple中的元素

print(hello('Hi'))    # => greeting='Hi', args=()
print(hello('Hi','Echo')) # =>greeting='Hi', args=('Echo')
name = ('Lisa','Echo')
print(hello('Nice to meet you',*name))


# kw args
def print_scores(**kw):
    print('name    score')
    print('--------------')
    for name,score in kw.items():    #遍历dict中的每个元素，key放入第一个参数中，value放入第二个参数中
        print('%10s   %d' % (name,score))
    print() # 打印空行

print_scores(Adam=99,Lisa=80,Tom=89)
data = {
    'L':23,
    'M':89
}
print_scores(**data)

def print_info(name,*,gender,city='HangZhou',age):
    print('personal information')
    print('--------------------')
    print('Name:%s' % name)
    print('gender:%s' % gender)
    print('city:%s' % city)
    print('age:%s' % age)
    print()

print_info('Tom',gender='F',age='18')
print_info('Tom',gender='F',age='18',city='Suzhou')

def product(x,*args):
    result = x
    if args is None:
        #return result
        pass
    else:
        for t in args:
            result = result * t 
    return result

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')