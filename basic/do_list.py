classmates = ['apple','tom']
print(classmates)
print(len(classmates))

print(classmates[0])
print(classmates[1])

print(classmates[-1])

classmates.append('jerry')
print(classmates)

classmates.insert(0,'kate')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(0)
print(classmates)

company = ['Apple','Google','Macrosoft']
language = ['Java','Python','Ruby']
name = ['Lisa','Tom','Adam']
L = [company,language,name]
print(L)
print(L[0][0])
print(L[1][1])
print(L[2][0])