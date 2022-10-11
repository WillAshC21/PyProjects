import turtle
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
turtle.colormode(255)
rgb_colors = [(253, 251, 248), (254, 250, 252), (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40), (218, 87, 49), (174, 178, 231)]
print(rgb_colors)

timmy_the_turtle.hideturtle()
timmy_the_turtle.penup()
ypos = -250
timmy_the_turtle.setpos(-300, ypos)
timmy_the_turtle.speed("fastest")
for x in range(10):
    for _ in range(10):
        timmy_the_turtle.dot(20, random.choice(rgb_colors))
        timmy_the_turtle.forward(50)
    ypos += 50
    timmy_the_turtle.setpos(-300, ypos)

screen = Screen()
screen.exitonclick()