__author__ = "sun wang"
import time

def deco(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print ("the run time of func is %s" % (start_time - stop_time))

def test1():
    time.sleep(3)
    print ("in the test1")

def test2():
    time.sleep(3)
    print ("in the test2")

deco(test1)
deco(test2)
#test1()
#test2()

