__author__ = "sun wang"

# import random
#
# checkcode=''
# for i in range(4):
#     current=random.randint(0,10)
#     checkcode+=str(current)
# print(checkcode)
# import random
# checkcode=''
# for i in range(4):
#     current=random.sample("abcdefghijklmn123456789",1)
#     checkcode+=str(current[0])
# print(checkcode)
import random
checkcode=''
for i in range(4):
    current=random.randrange(0,4)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    checkcode += str(tmp)
print(checkcode)


