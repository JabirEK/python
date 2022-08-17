num = 6
fact = 1
if num < 0:
    print("factorial of negative number is not exist")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact * i
    print(fact)
    

def rec_fact(n):
    if n == 1:
        return n
    else:
        return n * rec_fact(n-1)

num = -8
if num < 0:
    print("-ve number does not exist")
elif num==0:
    print('1')
else:
    print(rec_fact(num))