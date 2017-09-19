# # Author:Sun Wang
# info = {
#     'name':'alex',
#     'age': 22
# }
#
# f=open('test.text','w')
# f.write(str(info))
# f.close()
#
# Author:Sun Wang
import pickle
def sayhi(name):
    print("hello,",name)
info = {
    'name':'alex',
    'age': 22 ,
    'func':sayhi
}
# f=open('test.text','r')
#data = f.read()
# f.close()
# print(data['name'])
f=open('test.text','wb')
#print(json.dumps(info))
f.write(pickle.dumps(info))
f.close()
print()