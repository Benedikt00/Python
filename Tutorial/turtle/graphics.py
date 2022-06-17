import turtle
from turtle import *
import keyboard
import random

tim = turtle.Turtle()
tim.speed(0)
tim.width(5)

color = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

def up():
    tim.setheading(90)
    tim.forward(100)
def left():
    tim.setheading(180)
    tim.forward(100)
def right():
    tim.setheading(0)
    tim.forward(100)
def back():
    tim.setheading(270)
    tim.forward(100)
def middl():
    tim.penup()
    tim.setpos(0,0)
    tim.pendown()
    
def clickleft(x,y):
    tim.color(random.choice(color))

def clickright(x,y):
    tim.stamp()

turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')
turtle.onkey(back, 'Down')
turtle.onkey(middl, 'BackSpace')
turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)
turtle.mainloop()
