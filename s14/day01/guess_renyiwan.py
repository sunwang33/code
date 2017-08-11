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
for i in range(10):
    guess_age = int(input('guess_age:'))
    if (i+1)% 3 == 0 :
        ask_continue = input("Are you continue? (yes or no)")
        if ask_continue == "yes":
            pass
        else:
            break
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






