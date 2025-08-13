from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("Orange")
screen.setup(width=800, height=600)
screen.title("Welcome to the PoNG Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()


screen.exitonclick()


## Create the screen
## Create and move a paddle
# width = 20, height = 100, x_pos = 350, y_pos = 0
## Create another paddle
## Create the ball and make it move
## Detect collision with wall and bounce
## Detect collision with paddle
## Detect when paddle misses
## Keep score