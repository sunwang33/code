# Author:Sun Wang
# !/usr/bin/env python
# Author:Sun Wang
product_list = [("Iphone", 6000),
                ("Mac Pro", 10200),
                ("Bike", 1200),
                ("sword", 8000),
                ("coffee", 30)]

salary = input("Please input your salary: ")
shopping_list = []

if salary.isdigit():
    salary = int(salary)
else:
    print("invalid option.")

while True:
    #print ("profuct list".center(50 , "-")

    for index, item in enumerate(product_list):
        print(index, item)

    user_choice = input("Add product to cart: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice < len(product_list) and user_choice >= 0:
            p_item = product_list[user_choice]
            if salary >= p_item[1]:
                shopping_list.append(p_item)
                salary -= p_item[1]
                print("Add  product \033[31;1m%s\033[0m  to your cart,your balance is  \033[31;1m%s\033[0m" % (
                p_item, salary))
            elif salary < p_item[1]:
                print("your balance is \033[31;1m%s\033[0m ,it's not enough." % salary)
    elif user_choice == "q":
        print("shopping list")
        for q in shopping_list:
            print(q)
        print("your current is \033[31;1m%s\033[0m ." % salary)
        exit()
    else:
        print("Product code \033[31;1m%s\033[0m is not exist !!! ")




