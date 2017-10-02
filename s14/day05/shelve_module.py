__author__ = "sun wang"

import shelve,datetime

# d = shelve.open('shelve_test')  # 打开一个文件
#
# info = {'age':22 , "job":'it'}
#
# name = ["alex", "rain", "test"]
# d["name"] = name  # 持久化列表
# d["info"] = info
# d["date"] = datetime.datetime.now()
# d.close()

d = shelve.open('shelve_test')
print(d.get('name'))
print(d.get('info'))
print(d.get('date'))