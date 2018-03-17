# Turtle Shape Functions

import turtle 
from turtle import * 

shape('turtle')
mode('logo')
speed(10)

#create functions for each shape
def p():
    pendown()
    for i in range(5):
        forward(100)
        right(144)
    penup()


def h():
    pendown()
    for i in range(6):
        forward(100)
        right(60)
    penup()

def o():
    pendown()
    for i in range(8):
        forward(100)
        left(45)
    penup()

def s():
    pendown()
    for i in range(5):
        forward(100)
        right(144)
    pendup()


