__author__ = "sun wang"
import time
x=time.localtime()
#print(help(x))
#print(x.tm_year)
print(time.mktime(x))
print(time.strftime("%Y-%m:%d %H:%M:%S"))
print(time.strftime("%Y-%m:%d %H:%M:%S",time.localtime()))
print(time.strptime("2017-09:24 09:17:19","%Y-%m:%d %H:%M:%S"))
import datetime
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(3))
print(datetime.datetime.now()+datetime.timedelta(hours=3))
import random
x=random.random()
print(x)
y=random.randint(1,10)
print(y)
print(random.uniform(1,10))
l=[1,2,3,4,5,6]
random.shuffle(l)
print(l)