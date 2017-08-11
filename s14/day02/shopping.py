__author__ = "sun wang"

salary = input("Please input your salary:")
product_list = [
    ('Iphone', 5000),
    ('Mac Pro', 9800),
    ('Bike', 800),
    ('Watch', 10600),
    ('Coffee', 31),
    ('Alex Python', 120)
]
shopping_list = []
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(product_list):
            print (index, item)
        user_choice = input("选择要买什么？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    salary-=p_item[1]
                    print("Add %s into shopping cart, your current balance is \033[31;1m%s\033[0m" % (p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]了\033[0m" % salary)
            else:
                print("product code [%s] is not exist! " % user_choice)
        elif user_choice == 'q':
            print ("-------------shopping list-----------")
            for p in shopping_list:
                print(p)
            print("Your current balance:",salary)
            exit()
        else:
            print ("invalid option")
            exit()