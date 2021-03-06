# Binary tree
from turtle import *
# function to create the string according to which turtle would run!
def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

def draw_l_system_bt(instructions, angle, distance):
    lst = []
    lst1 = []
    i = 0
    for cmd in instructions:
        if cmd == '1' or cmd == '0':
            forward(distance)
        elif cmd == '+':
            left(angle)
        elif cmd == '-':
            right(angle)
        elif cmd == '[':
            lst1.append(i)
            lst.append([pos(), heading()])# storing position and angle
            i += 1
        elif cmd == ']':
            idx = lst1[-1]
            penup()
            setpos(lst[idx][0])# restoring position
            setheading(lst[idx][1])# restoring angle
            pendown()
            lst1.pop()
            


def main_bt(iterations, axiom, rules, angle, length=5.5, size=1, y_offset=-600,
        x_offset=0, offset_angle=0, width=3000, height=3000):

    inst = create_l_system(iterations, axiom, rules)
    setup(width, height)

    up()
    backward(-x_offset)
    left(90)
    backward(-y_offset)
    left(offset_angle)
    down()
    speed(0)
    pensize(size)
    draw_l_system_bt(inst, angle, length)
    hideturtle()

    exitonclick()

# let's print the pattern
axiom = "0"
rules = {"1":"11", "0":"1[+0]-0"}
iterations = 10
angle = 45
main_bt(iterations, axiom, rules, angle, length=1, size=1, y_offset=-600,
        x_offset=0, offset_angle=0, width=3000, height=3000)
