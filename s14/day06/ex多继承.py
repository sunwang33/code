__author__ = "sun wang"
class animal(object):
    def __init__(self,name,age,power):
        self.name = name
        self.age = age
        self.power = power
        self.skills = []
        print("doesn't run it")

    def eat(self):
        print ("%s is eating ..." %self.name)

class wing(object):
    def __init__(self,name,age,power):
        print("run it")
    def fly(self,obj):
        print("冲向天空吧，%s" %self.name)
        self.skills.append(obj)

class tiger(animal , wing):
    def __init__(self,name,age,power):
        super(tiger, self).__init__(name,age,power)
        self.power = power
        print("%s 一出生就有%s 力量。" %(self.name , self.power))

m1  = animal("小明",5 ,40)
m1.eat()
Tiger_1 = tiger("大虎", 5, 85)
Tiger_1.eat()
Tiger_1.fly("fly")
Tiger_1.skills="dance"
print(Tiger_1.skills)


