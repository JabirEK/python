from turtle import *
import tkinter as TK
speed(0)
bgcolor('black')
color('orange')
hideturtle()

n = 1
p = True

while True:
    circle(n)
    if p:
        n = n - 1
    else:
        n = n + 1
    if n == 0 or n==60:
        p = not p
    left(1)

done()

list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

list2 = list(set(list1))

list2.sort()

print(list2)

print(list2[-2])


import module as m
print(m.generate_key('apple'))