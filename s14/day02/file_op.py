__author__ = "sun wang"
#打开文件并读取里面的内容。
#data = open("yesterday",encoding="utf-8").read()
#f = open("yesterday2","r",encoding="utf-8")
#data = f.read()
#data2 = f.read()
#print (data)
#print ("------data2--------",data2 )
#f.write("when i was young i listen the radio.\n")
#data = f.read()
#print ("----read", data)


#f=open("yesterday2",'r',encoding="utf-8")

#for i in range(5):
    #print(f.readline())

#f=open("yesterday2",'r',encoding="utf-8")
#print(f.readlines())
'''
f=open("yesterday2",'r',encoding="utf-8")
new=[]
for line in f.readlines():
    new.append(line)
    if new.index(line) != 9 :
        print(line.strip())
'''
'''
f = open('yesterday2','r',encoding='utf-8')
for index,line in enumerate(f.readlines()):
    if index == 9:
        print ("---分割线---")
        continue
    print (line)
'''
'''
f = open("yesterday",'r',encoding='utf-8')
count = 0
for line in f:
    count += 1
    if count == 9:
        print("---分割线---")
        continue
    print(line)
'''
"""
f = open("yesterday2",'r',encoding="utf-8")
print(f.tell())
for i in range(3):
    print(f.readline())
print(f.tell())
f.seek(0)
print(f.tell())
print (f.readline())
print(f.encoding)
print (f.fileno())
print (f.name)
print (f.seekable())
print (f.flush())
print(f.buffer)
"""
"""
f = open("yesterday2",'a',encoding="utf-8")
f.truncate(10)
"""
"""
f = open("yesterday2",'a',encoding="utf-8")
f.seek(10)
f.truncate(20)

"""
"""
f = open("yesterday2",'w+',encoding="utf-8")
for i in range(3):
    print(f.readline())
print (f.tell())
f.write("--------diao---------")
print (f.readline())
"""
"""
f = open("yesterday2",'w+',encoding="utf-8")
for i in range(4):
    f.write("--------diao--------\n")
print (f.tell())
f.seek(10)
print(f.readline())
f.write("should be in the begining of the second line.")
"""
"""
f = open("yesterday2",'rb')
for i in range(3):
    print (f.readline())
"""
f = open("yesterday2",'wb')
f.write("hello binary\n".encode("utf-8"))

