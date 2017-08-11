__author__ = "sun wang"

def func1():
    """testing1"""
    print ('in the func1')
    return 0
def func2():
    """testing2"""
    print ('in the func2')

x = func1()
y = func2()
print ('from func1 return is %s' %x)
print ('from func2 return is %s' %y)