# Author:Sun Wang
#排错
print("Welcome !!!")
user_name = input("Please input your name: ")
lock_list = open("lock_list", 'r+')
def	real_login():
	count = 0
	while count < 3:
		#user_list.close()
		user_list1 = open("user_list",'r+')
		#user_list = user_list.readlines()
		if user_name in user_list1.readlines():
			while count < 3:
				user_password = input("Please input your password: ")
				for userpassord in user_list1:
					userpassword = userpassord.strip().split()
					if userpassword[1] == user_password:
						print ("login success!!!")
						exit()
					else:
						print ("Your password is wrong!!!")
						count += 1
						break
				if count == 3:
					lock_list.write('\n'+user_name)
					print ("Your account is locked now!!!")
					#user_list.close()
#检查用户是否在黑名单。
def  check_black_list():
	for lock_user in lock_list.readlines():
		lock_user = lock_user.strip().split()
		#print (lock_user[0])
		if lock_user[0] == user_name:
			print ("your user was locked!!!")
			lock_list.close()
			exit()
#检查用户是否是注册用户。
def	check_regedit_user():
	user_list = open("user_list",'r+')
	for  user_name1 in user_list.readlines():
		user_name1 = user_name1.split()[0]
		#print (user_name1)
		if user_name1 == user_name:
			#print ("1")
			return real_login()
		else:
			user_choise = input("你输入的用户名不存在，是否想注册新用户？(yes/no)")
			if user_choise == 'yes':
				msg1="注册开始"
				print (msg1.center(50,"-"))
				while True:
					create_name = input("请输入你要创建的用户名： ")
					user_list2 = open("user_list", 'a+')
					if create_name in user_list2.readlines():
						print ("您创建的用户名已经存在。")
						break
					else:
						print("您输入的用户名当前没有人使用。")
						#user_list.write('\n')
						#print ("写入用户名前")
						user_list2.write(create_name)
						#print("写入用户名后")
						while True:
							user_password_1 = input("请输入你的密码： ")
							user_password_2 = input("请再次输入你的密码： ")
							if user_password_1 == user_password_2 :
								#print("写入密码前")
								user_list2.write(' ')
								user_list2.write(user_password_1)
								user_list2.write('\n')
								return real_login()
								#exit()
							else:
								print ("两次输入密码不一致。")
			else:
				user_list.close()
				print ("回见")
				exit()
	#输入用户密码，如果密码错三次，账户被锁。



check_black_list()
check_regedit_user()
real_login()
