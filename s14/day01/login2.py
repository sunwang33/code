# Author:Sun Wang
import getpass
print ("Welcome !!!")
user_name = input("Please input your name: ")
lock_list = open("lock_list",'r+',encoding="utf-8")
count = 0
#检查用户是否在黑名单。
for lock_user in lock_list.readlines():
    lock_user = lock_user.strip().split()
    #print (lock_user[0])
    if lock_user == user_name:
        print ("your user is locked!!!")
        lock_list.close()
        exit()
#检查用户是否是注册用户。
user_list = open("user_list",'r+',encoding="utf-8")
for  _username in user_list:
    _username = _username.strip().split()
    #print (_username)
    if _username[0] == user_name:
        user_list.close()
        break
else:
    user_choise = input("你输入的用户名不存在，是否想注册新用户？(yes/no)")
    if user_choise == 'yes':
        msg1="注册开始"
        print (msg1.center(50,"-"))
        while True:
            create_name = input("请输入你要创建的用户名： ")
            user_list = open("user_list", 'r+', encoding="utf-8")
            for  user_name2  in user_list:
                user_name2 = user_name2.strip().split()
                #print(user_name2[0])
                if create_name == user_name2[0]:
                    print ("您创建的用户名已经存在。")
                else:
                    print("您的用户名没有人使用。")
                    #user_list.write('\n')
                    user_list.write(create_name)
                    user_password_1 = getpass.getpass("请输入你的密码： ")
                    user_password_2 = getpass.getpass("请再次输入你的密码： ")
                    while True:
                        if user_password_1 == user_password_2 :
                            user_list.write(' ')
                            user_list.write(user_password_1)
                            user_list.write('\n')
                            exit()
                        else:
                            user_password_1 = getpass.getpass("请输入你的密码： ")
                            user_password_2 = getpass.getpass("请再次输入你的密码： ")
                            continue






    else:
        user_list.close()
        exit()
#输入用户密码，如果密码错三次，账户被锁。
while count < 3:
    user_list = open("user_list",'r+',encoding="utf-8")
    user_list = user_list.readlines()
    for username in user_list:
        #print (username)

        username = username.strip().split()
        #print (username[0])

        if username[0] == user_name:

            while count < 3:
                user_password = input("Please input your password: ")
                for userpassord in user_list:
                    userpassword = userpassord.strip().split()
                    if userpassword[1] == user_password:
                        print ("login success!!!")
                        #user_list.close()
                        exit()
                    else:
                        print ("Your password is wrong!!!")
                        count += 1
                        break
                if count == 3:
                    lock_list.write('\n'+user_name)
                    print ("Your account is locked now!!!")
                    user_list.close()
    else:
        print ("账号不存在 ！！！")
        user_list.close()
        exit()


