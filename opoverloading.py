# Operator overloading

class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3
    
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)



s1 = Student(56,68)
s2 = Student(64,72)


s3 = s1 + s2

print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

a = 9

print(a)

print(s1.__str__())

print(s2)

# Methode overloading ------->

class Person:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s

stu1 = Person(67,73)

print(stu1.sum(12,23))

# Methode overriding ------->

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

a1 = B()
a1.show()