from turtle import *
import numpy as np

# Cantor set

# Binary tree

# function to create the string according to which turtle would run!
def create_l_system_cantor(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return start_string
    else:
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        return end_string
    #for _ in range(iters):
    #    end_string = "".join(rules[i] if i in rules else i for i in start_string)
    #    start_string = end_string

    

def draw_l_system_cantor(instructions, distance):
    for cmd in instructions:
        if cmd == 'A':
            forward(distance)
        else:
            penup()
            forward(distance)
            pendown()
            


def main_cantor(iterations, axiom, rules,
                length=1600, size=3, y_offset=0, x_offset=-900, offset_angle=0, width=3000, height=3000):
    
    setup(width, height)
    speed(0)
    sizes = np.linspace(1,size,iterations)
    for i in range(iterations):
        up()
        setpos(x_offset, y_offset-(8*i))
        left(offset_angle)
        down()
        speed(0)
        pensize(sizes[iterations - 1 - i])
        inst = create_l_system_cantor(i, axiom, rules)
        draw_l_system_cantor(inst, length)
        length = length/3.0
        axiom = inst
    hideturtle()
    exitonclick()

# let's print the pattern
axiom = "A"
rules = {"A":"ABA", "B":"BBB"}
iterations = 10
main_cantor(iterations, axiom, rules)
