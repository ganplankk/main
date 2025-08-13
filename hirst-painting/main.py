# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
# my_colors = []
# my_color = ()
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     my_color = (r, g, b)
#     my_colors.append(my_color)
import turtle as t
import random
color_list = [(232, 233, 238), (238, 242, 239), (15, 20, 39), (162, 62, 41), (198, 161, 108), (140, 162, 192), (230, 204, 99), (45, 14, 10), (34, 13, 21), (159, 55, 71), (72, 95, 125), (19, 43, 30), (171, 153, 43), (186, 139, 152), (139, 35, 25), (71, 114, 88), (159, 172, 159), (202, 72, 87), (46, 51, 97), (196, 92, 77), (127, 37, 57), (218, 176, 182), (77, 81, 28), (41, 81, 43), (225, 175, 171), (88, 112, 176), (176, 189, 213), (44, 73, 75)]

# 가로,세로 거리 10
# 점 크기 약 20 점들 간 간격 약 50걸음
dot = t.Turtle()
t.colormode(255)

up = 0
dot.up()

dot.speed("fastest")
dot.setheading(225)
dot.forward(250)
dot.setheading(0)
dot.hideturtle()

current_position = dot.position()

def dot_move_to_up(f_current_position):
    dot.setposition(f_current_position)
    dot.setheading(90)
    dot.forward(50)
    dot.setheading(0)
    return dot.position()

for _ in range(10):
    for _ in range(10):
        color = random.choice(color_list)
        dot.dot(20, random.choice(color_list));dot.fd(50)
    up += 50
    current_position = dot_move_to_up(current_position)

screen = t.Screen()
screen.exitonclick()