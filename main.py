class Person:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def address(self):
        print(self.name, self.contact)
class Patient(Person):
    pass
class Doctor(Person):
    pass

doct = Doctor("jabir", 12345)
patt = Patient("arun", 98765)

doct.address()
patt.address()