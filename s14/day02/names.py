#Author： sun wang
import copy
#names = [ "ZhangYang" , "GuYun" , "XiangPeng" , "XuLiangChen"]
names = [ "4ZhangYang" , "#!GuYun" , "xXiangPeng" , ["alex","jack"], "Chenronghua" , "XuLiangChen"]
print (names[0:-1:2])
"""
for i in names:
    print (i)
"""
name2 = copy.deepcopy(names)
print (names)
print (name2)
names[names.index("xXiangPeng")] = "向鹏"
names[3][0] = "ALEXANDER"
print (names)
print (name2)
"""
print ( names )
print ( names[0] ,names[2] )
print ( names[1:2])

print ( names[-3:-1])
print ( names[-2:-1])

print ( names[-1:-3])
"""
"""
names.append("LeiHaidong")
names.insert(1,"ChenRonghua")
names.insert(3, "Xinzhiyu")
print (names)
#names[2] = "XieDi"
#names.remove("ChenRonghua")
#del names[1]
#names.pop(1)
#print (names.index("XieDi"))
names.insert(5 , "ChenRonghua")
print (names)
print (names.count("ChenRonghua"))
#names.reverse()
#names.sort()
print (names)
names2 = [1,2,3,4]
names.extend(names2)
print (names)
del names2
print (names2)
"""
