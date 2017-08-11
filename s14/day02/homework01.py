__author__ = "sun wang"
import copy
your_salary = int(input("your salary:"))
# the sum of the product
sum_product = 0
# the price of the product
product_price = 0
#the blance of the custom
blance = your_salary  - product_price
list = """
1. Iphone 5800
2. Mac Pro 12000
3. StarBuck Latte 31
4. Alex Python 81
5  Bike 800
"""
list1 = [
["1","Iphone","5800"],
["2","Mac Pro", "12000"],
["3","StarBuck Latte", "31"],
["4","Alex Python","81"],
["5","Bike","800"]
]
list2 = [ 0, 1, 2, 3, 4, 5,6]
shop_list = []
for product_seq in list2:
    print(list)
    product_seq = input("Please select the seq of the product: ")
    product_seq2 = str(product_seq)
    if product_seq2 == "q":
        print("have bought below:", shop_list,
              "your blance ：", blance)
        break
    product_seq1 = int(product_seq)
    product_price = int(list1[product_seq1 - 1][2])
    if blance > product_price:
        sum_product += product_price
        blance = your_salary - sum_product
        shop_list.append(list1[product_seq1 - 1][1])
    else:
        print ("your blance is not enough.")
        print("have bought below:", shop_list,
              "your blance ：", blance)






