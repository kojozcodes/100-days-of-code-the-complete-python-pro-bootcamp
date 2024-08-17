from math import degrees
from turtle import Turtle, Screen

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
while base_shape_sides <= 10:
    draw_shape(base_shape_sides)
    base_shape_sides += 1

screen = Screen()
screen.exitonclick()