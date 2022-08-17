list1 = [3, 5, 7, 8, 23, 45]
print(len(list1))
thislist = list(("apple", "banana", 6, 8, 9))
try:
    del thislist
    print(thislist)
except:
    print("thislist is completely deleted")

# print(thislist)
print(list1)
list1[1] = "apple"
list1.insert(4, "banana")
list1.insert(0, "jabir")
list1.append("ek")
print(list1)
list1.remove(45)
list1.pop(3)
del list1[4]
list1.clear()
print(list1[0:-1])


ls1 = [2, 4, 6]
ls2 = [3, 5, 7]
ext = [8, 10]
ls3 = ls1 + ls2
print(ls3)
ls1.extend(ext)
print(ls1)

for x in ls2:
    ls1.append(x)
print(ls1)

for x in ls3:
    ls1.append(x)
print(ls1)

ls1.sort()
print(ls1)

ls1.reverse()
print(ls1)


