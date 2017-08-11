__author__ = "sun wang"

# school = "Oldboy edu."

# def change_name(name):
#     global school
#     school = "Mage Linux"
#     print("before change", name , school)
#     name = "Alex li"
#     age = 23
#     print ("After change", name)


# name = "alex"
# change_name(name)
# print(name)
# print ("school: ",school)
#print (age)

# def change_name():
#     global name
#     name = "alex"
#
# change_name()
# print (name)
school = 'Oldboy edu.'
names = ['Alex','Jack','Rain']
def change_name():
    names[0] = '金角大王'
    print ('inside func',names)

change_name()
print(names)