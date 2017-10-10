# Author:Sun Wang
class People:

    def __init__(self, name, age):
        self.name = name
        self.age = name

    def eat(self):
        print("%s is eating ..." %self.name)

    def talk(self):
        print("%s is talking ..." %self.name)

    def sleep(self):
        print("%s is sleeping ..." %self.name)

class Man(People):
    #pass
    def __init__(self,name,age,money):
        #People.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.money = money
        print("%s 一出生就有%s money" %(self.name ,self.money))
    def piao(self):
        print("%s is piaoing ... 20s ...done." %self.name)

    def sleep(self):
        print ("Man is sleeping.")

class Woman(People):
    def get_birth(self):
        print("%s is born a baby ..." %self.name)

m1 = Man("NiuHanYang" , 22,10)
m1.eat()
m1.piao()
m1.sleep()

w1 = Woman("ChenRonghua",26)
w1.get_birth()