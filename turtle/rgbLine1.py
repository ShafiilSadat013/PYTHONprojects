import random
from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.speed("10")
tim.pensize(7)

colour = [
    "red", "orange", "yellow", "green", "blue", "indigo", "violet",
    "crimson", "tomato", "coral", "gold", "lime", "cyan", "skyblue", "magenta",
    "pink", "salmon", "turquoise", "springgreen", "orchid", "plum", "khaki",
    "lavender", "peru", "sienna", "chocolate", "darkorange", "deeppink",
    "darkviolet", "mediumslateblue", "mediumorchid", "dodgerblue", "royalblue",
    "forestgreen", "limegreen", "mediumseagreen", "aqua", "aquamarine",
    "fuchsia", "hotpink", "firebrick", "tomato", "orangered", "mediumvioletred"
]
directions = [0,90,180,270]
for _ in range(500):
    tim.color(random.choice(colour))
    tim.forward(45)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.mainloop()
