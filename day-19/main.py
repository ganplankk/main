from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
# tim.setpos(125,100)
all_turtle = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_position[turtle_index])
    print(new_turtle.color)
    all_turtle.append(new_turtle)


race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won, {winning_color} turtle got it")
            else:
                print(f"You've lost, {winning_color} turtle got it")
        x_forward = random.randint(0, 10)
        turtle.forward(x_forward)




# def move_forwards():
#     tim.forward(10)
# def move_backwards():ads
#     tim.backward(10)
# def head_left():
#     tim.left(10)
# def head_right():
#     tim.right(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=head_left)
# screen.onkey(key="d", fun=head_right)
# screen.onkey(key="c", fun=clear)

# TODO W=Forwards, S=Backwards, A=Counter-Clockwise, D=Clockwise, C=Clear drawing

screen.exitonclick()