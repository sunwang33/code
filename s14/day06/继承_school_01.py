# Author:Sun Wang
class School:
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):
        print("为学员%s办理入学手续。" %stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):
        print("雇佣新员工%s"%staff_obj.name)
        self.staffs.append(staff_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        #super(teacher,self).__init__(name,age,sex)
        super(teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        #pass
        print ("""
        ----------Info of teacher : %s ----------
        Name : %s
        Age : %s
        Sex : %s
        Salary : %s
        Course : %s
        """ %(self.name , self.name , self.age , self.sex , self.salary , self.course))

    def teach(self):
        print("%s is teaching [%s]." %(self.name , self.course))

class student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print ("""
        -----------Info of student：%s ----------
        Name : %s
        Age : %s
        Sex : %s
        Stu_id : %s
        Grade : %s
        """ %(self.name , self.name , self.age , self.sex , self.stu_id , self.grade))

    def pay_tution(self,amount):
        print("%s交学费$%s元。" %(self.name,amount))

school = School("老男孩","沙河")
t1 = teacher("Alex",28,'F',20000,"Python")
s1 = student("小米",22,'M',1001,"python")
school.hire(t1)
school.enroll(s1)
t1.teach()
s1.pay_tution(20000)
print(school.students)
print(school.staffs)
school.staffs[0].teach()


