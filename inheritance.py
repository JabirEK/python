class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display(self):
        print("Polygon")

    def perimeter(self):
        result = sum(self.sides)
        return result

class Triangle(Polygon):
    def display(self):
        print("Triangle hav 3 sides")
        Polygon.display(self)

class Quadrilateral(Polygon):
    def display(self):
        print("i have 4 sides")
        super().display()

t1 = Triangle([2, 8, 10])

print(t1.perimeter())
t1.display()
t2 = Quadrilateral([2,3,4,5])
print(t2.perimeter())
t2.display()
