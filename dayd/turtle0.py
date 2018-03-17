#test out the turtle 

import turtle
from turtle import *

turtle.shape('turtle')
turtle.mode('logo')
turtle.speed(10)

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)

pencolor('orange')
width(10)
circle(180)

for i in range(5):
    forward(100)
    right(144)

mainloop()