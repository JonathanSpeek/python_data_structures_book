# Write a program that takes the radius of a sphere (a floating point number) as input,
# and outputs the sphere's diameter, circumference, surface area, and volume
from math import pi

radius = float(input('What is the radius of the sphere: '))


def diameter(sphere):
    d = sphere * 2
    print('The diameter is: {d}'.format(d=d))


def circumference(sphere):
    c = 2 * pi * sphere
    print('The circumference is: {c}'.format(c=c))


def surface_area(sphere):
    s = 4 * pi * sphere**2
    print('The surface area is: {s}'.format(s=s))


def volume(sphere):
    v = (4/3) * pi * sphere**3
    print('The volume is: {v}'.format(v=v))

diameter(radius)
circumference(radius)
surface_area(radius)
volume(radius)
