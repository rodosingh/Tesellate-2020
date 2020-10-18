from turtle import *
from random import randint

setup(width = 900, height = 700)
speed(0)
colormode(255)
bgcolor("black")

x = 1
while x<550:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    #color(r,g,b)
    color(255,255,0)
    fd(x)
    rt(90.11)
    x = x+1
hideturtle()
done()
