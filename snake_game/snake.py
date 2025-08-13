import turtle
from turtle import Screen, Turtle
import time
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

def snake_append():
    snake_cnt = len(STARTING_POSITIONS)

class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]
        self.tail = self.snakes[len(self.snakes) - 1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = turtle.Turtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.setpos(position)
        self.snakes.append(new_snake)

    def snake_extend(self):
        self.add_snake(self.snakes[-1].pos())

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
          self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

        # 꼬리 부분 위치 뒤 20 만큼 계산
        # snakes.append 해서 새로운 snake 추가
    def snake_rest(self):
        for snake in self.snakes:
            snake.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

# todo 1. Create a snake  body
# todo 2. Move the snake
# todo 3. Create snake food
# todo 4. Detect collision with food
# todo 5. Create a scoreboard
# todo 6. Detect collision with wall
# todo 7. Detect collision with tail
# screen.exitonclick()