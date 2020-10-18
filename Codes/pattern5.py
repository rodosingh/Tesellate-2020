from turtle import *
from random import randint

setup(width = 900, height = 700)
speed(0)
colormode(255)
bgcolor("black")
pensize(7)

x = 1
while x<600:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color(r,g,b)
    fd(x)
    rt(119)
    x = x+1
penup()
color("purple")
goto(-20,-300)
hideturtle()
done()
