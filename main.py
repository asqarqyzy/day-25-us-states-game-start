import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_num = 0
states_data = pd.read_csv("50_states.csv")
states = states_data["state"].to_list()

guessed_states = set()

while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 guessed states", "What's next state's name?").title()
    if answer == "Exit":
        states_to_learn = [state for state in states if state not in guessed_states]
        df_states_to_learn = pd.DataFrame(states_to_learn, columns=["State"])
        df_states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer in states:
        guessed_states.add(answer)
        state_row = states_data[states_data.state == answer]
        write_state = turtle.Turtle()
        write_state.hideturtle()
        write_state.penup()
        write_state.goto(state_row.x.item(), state_row.y.item())
        write_state.write(answer, align="center")

