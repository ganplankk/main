import turtle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collect
from collect import CollectState

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
check_state = CollectState

MAX_LIFE = 50
collect_state = []
data = pd.read_csv("50_states.csv")
value = data.values.tolist()
all_state = data.state.to_list()
export_csv = []

while len(collect_state) != MAX_LIFE:
    answer_state = screen.textinput(title=f"{len(collect_state)}/{MAX_LIFE} Guess the State", prompt="What's another stat's name?").title()
    # missing_states = []
    # if answer_state == "Exit":
    #     for state in all_state:
    #         if state not in collect_state:
    #             missing_states.append(state)
    #             export_csv.append(state)
    #     df = pd.DataFrame(missing_states)
    #     df.to_csv('leaving_state.csv', index=False)
    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in collect_state]
        df = pd.DataFrame(missing_states)
        df.to_csv('leaving_State.csv')
        break
    for i in range(len(value)):
        if value[i][0] in answer_state:
            collect_state.append(answer_state)
            print(f"Your input{answer_state}")
            print(f"exit value{value[i][0]}")
            check_state(value[i][0], value[i][1], value[i][2])

# 사용자가 맞추지 못한 state 를 csv 출력


screen.exitonclick()

# state_data = data[data.state == answer_state]
# turtle.goto(int(state_data.x), int(state_data.y))

#1. Convert the guess to Title case
#2. Check if the guess if among the 50 states
#3. Write correct guesses onto the map
#4. Use a loop to allow the user to keep guessing
#5. Record the correct guesses in a list
#6. Keep track of the score

