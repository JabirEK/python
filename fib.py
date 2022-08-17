# n = 10
# n1, n2 = 0, 1
# count = 0
# while count < n:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2 
#     n2 = nth
#     count +=1

def fib(n):
    a=0
    b=1
    if n<=0:
        print("negative number does not have fib series")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
          c = a + b
          a = b
          b = c
          print(c)

fib(-5)
print("<----------------->")
def rec_fib(n):
    if n <= 1:
        return n
    else:
        return (rec_fib(n-1)+rec_fib(n-2))
nterms = 10
for i in range(nterms):
    print(rec_fib(i))