__author__ = "sun wang"
"""
def test(*args):
    print (args)
#test(1,2,3,4,5)
test(*[1,2,3,4,5])
"""
"""
def test(name,**kwargs):
    print (name)
    print (kwargs)
#test(name='alex',age=8,sex='F')
test('alex',age=8,sex='m')
"""

def test(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST4")
def logger(source):
     print ("FROM %s" % source)
test('alex',age=34,sex='m',hobby='tesla')