import re

x = r'10*'

print(re.search(x, 'abc10005678'))


# map function
def cube(num):
    return num ** 3
print(list(map(cube, [1,2,3,4,5])))

x = [1,-3,5,-6,-7]
print(list(map(abs, x)))

y = [1,-3,5,-6,-7]

xy = list(map(lambda z:z+1, y))
print(xy)

# Filter function
def positive(num):
    return True if num>0 else False
my_list = [-3,4,-5,9,29]
print(list(filter(positive, my_list)))

x = [2,3,5,8,1,12,42,60,32]

print(list(filter(lambda z:z%2==0, x)))

print(list(filter(lambda y:y.isupper(), "AppLe")))


