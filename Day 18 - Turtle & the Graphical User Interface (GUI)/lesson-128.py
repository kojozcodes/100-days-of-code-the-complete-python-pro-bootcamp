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




timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
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
def draw_shape(num_sides):
    degree_turn = 360/num_sides
    for side in range(num_sides):
        timmy.right(degree_turn)
        timmy.forward(100)


base_shape_sides = 3
for shape_side in range(base_shape_sides, 10):
    timmy.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()