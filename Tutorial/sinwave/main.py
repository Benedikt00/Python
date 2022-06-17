import math
import turtle

wn = turtle.Screen()

s = turtle.Turtle()
s.speed(0)


fred = turtle.Turtle()
fred.speed(0)


d = turtle.Turtle()
d.speed(0)

f = turtle.Turtle()
f.color('red')
f.speed(0)

sc = turtle.Screen()
sc.reset()

sc.setworldcoordinates(0,-1.5,720,1.5)

fred.penup()
s.penup()
d.penup()

for angle in range(720):


    y = math.sin(math.radians(angle))
    fred.goto(angle,y)
    fred.pendown()


    x = math.sin(math.radians(angle + 120))
    s.goto(angle,x)
    s.pendown()


    z = math.sin(math.radians(angle + 240))
    d.goto(angle,z)
    d.pendown()

    f.goto(angle, 0)


wn.exitonclick()


