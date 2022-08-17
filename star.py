i = 1 
while i <= 5:
    print("* " * i)
    i+=1

n= 5
for i in range(n+1):
    print("* " * i)
x = "jabir"
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


def rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n*rec(n-1)
n = int(input("Enter the number: "))
if n < 0:
    print("factorial of negative does not exist")
else:
    res = rec(n)
    print(res)

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*", end="")
    print('')

def rec(n):
    if n==0:
        return 1
    else:
        res = n*rec(n-1)
        print(res)
        return res
n = int(input("Enter the number: "))

rec(n)
print(res)

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print("")

def pat(n):
    for i in range(n):
        print(" "*(n-i-1)+"* "*(i+1))
    
    for j in range(n-1,0,-1):
        print(" "*(n-j)+"* "*(j))

pat(5)

def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
y = shout
 
print(y('Hello'))