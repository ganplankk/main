import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_over=1
data = pandas.read("50_states.csv")
while game_over != 50:
    answer_state = screen.textinput(title=f"{game_over}/50 Guess the State", prompt="What's another stat's name?")
    game_over+=1

    print(answer_state)

#1. Convert the guess to Title case
#2. Check if the guess if among the 50 states
#3. Write correct guesses onto the map
#4. Use a loop to allow the user to keep guessing
#5. Record the correct guesses in a list
#6. Keep track of the score