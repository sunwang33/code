# Author:Sun Wang
import json
# info = {
#     'name':'alex',
#     'age': 22
# }
# def sayhi(name):
#     print("hello2,",name)
info = {
    'name':'alex',
    'age': 22 ,
    #'func':sayhi
}
f=open("test.text","r")
#data=pickle.loads(f.read())
data=json.load(f)
print(data["func"]('alex'))