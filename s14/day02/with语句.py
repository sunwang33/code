__author__ = "sun wang"
"""
with open("yesterday2",'r',encoding="utf-8") as f:
    print (f.readline())
"""
with open("yesterday2",'r',encoding="utf-8") as f , \
    open("yesterday2", 'r' , encoding="utf-8") as f2 :
    for line in f:
        print (line)