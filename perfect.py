#  Perfect Number or Not

num = 6
sum =0
for i in range(1, num):
    if num%i==0:
        sum = sum + i

if sum == num:
    print('perfect')
else:
    print('no')


#  Strong ------->

num = 145
sum = 0
temp = num
while temp>0:
    r=temp%10
    fact = 1
    for i in range(1,r+1):
        fact = i*fact
    sum = sum + fact
    temp = temp//10

if num == sum:
    print('strong')
else:
    print('no')


# Reverse of a string ------->

def rev(x):
    s = ""
    for ch in x:
        s = s + ch
    return s

str = "dad"
val = rev(str)
if list(str) == list(val):
    print('palindrome')
else:
    print('not')
print(val)