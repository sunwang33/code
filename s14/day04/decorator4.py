__author__ = "sun wang"
import time
def timer(func):
    def deco():
        start_time = time.time()
        func()
        stop_time = time.time()
        print ("the run time of func is %s" % (start_time - stop_time))
    return deco
@timer
def test1():
    time.sleep(3)
    print ("in the test1")
@timer
def test2():
    time.sleep(3)
    print ("in the test2")

#print(timer(test1))
#test1 = timer(test1)
test1()
test2()
# test1=deco(test1)
# test1()
# test2=deco(test2)
# test2()
#test1()
#test2()

