# Author:Sun Wang
import pickle
# info = {
#     'name':'alex',
#     'age': 22
# }
def sayhi(name):
    print("hello2,",name)
info = {
    'name':'alex',
    'age': 22 ,
    'func':sayhi
}
f=open("test.text","rb")
data=pickle.loads(f.read())
print(data["func"]('alex'))
