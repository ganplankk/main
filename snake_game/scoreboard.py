
from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/USER/PycharmProjects/snake_game/data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()
        print(self.high_score)


    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} / High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        new_data = self.high_score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


#!/usr/bin/env python

import datetime
import time
import sys
import amss.common.sfu as sfu

COMMANDS = [
	"show port-monitoring",
	"show port statistics"
]
SLEEP = 0.1

while True:
	print("Time: %s" % datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"))
	print(sfu.Sfu.execute(COMMANDS, config=False))
	sys.stdout.flush()
	time.sleep(SLEEP)
