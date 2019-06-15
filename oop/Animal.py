#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')
        
class Dog(Animal):
    def run(self):      # 覆盖父类的方法
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
def run_twice(animal):
    animal.run()
    animal.run()

if __name__ == '__main__':
    animal = Animal()
    dog = Dog()
    cat = Cat()
    animal.run()
    dog.run()
    cat.run()
    print('animal is Animal?',isinstance(animal,Animal))
    print('dog is Animal?',isinstance(dog,Animal))
    print('cat is Animal?',isinstance(cat,Animal))
    run_twice(animal)
    run_twice(dog)
    run_twice(cat)