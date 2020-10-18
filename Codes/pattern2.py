import turtle

t = turtle.Turtle()

colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
for x in range(300):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
    t.hideturtle()
turtle.done()
