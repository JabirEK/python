class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("The config is: ",self.cpu,self.ram)


comp1 = Computer('i5 processor','8gb ram')
comp2 = Computer('i7 processor','16gb ram')
# Computer.config(comp1)
# Computer.config(comp2)

comp1.config()
comp2.config()

class Computer:
    def __init__(self):
        self.name = "Navin"
        self.age = 15
    
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()
c1.age = 10
c2.age = 18
if c1.compare(c2):
    print("same age")
else:
    print("Not same age")

print(c1.age)
print(c2.age)

#  Instance variable and class variable(static variable)

class Car:
    wheel = 4
    def __init__(self):
        self.mil=10
        self.com="BMW"

car1 = Car()
car2 = Car()
car1.mil=18
Car.wheel=6
print(car1.mil,car1.com,car1.wheel)
print(car2.mil,car2.com,car2.wheel)

#Instance method, class method and static method

class Student:
    school = "gmhs raroth"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        average = (self.m1+self.m2+self.m3)/3
        return average

    @classmethod
    def getSchool(cls):
        value = cls.school
        print(value)

    @staticmethod
    def info():
        print("This is static method")
    

s1 = Student(45,39,48)
s2 = Student(47,46,50)

print(s1.avg())
print(s2.avg())

Student.getSchool()  

Student.info()

#Inner class --------->

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i3"
            self.ram = '8gb'

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('jabir', 17)
s1.show()
# lap1 = s1.lap
# print(lap1.cpu)
lap1 = Student.Laptop()
print(lap1.cpu)

#Encapsulation

class Encap:
    __a = 10
    def __dispaly(self):
        print("encapsulation")

obj1 = Encap()
obj1.dispaly()
print(obj1.__a)
obj2 = Encap()
obj2.__dispaly()
