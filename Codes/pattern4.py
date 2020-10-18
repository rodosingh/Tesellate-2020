from turtle import *
import random
#screen = turtle.Screen()
#p = turtle.Turtle()
setup(width = 900, height = 700)
bgcolor("black")
colormode(255)
tup = (255,239,0)
pencolor(tup)
speed(0)
def rapid(x):
    for i in range(500):
        forward(i)
        left(x)
rapid(132)
hideturtle()
done()
