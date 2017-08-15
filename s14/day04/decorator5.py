# Author:Sun Wang
import time
def decorator(func):
    def warpper(name,times):
        start_time = time.time()
        time.sleep(3)
        func(name, times)
        stop_time = time.time()
        print ("the run time is %s." %(stop_time - start_time))
    return warpper


@decorator
def test1(name,times):
    print ("%s is %s time to write decorator." %(name,times))

test1('sun','the first')

