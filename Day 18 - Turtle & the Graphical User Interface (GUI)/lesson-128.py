import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270]
timmy.speed(0)
# timmy.pensize(10)

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

# for _ in range(200):
#     timmy.forward(20)
#     timmy.color(random_color())
#     timmy.setheading(random.choice(directions))

########### Challenge 5 - Spirograph ########
def draw_spirograph(space_size):
    for _ in range(int(360 / space_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + space_size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()