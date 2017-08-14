# Author:Sun Wang
import getpass
count = 0
exit_flag = True
lock_list =  open("lock_list",'r+',encoding="utf-8")
user_list =  open("user_list",'r+',encoding="utf-8")
while count < 3 and exit_flag == True:
    if count == 3:
        lock_list.write(_username,"\n")
    _username = input("Please input your name: ")
    _password = getpass.getpass("Please input your password: ")
    for lock_user in lock_list.readlines():
        lock_user = lock_user.strip().split(" ")
        print (i)
        """
        if _username != i:
            continue
        else:
            print ("the username is locked!!!!!")
            exit_flag = False
            break
    for j in user_list.readlines():
        j = j.strip().split(" ")
        if   j[0] ==_username and  j[1] == _password:
            print ("Welcome!!!")
            exit_flag = False
            break
        else:
            print ("Invalid username or password!!!")
            count+=1
            """



