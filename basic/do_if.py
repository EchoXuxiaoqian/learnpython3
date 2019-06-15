# coding:utf-8

age = 20
if age >18:
    print("your age is",age)
    print("adult")
    
age = 20
if age >= 6:
    print("teenager")
elif age >= 18:
    print('adult')
else:
    print('kid')

birth = input('birth:')
birth = int(birth) # input读取用户输入，数据类型为str，int()函数将str转换为int 
if birth < 2000:
    print('00前')
else:
    print('00后')
    

h = input('please input your height(m):')
w = input('please input your weight(kg):')
bmi = float(w)/(float(h)**2)
print('your bmi is %.2f' % bmi)
if bmi < 18.5:
    print('过轻')
elif bmi>= 18.5 and bmi < 25:
    print('正常')
elif bmi>= 25 and bmi < 28:
    print('过重')
elif bmi>= 28 and bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')