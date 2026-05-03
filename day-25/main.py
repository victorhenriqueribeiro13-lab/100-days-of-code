import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
states = pd.read_csv("50_states.csv")
states_list = states["state"].to_list()

correct_guesses = 0
correct_guesses_text = []
title = "Guess the State"
while len(correct_guesses_text) < 50:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        correct_guesses += 1
        title = f"{correct_guesses}/50 States Correct"
        correct_guesses_text.append(answer_state)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        current_x_coordinate = states[states['state'] == answer_state]
        current_x_coordinate = current_x_coordinate["x"].to_list()
        current_y_coordinate = states[states['state'] == answer_state]
        current_y_coordinate = current_y_coordinate["y"].to_list()
        actual_coordinate = current_x_coordinate, current_y_coordinate

        coordinates_x_and_y = [element for innerList in actual_coordinate for element in innerList]
        coordinates_right = list(map(int, coordinates_x_and_y))
        x_coordinate = coordinates_right[0]
        y_coordinate = coordinates_right[1]
        text.setpos(x_coordinate, y_coordinate)
        text.write(f"{answer_state}", align="center", font=("Arial", 8, "normal"))
    if correct_guesses == 50:
        break

#print only the states that the user didn't guess right as a .csv
states_to_learn = []
for state in states_list:
    if state not in correct_guesses_text:
        states_to_learn.append(state)
states_to_learn_dict = {
    "States": [state for state in states_to_learn],
}
final_list = pd.DataFrame(states_to_learn_dict)
final_list.to_csv("states_to_learn.csv")













