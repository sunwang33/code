#Author： sun wang

name = input("name: ")
age = input( "age：")
job = input(" job: ")
salary = int(input("salary: "))

info3 = '''
-------- info of { 0 } --------
Name: { 0 }
Age: { 1 }
Job: { 2 }
Salary: { 3 }
''' .format( name , age , job , salary  )
print(info3)

