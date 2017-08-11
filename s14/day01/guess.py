#Author： sun wang
"""
age_of_boy = 56
count = 0
while count < 3:
    guess_age = int(input('guess_age:'))
    if guess_age == age_of_boy :
        print ( " yes, you got it. " )
        break
    elif guess_age > age_of_boy :
        print ( " think smaller ..." )
    else:
        print ( " think bigger! " )
    count+= 1
else:
    print ("You have tried too many times.")
"""
"""
age_of_boy = 56
count = 0
for i in range(3):
    guess_age = int(input('guess_age:'))
    if guess_age == age_of_boy :
        print ( " yes, you got it. " )
        break
    elif guess_age > age_of_boy :
        print ( " think smaller ..." )
    else:
        print ( " think bigger! " )
else:
    print ("You have tried too many times.")
"""

for i in range(0,10,2):
    print ( "loop:",i )



