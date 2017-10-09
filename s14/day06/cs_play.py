__author__ = "sun wang"


class Role:
    n = 123
    name = "我是类name"
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value
        self.money = money

    def __shot(self):
        print("shooting...")

    def got_shot(self):
        self.__life_value -= 50
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("%s just bought %s" %(self.name ,gun_name))

    def __del__(self):
        print (" %s 彻底死了....." %self.name)

    def show_status(self):
        print ("name: %s weapon:%s life_val:%s" %(self.name ,
                                                  self.weapon,
                                                  self.__life_value))


# print(Role.n)
r1 = Role('Alex', 'police', 'AK47')    #生成一个角色。
r1.buy_gun("B55")
r1.show_status()
r1.got_shot()
r1.show_status()



# r1.name="陈荣华"
# r1.bullet_prov = "True"
# print(r1.n , r1.name , r1.bullet_prov , r1.weapon)
# # del r1.weapon
# # print(r1.n , r1.name , r1.bullet_prov , r1.weapon)
#
# r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色。
# r2.name = "徐良伟"
# r1.buy_gun('AK47')
# print(r1.n , r1.name , r1.bullet_prov , r1.weapon)
# r1.n = "改类变量"
# Role.n = "改变类变量"
# print(r1.n , r1.name , r1.bullet_prov , r1.weapon)
# print (r2.n)
