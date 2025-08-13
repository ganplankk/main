import turtle as t
from turtle import Screen
import random
import colorgram
from cmath import atanh

tim = t.Turtle()
# point = 3
# degree = 360
#
# for i in range(7):
#     turn = degree / point
#     # print(f"point value {point} , turn value : {turn}")
#     for j in range(point):
#         tim.right(turn)
#         tim.forward(50)
#     point += 1

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for j in range(num_sides):
#         tim.right(angle)
#         tim.forward(50)

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# turnaround = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(turnaround))

# tim.shape("circle")
# tim.position()
# tim.color("blue")
# astamp = tim.stamp()
# tim.circle(100)
# tim.position()

def draw_spirograph(size_if_gap):
    for _ in range(int(360 / size_if_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)
draw_spirograph(5)

## TODO 1. Random 모듈을 사용해서 방향과 거리 값을 랜덤하게 조정하여 선을 긋게한다.
## TODO 2. 선을 그으면서 선의 색깔은 colours 리스트를 랜덤하게 선택해서 변하도록 한다.

screen = t.Screen()
screen.exitonclick()


