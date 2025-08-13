from turtle import Turtle, Screen
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()
class Player(Turtle):

    # def __init__(self,pos):
    #     super().__init__()
    #     self.penup()
    #     self.shape("turtle")
    #     self.setheading(90)
    #     self.setpos(pos)

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def next_level(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    # def move_up(self):
    #     new_y = self.ycor() + 20
    #     self.goto(0, new_y)
