# import another_module
# print(another_module.another_variable)
#
# #import turtle
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.right(100)
# # my_screen 이라는 object 를 Screen() 함수를 담아 생성
# my_screen = Screen()
# # my_screen 이라는 object의 canvheight 이라는 특성을 출력
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
table.align="c"
print(table)
