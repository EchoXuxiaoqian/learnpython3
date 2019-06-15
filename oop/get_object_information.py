#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from Animal import Animal ,Dog,Cat

print('type(123) = ',type(123))
print('type("abc") = ',type("abc"))
print('type([1,2,3]) = ',type([1,2,3]))
print('type((1,2,3)) = ',type((1,2,3)))
print('type({1:1,2:2}) = ',type({1:1,2:2}))
print('type({1,2,3}) = ',type({1,2,3}))
print('type(Animal()) = ',type(Animal()))
print('type(Dog()) = ',type(Dog()))

animal = Animal()
dog = Dog()
cat = Cat()
print('animal is Animal?',isinstance(animal,Animal))
print('dog is Animal?',isinstance(dog,Animal))
print('cat is Animal?',isinstance(cat,Animal))
print('cat is Cat?',isinstance(cat,Cat))
print('cat is Dog?',isinstance(cat,Dog))

print(dir(animal))

print(hasattr(animal,'run'))
print(hasattr(animal,'test'))
print(hasattr(animal,'test'))
print(getattr(animal,'run'))
print(getattr(animal,'test','none'))