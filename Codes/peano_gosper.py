from turtle import *

# function to create the string according to which turtle would run!.
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
def draw_l_system(instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            forward(distance)
        elif cmd == '+':
            right(angle)
        elif cmd == '-':
            left(angle)

# function to execute the pattern.
def main(iterations, axiom, rules, angle, length=8, size=2, y_offset=0,
        x_offset=0, offset_angle=0, width=450, height=450):

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
    draw_l_system(inst, angle, length)
    hideturtle()

    exitonclick()
    
# specify features
# Peano-Gosper Curve
axiom = "FX"
rules = {"X":"X+YF++YF-FX--FXFX-YF+", "Y":"-FX+YFYF++YF+FX--FX-Y"}
iterations = 4 # TOP: 6
angle = 60
main(iterations, axiom, rules, angle)
