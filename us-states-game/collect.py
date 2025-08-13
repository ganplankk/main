from turtle import Turtle

class CollectState(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.state = state
        self.x = x
        self.y = y
        self.write_state()

    def write_state(self):
        self.penup()
        self.goto(self.x, self.y)
        self.write(self.state)
