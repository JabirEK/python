num = 13
if num > 1:
    for i in range(2, num):
        if num%i==0:
            print("not a prime")
            break
    else:
        print("is aprime")
else:
    print("not a prime")