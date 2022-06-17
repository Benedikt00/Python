import turtle
from turtle import Screen, Turtle

try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp


mp.dps = 5000  # set number of digits

mp = str(mp.pi)

nl = list(mp)

nl[1] = "0"

tim = turtle.Turtle()
screen = Screen()
#screen.screensize(canvwidth=500, canvheight=400)

tim.color('black')
tim.pensize(2)
tim.shape('turtle')
tim.hideturtle()
tim.speed(-1)

def getang(num, base):
    return num* (360/base)

def main():

    for x in range(len(nl)):
        ang = getang(int(nl[x]), 9)
        tim.left(ang)
        tim.forward(15)

    turtle.done()
main()

