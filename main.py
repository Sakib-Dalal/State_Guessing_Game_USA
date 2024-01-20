import turtle
import pandas

image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title("Guess State Name")
screen.addshape(image)
turtle.Turtle(image)

# get x and y on click on screen
# def get_mouse_click_coor(x, y):
#     print(f"x:{x}, y:{y}")
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv('50_states.csv')
all_states = data['state'].to_list()
guess_states = []
lost_state = []


while len(guess_states) < 50:
    user_inputted_state = (turtle.textinput(f"Guess State {len(guess_states)}/50", "Enter State Name: ")).title()

    if user_inputted_state == "Exit":
        for state in all_states:
            if state not in guess_states:
                lost_state.append(state)
        new_data = pandas.DataFrame(lost_state)
        new_data.to_csv('learn.csv')
        break
    if user_inputted_state in all_states:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        state_data = data[data['state'] == user_inputted_state]
        pen.goto(int(state_data.x), int(state_data.y))
        pen.write(state_data.state.item())
        guess_states.append(state_data.state.item())

