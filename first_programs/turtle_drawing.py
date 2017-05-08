from turtle import *


def draw_square(t, x, y, length):
    """Draws a square with the given turtle, an
    upper-left corner point (x, y), and a side’s length."""

    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)


def draw_polygon(t, vertices):
    """Draws a polygon from a list of vertices.
    The list has the form [(x1, y1), ..., (xn, yn)]."""

    t.up()
    (x, y) = vertices[-1]
    t.goto(x, y)
    t.down()
    for (x, y) in vertices:
        t.goto(x, y)


def draw_spiral(t, color_hex_a, color_hex_b):
    """Draws a spiral in 2 different colors, given a turtle object and 
    2 hex color values or basic color string, ex. 'blue'"""

    t.pencolor(color_hex_a)
    for i in range(100):
        t.forward(50)
        t.left(130)

    t.pencolor(color_hex_b)
    for j in range(100):
        t.forward(75)
        t.left(130)
