from turtle import Screen, Turtle

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len = 1, stretch_wid = 5)
        self.setpos(pos)
        self.color("black")

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
