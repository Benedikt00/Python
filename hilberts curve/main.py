import turtle
from turtle import *

t = turtle.Turtle()

t.color('red')
t.pensize(1)

t.speed(-1)

def hilbert(level, angle, step):
    # Input Parameters are numeric
    # Return Value: None
    if level == 0:
        return

    t.right(angle)
    t.hilbert(level - 1, -angle, step)

    t.forward(step)
    t.left(angle)
    t.hilbert(level - 1, angle, step)

    t.forward(step)
    t.hilbert(level - 1, angle, step)

    t.left(angle)
    t.forward(step)
    t.hilbert(level - 1, -angle, step)
    t.right(angle)


def main():
    level = int(input("Enter Level of hilbert-Curve: "))
    size = 200
    t.penup()
    t.goto(-size / 2.0, size / 2.0)
    t.pendown()

    # For positioning turtle
    hilbert(level, 90, size / (2 ** level - 1))
    done()


if __name__ == '__main__':
    main()
