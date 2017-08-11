__author__ = "sun wang"
f1 = open("yesterday3",'r+',encoding="utf-8")
f2 = open("yesterday2.bak",'w',encoding='utf-8')
file1 = f1.readlines()
for i in file1:
    if file1.index(i) == 29:
        i= "有那么多肆意的快乐等Alex享受\n"
        f2.write(i)
    else:
        f2.write(i)

