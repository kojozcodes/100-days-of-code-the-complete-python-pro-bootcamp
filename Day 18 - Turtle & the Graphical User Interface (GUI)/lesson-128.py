from math import degrees
from turtle import Turtle, Screen
import random

colors = [
    "Black", "Blue", "BlueViolet", "Brown", "CadetBlue", "Chocolate",
    "Crimson", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenRod",
    "DarkGray", "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen",
    "DarkOrange", "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen",
    "DarkSlateBlue", "DarkSlateGray", "DarkTurquoise", "DarkViolet",
    "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue", "FireBrick",
    "ForestGreen", "Fuchsia", "Gray", "Green", "Indigo", "Maroon",
    "MediumAquaMarine", "MediumBlue", "MediumOrchid", "MediumPurple",
    "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen",
    "MediumTurquoise", "MediumVioletRed", "MidnightBlue", "Navy",
    "Olive", "OliveDrab", "OrangeRed", "Orchid", "Purple",
    "Red", "RoyalBlue", "SaddleBrown", "SeaGreen", "Sienna",
    "SlateBlue", "SlateGray", "SteelBlue", "Teal", "Tomato",
    "Turquoise", "Violet"
]

directions = [0, 90, 180, 270]

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.speed(10)
timmy.pensize(10)

# timmy.forward(100)
# timmy.backward(200)
# timmy.right(90)
# timmy.left(180)
# timmy.setheading(0)

######## Challenge 1 - Draw a Square ############
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
#
# #shorter version
# for side in range(4):
#     timmy.forward(100)
#     timmy.left(90)


########### Challenge 2 - Draw a Dashed Line ########
# for line in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#

########### Challenge 3 - Draw Shapes ########
# def draw_shape(num_sides):
#     degree_turn = 360/num_sides
#     for side in range(num_sides):
#         timmy.right(degree_turn)
#         timmy.forward(100)
#
#
# base_shape_sides = 3
# for shape_side in range(base_shape_sides, 10):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side)


########### Challenge 4 - Random Walk ########

for _ in range(200):
    timmy.forward(20)
    timmy.color(random.choice(colors))
    timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()