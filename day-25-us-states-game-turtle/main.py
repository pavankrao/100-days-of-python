import turtle
import pandas

IMAGE = "blank_states_img.gif"
USER_SCORE = 0
NUM_OF_US_STATES = 50
USER_GUESSED_STATES = []

# game screen initialization
screen = turtle.Screen()
screen.title("U.S. States Game")

# add image as shape to screen
screen.addshape(IMAGE) # to add a new shape
turtle.shape(IMAGE) # make turtle the image itself

# all states list
data = pandas.read_csv("50_states.csv")
ALL_US_STATES = data.state.to_list()

#################################
#### find coordinates in a image
#################################
# def get_mouse_click_coor(x, y):
#     print(x, y)
# print(turtle.pos())
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

while len(USER_GUESSED_STATES) < 50:
    USER_SCORE = len(USER_GUESSED_STATES)

    # score in title
    title = f"{USER_SCORE}/50 States Correct"
    if USER_SCORE == 0:
        title = "Guess the State"

    # user guess
    try:
        user_guess = screen.textinput(title=title, prompt="What is another state's name?").title() # title case
    except AttributeError:
        break

    # if exit, save missing states to learn
    if user_guess == "Exit":
        missing_states = [state for state in ALL_US_STATES if state not in USER_GUESSED_STATES]
        missing_states_data = pandas.DataFrame(data=missing_states)
        missing_states_data.index += 1 # start index at 1
        missing_states_data.to_csv("states_to_learn.csv", header=False) # header=False removes the 0,
        break

    # if correct, print state name on map
    if user_guess in ALL_US_STATES and user_guess not in USER_GUESSED_STATES: # Bug fixed same state printed again - yay!
        t = turtle.Turtle()
        t.hideturtle()
        USER_GUESSED_STATES.append(user_guess)
        # find coordinates
        state_row_data = data[data.state == user_guess] # specific row selection
        t.penup()
        t.goto(state_row_data.x.item(), state_row_data.y.item())
        t.color("red")
        t.write(user_guess, align='center')

#screen.exitonclick()