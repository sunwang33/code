__author__ = "sun wang"


def wrapper(*args, **kwargs):
    user_name = input("USERNAME: ").strip()
    pass_word = input("PASSWORD：").strip()
    if user_name == user and pass_word == password:
        print("Login success !")
        res = func(*args, **kwargs)
        return res
    else:
        print("Login fail !")


return wrapper
