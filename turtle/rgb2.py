import random
import turtle
from turtle import Turtle,Screen
tim = Turtle()
turtle.colormode(255)
def ran_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ran_col = (r, g, b)
    return ran_col

tim.shape("turtle")
tim.speed(10)
tim.pensize(7)

directions = [0,90,180,270]
for _ in range(200):
    tim.color(ran_col())
    tim.forward(45)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.mainloop()
