import random
from turtle import Turtle, Screen


screen = Screen()
bet = screen.textinput("make your bet", "which turtle do you think will win the race: ")
colors = ["red", "yellow", "blue", "green", "orange", "purple"]
ypos = [-90, -50, -10, 30, 70, 110]
screen.setup(500, 400)
is_race = False
racers = []

if bet:
    is_race = True

for x in range(0, 6):
        timmy = Turtle()
        timmy.penup()
        timmy.setpos(-230, ypos[x])
        timmy.color(colors[x])
        timmy.shape("turtle")
        racers.append(timmy)

while is_race:
    for a in racers:
        if a.xcor() > 230:
            is_race = False
            win = a.pencolor()
            if win == bet:
                print(f"{bet} has won")
            else:
                print(f"{bet} has lost")

        r_distance = random.randint(0, 10)
        a.forward(r_distance)

screen.exitonclick()