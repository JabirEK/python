class IncNumbers:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        if self.x < 11:
            n = self.x
            self.x += 1
            return n
        else:
            raise StopIteration

obj = IncNumbers()

ite_obj = iter(obj)
# print(next(ite_obj))
# print(next(ite_obj))
# print(next(ite_obj))
for i in ite_obj:
    print(i)

print(next(ite_obj))


# def f1():
#     x = 100
#     return x

# x = f1()+1
# print(x)


class Code:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Show(self):
        return f"the name: {self.name} age: {self.age}"

n1 = Code('jabir',25)
x = n1.Show()
print(x)