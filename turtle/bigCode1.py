import random
from turtle import Turtle,Screen
tim = Turtle()
tim.shape("turtle")
tim.speed(2)
#tim.color("blue")
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

colours = ["red", "orange",
           "yellow", "green", "blue", "purple"]
for shapes_sides_n in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(shapes_sides_n)
screen = Screen()
screen.mainloop()
