__author__ = "sun wang"
class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students=[]
        self.staffs=[]

    def enroll(self,stu_obj):
        print ("为学员%s办理注册手续" % stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        self.staffs.append(staff_obj)
        print("雇佣新员工%s" % staff_obj.name)


class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass


class teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print("""
        ----------- info of Teacher %s -----------
        Name : %s
        Age : %s
        Sex : %s
        Salary : %s
        Course : %s
        """ %(self.name , self.name , self.age , self.sex , self.salary,self.course ))

    def teach(self):
        print("%s is teaching course [%s]." %(self.name , self.course))


class student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def pay_tution(self,amount):
        print ("%s has paid tution $%s" %(self.name , self.amount))


school = School("老男孩" ,"沙河" )

s1 = student("Jim", 20, 'M',1001,"linux")
s2 = student("Tom",21,'F',1002,"python")

t1 = teacher("oldboy",56,'M',2000000,"linux")
t2 = teacher("Alex",28,'F',10000,"python")


t1.tell()
t2.tell()
s1.tell()
s2.tell()

school.hire(t1)
school.hire(t2)

school.enroll(s1)
school.enroll(s2)
# #

#
print(school.students)
print(school.staffs)
school.staffs[0].teach()






