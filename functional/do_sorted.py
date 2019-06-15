# -*-coding:utf-8-*-

l = [-1,2,-34,435,23]
r = sorted(l)
print(r)
r = sorted(l,key=abs)
print(r)

l2 = ['ad','Ss','Zas']
r2 = sorted(l2) # 默认字母按ASCII排序
print(r2)
r2 = sorted(l2,key=str.lower) # 实现忽略大小写的排序
print(r2) 
r2 = sorted(l2,key=str.lower,reverse=True) # 进行反向排序
print(r2) 

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 对上述列表按名字排序
def by_name(t):
    return t[0].lower()
L1 = sorted(L, key=by_name)
print(L1)
# 按成绩从高到低排序
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score,reverse=True)
print(L2)
