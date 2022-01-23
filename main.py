import turtle
import pandas
from scoreboard import Scoreboard
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = Scoreboard()
all_states = pandas.read_csv("50_states.csv")
states_list = all_states["state"].to_list()


def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)


states_guessed = []
game = True
while len(states_guessed) < 50 and game:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()
    print(f"You typed in {answer_state}")
    for state in states_list:
        if answer_state == "Exit":
            game = False
        if answer_state == state:
            states_guessed.append(answer_state)
            scoreboard.increase_score()

            state_info = all_states[all_states.state == answer_state]

            new_state = turtle.Turtle()
            new_state.hideturtle()
            new_state.color("black")
            new_state.pu()
            new_state.goto(int(state_info.x), int(state_info.y))
            new_state.write(f"{state}", align="center", font=("Arial", 8, "normal"))
            print(states_guessed)
if len(states_guessed) == 50:
    scoreboard.game_over()
states_to_learn = []
for state in states_list:
    if state in states_guessed:
        pass
    else:
        states_to_learn.append(state)
learn = pandas.DataFrame(states_to_learn)
learn.to_csv("to_learn.csv")
turtle.mainloop()