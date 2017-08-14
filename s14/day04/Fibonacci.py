__author__ = "sun wang"
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print (b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
g = fib(6)
while True:

    try:

        x = next(g)  #这是一个内置方法和两个下划线效果一样。

        print('g:', x)

    except StopIteration as e:

        print('Generator return value:', e.value)

        break
#print(fib(100))
# f=fib(100)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
