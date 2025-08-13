from turtle import Turtle, Screen

class Tom(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.clear()
        self.setheading(90)
        self.shape("turtle")
        self.goto(0,-230)

