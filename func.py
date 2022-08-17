# function can return another function


def outer(x):
    def inner(y):
        return x + y
    return inner

z = outer(15)
print(z(10))

# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)

# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))


#defining a decorator

def hello_decorator(func):
 
    # inner1 is a Wrapper function in
    # which the argument is called
     
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
 
        # calling the actual function now
        # inside the wrapper function.
        func()
 
        print("This is after function execution")
         
    return inner1
 
 
# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")
 
 
# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)
 
 
# calling the function
function_to_be_used()

def decor(fun):
    def wrapper(n):
        any_list = fun(n)
        return [item*3 for item in any_list]
    return wrapper

@decor
def reverse(l):
    return l[::-1]

print(reverse([1,2,'a','ds']))

@decor
def upper_list(l):
    return [item.upper() for item in l]

print(upper_list(['a','b']))

@decor
def fib(c):
    result = []
    a,b = 0,1
    while b < c:
        result.append(b)
        a,b = b,a+b
    return result


print(fib(6))


def decorators(fun):
    def wrapper():
        result = fun()
        return result.upper()
    return wrapper

@decorators
def print_name():
    return "hello jabir"

x = print_name()
print(x)