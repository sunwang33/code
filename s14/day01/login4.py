# Author:Sun Wang
def real_login():
    count = 0
    while count < 3:
        user_password = input("请输入你的密码: ")
        with open("user_list",'r') as login_file:
            for user_info in login_file.readlines():
                user_info = user_info.strip().split()
                if user_name == user_info[0]:
                    if user_password == user_info[1]:
                        print ("Login Success!!!")
                        exit()
                    else:
                        count +=1
                        if count < 3:
                            print ("您输入的用户名或密码存在问题，请重新输入。")
                        else:
                            print("您输入的用户已经被锁定。")
                        continue
                else:
                    continue
    if count == 3:
        with open("lock_list",'a+') as lock_file2:
            lock_file2.writelines("\n")
            lock_file2.writelines(user_name)
def user_register():
    user_choise = input(" 是否想要注册用户名？（yes/no)")
    if user_choise == "yes":
        count = 0
        while count < 10 :
            user_name2 = input("请输入你要创建的用户名： ")
            user_list2 = []
            with open("user_list",'r') as user_list_file:
                for user_name_3 in user_list_file:
                    user_name_3 = user_name_3.strip().split()[0]
                    user_list2.append(user_name_3)
                if user_name2 in user_list2:
                    print ("您输入的用户名已经存在。")
                    count +=1
                else:
                    with open("user_list",'a+') as user_list_file:
                        user_list_file.write("\n")
                        user_list_file.write(user_name2)
                        user_list_file.write(" ")
                    count2 = 0
                    while count < 3:
                        user_password2 = input("请输入密码：")
                        user_password3 = input("请再次输入密码：")
                        if user_password2 == user_password3:
                            with open("user_list", 'a+') as user_list_file:
                                user_list_file.write(user_password2)
                                user_list_file.write("\n")
                            print ("新建用户成功，请登录")
                            return real_login()
                        else:
                            count +=1
                        if count == 3:
                            msg3 = input("您已经错了三次，是否继续？(yes/no)")
                            if msg3 != "no":
                                count = 0

    else:
        print ("好的，再见。")

def lock_list():
    with open("lock_list",'r') as lock_file:
        #print (lock_file.readlines())
        for user_name2 in lock_file.readlines():
            #user_name2 = username2.split("\n")
            #print(user_name2)\
            user_name2 = user_name2.strip()
            if user_name2 == user_name:
                print ("your username is locked.")
            else:
                continue
def check_user_register():
    with open("user_list",'r') as check_file:
        for user_name3 in check_file:
            user_name3 = user_name3.strip().split()[0]
            if user_name == user_name3:
                 return real_login()
            else:
                continue
        else:
            return user_register()



print ("Welcome!!!")
user_name = input("Please input your username: ")

lock_list()
check_user_register()

