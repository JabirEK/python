from operator import le
from unittest import result


price = 47 
text = "new offer"
item = 23
txt = "mangoes price is {0} rupees only {1} {1} batch {2:.2f}"
myorder = "{carname} is {model} model"
print(txt.format(price, text, item))
print(myorder.format(carname="ford", model="Mustang"))

# x = 2

try:
  print(price)
except:
  print("Something went wrong")
else:
  print("hi")
finally:
  print("The 'try except' is finished")


# Bubble sort in Python

# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        print(key)
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
        


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)

#Stack implementation in python


#Creating a stack
def create_stack():
    stack = []
    return stack


# Creating an empty stack
def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()


stack = create_stack()
push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))
print("popped item: " + pop(stack))
print("popped item: " + pop(stack))
push(stack, "trim")
print("stack after popping an element: " + str(stack))
print("not empty: ", check_empty(stack))

#Queue implementation in Python

class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    # def size(self):
    #     # return len(self.queue)
    #     print(len(self.queue))


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()
q.dequeue()


print("After removing an element")
q.display()
q.size()

class Triangle:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b
    self.c = c

  def perimeter(self):
    result = self.a + self.b + self.c
    return result


t1 = Triangle(3, 4, 6)
result = t1.perimeter()
print(result)

