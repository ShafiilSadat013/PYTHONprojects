import random
import turtle
from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.pensize(1)
tim.speed("fastest")

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def draw(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        cur_heading =  tim.heading()
        tim.setheading(cur_heading + gap)
        tim.circle(100)

draw(3)
screen = Screen()
screen.mainloop()



##Without draw Function
import random
import turtle
from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.pensize(2)
tim.speed("fastest")

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

for _ in range(400):
    tim.color(random_color())
    tim.circle(100)
    cur_heading =  tim.heading()
    tim.setheading(cur_heading+10)
    tim.circle(100)
screen = Screen()
screen.mainloop()
