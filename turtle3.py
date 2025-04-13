import turtle as t
from turtle import Turtle
import random
tim = Turtle()
colors =["purple","red","green","blue","yellow","black"]

def draw_shapes(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)
for shapes_size in range(3 ,13):
    tim.color(random.choice(colors))
    draw_shapes(shapes_size)