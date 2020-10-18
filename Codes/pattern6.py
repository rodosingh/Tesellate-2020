from turtle import *
speed(0)
setup(width = 900, height = 700)
bgcolor("black")
lst = ["purple", "red", "orange", "blue", "green"]
for i in range(300):
    color(lst[i%5])
    pensize(i/10+0.5)
    forward(i)
    left(59)
penup()
hideturtle()
done()
