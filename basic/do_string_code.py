# coding:utf-8

print("中文")

print(ord('B'))
print(ord('一'))
print(chr(66))
print(chr(19968))

print('123'.encode('ascii'))
print('一二三'.encode('utf-8'))
print(b'123'.decode('ascii'))
print(b'\xe4\xb8\x80\xe4\xba\x8c\xe4\xb8\x89'.decode('utf-8'))

print(len("abc123"))
print(len("一二三".encode('utf-8')))

print('亲爱的%s,你的账号为%06d,你已累计在线学习%.2f小时,超过了%.2f%%的人' % ('xxq',1,3.456,84.2))

s1 = 72
s2 = 85
r = 100*(s2-s1)/s1
print('小明成绩提升了%.1f%%' % r)