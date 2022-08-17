lo = 2
up = 50
for num in range(lo, up+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)