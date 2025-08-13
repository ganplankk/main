from turtle import Screen, Turtle
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
tail_pos = snake.tail
score = 0

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

## game start
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ## 밥먹고 점수 올리기
    if snake.head.distance(food) < 15:
        print("nom nom")
        food.refresh()
        scoreboard.point()
        snake.snake_extend()
    ## 꼬리랑 부딪치다
    for tail in snake.snakes[1:]:
        if tail == snake.head:
            pass

        elif snake.head.distance(tail) < 10:
            scoreboard.reset()
            game_is_on = False
            scoreboard.game_over()

    if snake.head.distance(tail_pos) < 15:
        scoreboard.reset()
        game_is_on = False
        scoreboard.game_over()

    ## 벽 계산
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()