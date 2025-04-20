import turtle
import pandas as pd
from state_label import StateLabel

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []
state_label = StateLabel()


while True:
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(data)} guessed", prompt="What's another state name?")
    answer.title()
    if answer in data.state.to_list() and answer not in guessed_states:
        lat = data[data.state == answer].y.item()
        lon = data[data.state == answer].x.item()
        state_label.label_state(answer, lon, lat)
        guessed_states.append(answer)
    if len(guessed_states) >= 50:
        break
    if answer.lower() == "exit":
        break

missed_states = [state for state in all_states if state not in guessed_states]
new_data = pd.DataFrame(missed_states)
new_data.to_csv("states_to_learn.csv")
