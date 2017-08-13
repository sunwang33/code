__author__ = "sun wang"

import time

user = "Alex"
password = "abc"
def auth(auth_type):
    print ("auth_type:",auth_type)
    def out_warpper(func):
        print ("func:",func)
        def wrapper(*args, **kwargs):
            print ("warpper func args: ",*args, **kwargs)
            if auth_type == "local":
                user_name = input("USERNAME: ").strip()
                pass_word = input("PASSWORD：").strip()
                if user_name == user and pass_word == password:
                    print("Login success !")
                    res = func(*args, **kwargs)
                    return res
                else:
                    print("Login fail !")
            elif auth_type == "ldap":
                print ("搞毛线。")

        return wrapper
    return out_warpper


def index():
    print ("welcome to the index.")
@auth(auth_type="local")
def home():
    print("welcome to the home.")
    return "from home"
@auth(auth_type="ldap")
def bbs():
    print("welcome to the bbs.")

index()
home()
bbs()

