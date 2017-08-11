#Author： sun wang

name = input("name: ")
age = input( "age：")
job = input(" job: ")
salary = input("salary: ")

info2 = '''
-------- info of { _name } --------
Name: {_name }
Age: {_age }
Job: {_job }
Salary: { _salary }
''' .format( _name=name,
             _age=age,
             _job=job,
             _salary=salary)
print(info2)

info2 = '''
-------- info of { 0 } --------
Name: { 0 }
Age: { 1 }
Job: { 2 }
Salary: { 3 }
''' .format( _name=name,
             _age=age,
             _job=job,
             _salary=salary)
print(info3)


