import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.penup()

color_list = [(244, 231, 212), (215, 230, 243), (246, 224, 236),
              (120, 177, 208), (224, 243, 234), (225, 158, 90),
              (232, 206, 99), (211, 130, 165), (192, 172, 17),
              (36, 114, 164), (172, 12, 48), (213, 76, 116),
              (28, 141, 73), (202, 64, 25), (24, 180, 142),
              (15, 173, 206), (241, 162, 189), (233, 78, 48),
              (136, 191, 169), (12, 26, 80), (60, 17, 45),
              (162, 59, 97), (129, 213, 232), (69, 21, 14),
              (171, 18, 12), (102, 115, 179), (25, 47, 132),
              (241, 167, 157), (148, 215, 197), (171, 186, 226)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 101
for dot_c in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_c % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


tim.hideturtle()
screen = Screen()
screen.mainloop()
