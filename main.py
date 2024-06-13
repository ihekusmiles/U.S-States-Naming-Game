import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Naming Game")
screen.setup(730, 500)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()  # all_states = []
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]  # Using List Comprehension
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break  # Breaks out of the while loop and exits game when "Exit" is entered.

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_state) # item() fetches the first element in a row, not used here.

        # print(f'state_data.x type: {type(state_data.x)}\nstate_data.y type: {type(state_data.y)}')  # Debugging