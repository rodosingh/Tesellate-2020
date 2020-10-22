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

# draw along the above string
def draw_l_system_fp(instructions, angle, distance):
    lst = []
    lst1 = []
    i = 0
    for cmd in instructions:
        if cmd == 'F':
            forward(distance)
        elif cmd == '+':
            right(angle)
        elif cmd == '-':
            left(angle)
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
            

# function to execute the pattern
def main_fp(iterations, axiom, rules, angle, length=5.5, size=1, y_offset=-600,
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
    draw_l_system_fp(inst, angle, length)
    hideturtle()

    exitonclick()
    
    
# Thin Bush

axiom = "F"
rules = {"F":"FF+[+F-F-F]-[-F+F+F]"}
iterations = 4 # TOP: 6
angle = 22.5
main_fp(iterations, axiom, rules, angle, length=10, size=1, width=3000, height=3000, y_offset = -480)
