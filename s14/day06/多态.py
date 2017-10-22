__author__ = "sun wang"
class Animal(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("%s: 喵喵喵！"%self.name)

class Dog(Animal):
    def talk(self):
        print("%s: 汪汪汪！"%self.name)

def func(obj):
    obj.talk()

c1 = Cat("小晴")
d1 = Dog("李磊")

func(c1)
func(d1)
