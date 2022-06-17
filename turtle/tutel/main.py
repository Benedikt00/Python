import turtle
from turtle import Screen, Turtle

tim = turtle.Turtle()
screen = Screen()

tim.color('red')
tim.pensize(5)
tim.shape('turtle')
tim.speed(-1)

def main():
    y = 500
    tim.penup()
    tim.goto(-300, 300)
    tim.pendown()


    while y >= 0:

        tim.forward(y)
        tim.right(90)
        tim.forward(y/2)
        tim.right(90)

        y = y-10

    screen.mainloop()

main()



