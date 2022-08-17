newlist = [x for x in range(1, 101) if x%5==0 and x%3==0]
print(newlist)

# Normal way
ls1 = [1,2,3,4,5,6,7,8,9,10]

new = []
for x in ls1:
    if x%2==0:
        new.append(x)
print(new)

# List comprehension

z = [x for x in ls1 if x%2==0]
print(z)

l1 = ["a", "cat"]
l2 = [1,2,3,"jack"]

l1.append(l2)
print(l1)

for x in l2:
    l1.append(x)
print(l1)

l1.extend(l2)
print(l1)

# ls1 = [1,2,3]
# ls2 = ls1.copy()
# print(ls2)

# ls1 = [1,2,3]
# ls2 = [4,5,6]
# ls3 = ls1+ls2
# print(ls3)

# ls2 = [4,5,6,2,3,9]
# # ls2.sort(reverse=True)
# # print(ls2)
# ls2.reverse()
# print(ls2)


# ls1 = [1,2,3]
# ls1[2] = "cat"
# print(ls1)

