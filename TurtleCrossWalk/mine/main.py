import time
from turtle import Turtle, Screen
from tom import Tom

screen = Screen()
tom = Tom()
screen.setup(600,600)
game_on = 0
screen.tracer(0)

while game_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
