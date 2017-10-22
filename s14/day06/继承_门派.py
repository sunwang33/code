__author__ = "sun wang"

class Organization(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.goldens = []
        self.staffs = []

    def hire(self,gold_obj):
        print("雇佣了修仙者%s" %gold_obj.name)
        self.goldens.append(gold_obj)

    def eroll(self,staff_obj):
        print("")
        self.staffs.append(staff_obj)

class Person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

class golden(Person):
    def __init__(self,name,age,sex,superpower,level,course):
        super(golden,self).__init__(name,age,sex)
        self.superpower = superpower
        self.level = level
        self.course = course

    def tell(self):
        print("""
        ####Info of golden: %s####
        Name : %s
        Age : %s
        Sex : %s
        Superpower : %s
        Level : %s
        Course : %s""" %(self.name,self.name,self.age,self.sex,self.superpower,self.level,self.course))

    def teach(self):
        print("修仙者%s教授[%s]法术课程。"%(self.name,self.course))

class factotom(Person):
    def __init__(self,name,age,sex,superpower,level,grade):
        super(factotom,self).__init__(name,age,sex)
        self.superpower = superpower
        self.level = level
        self.grade = grade

    def tell(self):
        print("""
        ####Info of factotom: %s
        Name : %s
        Age : %s
        Sex : %s
        SuperPower : %s
        Level : %s
        Grade : %s
        """)

    def task(self,amount):
        print("杂役弟子%s向门派贡献灵石%s块。" %(self.name,amount))

organ_1 = Organization("九盈门","盘山")
f1 = factotom("汤木",22,"M","金刚诀","炼气期","观海诀")
f2 = factotom("韩丽",20,"M","长春功","炼气期","望月诀")
f3 = factotom("路坦",21,"M","眨眼剑法","炼气期","望月诀")

g1 = golden("解瑞",25,"M","不动明王经","筑基期","观海诀")
g2 = golden("洛水",28,"M","洞玄心经","筑基期","望月诀")

organ_1.hire(g1)
organ_1.hire(g2)

organ_1.eroll(f1)
organ_1.eroll(f2)
organ_1.eroll(f3)

print(organ_1.goldens)
print(organ_1.staffs)

organ_1.goldens[0].teach()
organ_1.goldens[1].teach()

f1.task(1000)
f2.task(600)
f3.task(300)













