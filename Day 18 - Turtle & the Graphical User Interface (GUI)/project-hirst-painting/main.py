# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
import turtle
from turtle import Turtle, Screen
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_rgb = (r, g, b)
#     rgb_colors.append(color_rgb)
#
# print(rgb_colors)

timmy = Turtle()
turtle.colormode(255)
timmy.home()
timmy.speed(0)
timmy.penup()

color_list = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
    (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
    (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
    (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

vertical_gap = 50
timmy.setx(-250)
timmy.sety(-250)

for _ in range(100):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if timmy.xcor() == 250.0:
        timmy.setx(-250)
        timmy.sety(timmy.ycor() + vertical_gap)
timmy.home()

screen = Screen()
screen.exitonclick()