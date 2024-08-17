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
for line in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()