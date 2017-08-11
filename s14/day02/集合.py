__author__ = "sun wang"

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)
print(list_1 , type(list_1))
list_2 = set([2,6,0,66,22,4])
print(list_1 , list_2 )
print(list_1.intersection(list_2))
print(list_1.union(list_2))
print(list_1.difference(list_2))
print(list_2.difference(list_1))
print(list_1.issubset(list_2))
print(list_1.issuperset(list_2))
list_3 = set([1,3,7])
print(list_3.issubset(list_1))
print (list_1.symmetric_difference(list_2))
name_1="分割线"
print(name_1.center(50,'-'))


list_4 = set([5,6,8])
print(list_3.isdisjoint(list_4))
#求交集
print (list_1 & list_2)
print (list_1 | list_2 )
print (list_1 - list_2 )
print (list_1 ^ list_2)
list_1.add(999)
print (list_1)

list_1.update([10,37,42])
print(list_1)

list_1.remove(42)
print(list_1)
list_1.add(42)
print(list_1)

print(len(list_1))

if 42 in list_1:
    print ("42 in list_1")

print(list_1.pop())
print(list_1)
list_1.discard(888)
list_1.discard(3)
print(list_1)
