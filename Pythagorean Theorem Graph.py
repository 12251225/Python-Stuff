import math
import turtle as t

def draw_t(a,b):
    window = t.Screen()
    window.bgcolor("green")

    pen = t.Turtle()

    pen.forward(a)
    pen.left(b)
    pen.forward(a)
    pen.left(b)
    pen.forward(a)

    window.exitonclick()

draw_t(int(input("Enter for a: ")), int(input("Enter for b: ")))


def pt(a,b):

    #a2 = input("Enter number: ")
    c = (a**2) + (b**2)
    print(math.sqrt(c))
    print(id(c))


pt(int(input("Enter for a: ")), int(input("Enter for b: ")))
