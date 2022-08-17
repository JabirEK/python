num = 121
rev = 0
temp = num
while temp >0:
    digit = temp%10
    rev = rev*10+digit
    temp = temp//10

print(rev)


def pal(x):
    rev = 0
    while x > 0:
        digit = x%10
        rev = rev*10+digit
        x=x//10
    return rev
num=121 
value = pal(num)
if num == value:
    print('Yes')
else:
    print('no')


