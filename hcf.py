#   HCF  ----->


def hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf = i
    return hcf

num1=54
num2=24
print('hcf is: ', hcf(num1,num2))

#  LCM ------>
def lcm(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if greater%x==0 and greater%y==0:
            lcm = greater
            break
        greater += 1
    return lcm

num1=54
num2=24
print('lcm is: ', lcm(num1,num2))


def lcmm(x=None,y=None,z=None):
    if x!=None and y!=None and z!=None:
        if x>y and x>z:
            gret = x
        elif y>x and y>z:
            gret = y
        else:
            gret = z
        while True:
            if gret%x==0 and gret%y==0 and gret%z==0:
                lcm = gret
                break
            gret+=1
        return lcm
    elif x!=None and y!=None:
        if x>y:
            gret = x
        else:
            gret = y
        while True:
            if gret%x==0 and gret%y==0:
                lcm = gret
                break
            gret =+1
        return lcm
    else:
        print("lcm single number is not defined")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the first number: "))
# num3 = int(input("Enter the first number: "))
num1=12
num2=38
print(lcmm(num1,num2))
