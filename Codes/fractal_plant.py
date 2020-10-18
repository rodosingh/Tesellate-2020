# fractal plant

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
            


def main_fp(iterations, axiom, rules, angle, length=5.5, size=1, y_offset=-600,
        x_offset=0, offset_angle=0, width=3000, height=3000):

    inst = create_l_system(iterations, axiom, rules)
    setup(width, height)

    up()
    backward(-x_offset)
    left(65)
    backward(-y_offset)
    left(offset_angle)
    down()
    speed(0)
    pensize(size)
    draw_l_system_fp(inst, angle, length)
    hideturtle()

    exitonclick()

# let's print the pattern
axiom = "X"
rules = {"X":"F+[[X]-X]-F[-FX]+X", "F":"FF"}
iterations = 6
angle = 25
main_fp(iterations, axiom, rules, angle)