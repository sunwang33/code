# # # # # # # # # # # # # __author__ = "sun wang"
# # # # # # # # # # # # # # #print(all([1,-5,3]))
# # # # # # # # # # # # # # #print(any([1,-5,3]))
# # # # # # # # # # # # # # #print(any([0,-5,3]))
# # # # # # # # # # # # # # #print(any([]))
# # # # # # # # # # # # # # b=ascii([1,'a','你好'])
# # # # # # # # # # # # # # print(type(b))
# # # # # # # # # # # # # #print([bin(2)])
# # # # # # # # # # # # # print (bool([1]))
# # # # # # # # # # # # # print (bool([0]))
# # # # # # # # # # # # # print (bool([]))
# # # # # # # # # # # # # a = bytes("abcde",encoding="utf-8")
# # # # # # # # # # # # # print (a.capitalize() , a)
# # # # # # # # # # # # b= bytearray("abcde",encoding="utf-8")
# # # # # # # # # # # # print (b[0])
# # # # # # # # # # # # b[1]=100
# # # # # # # # # # # # print (b)
# # # # # # # # # # # print (callable([]))
# # # # # # # # # # def sayhi():pass
# # # # # # # # # # # print(callable(sayhi))
# # # # # # # # # # print (chr(97))
# # # # # # # # # # print (ord('d'))
# # # # # # # # # # print (complex("1+2j"))
# # # # # # # # # # print (complex("1"))
# # # # # # # # # STR="abcdef"
# # # # # # # # # # print(eval(STR))
# # # # # # # # # # (lambda n:print(n))(5)
# # # # # # # # # # print(lambda n:print(n))
# # # # # # # # # calc=lambda n:print(n)
# # # # # # # # # calc(5)
# # # # # # # # calc=lambda n:3 if n<4 else n
# # # # # # # # print(calc(2))
# # # # # # # res = filter(lambda n:n>5,range(10))
# # # # # # # for i in res:
# # # # # # #     print (i)
# # # # # #res = map(lambda n:n*n ,range(10))
# # # # # # for i in res:
# # # # # #     print (i)
# # # # # #res = map(lambda n:n*2 ,range(10))
# # # # # res = [lambda i:i*2 for i in range(10)]
# # # # # for i in res:
# # # # #     print(i)
# # # # import functools
# # # # res=functools.reduce(lambda x,y : x+y , range(1,10))
# # # # print (res)
# # # a = frozenset([1,4,333,212,33,33,12,4])
# # # a.add(999)
# # # b =set([1,4,333,212,33,33,12,4])
# # # b.add(999)
# # # print(b)
# #
# # print(globals())
# # print(hash('alex'))
# print(hex(10))
a = {1:'a' , 2:'b',3:'c' }
print(sorted(a.items() , key=lambda x:x[1]))