num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp%10
    sum = sum + digit**3
    temp = temp//10
if num == sum:
    print('armstrong number')
else:
    print('not armstrong')