import  turtle
import pandas
screen = turtle.Screen()
screen.title("U.S> States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_on = True
guessed_states = 0
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
Guessed_values=[]
while guessed_states<50 and game_on:
    answer_state= screen.textinput(f"{guessed_states}/50 States guessed correct", "What's your guess?").title()
    if answer_state in states:
        guessed_states = guessed_states + 1
        state_cordinates = data[data["state"]==answer_state]
        x_pos = int(state_cordinates["x"])
        y_pos = int(state_cordinates["y"])
        marker = turtle.Turtle()
        marker.hideturtle()
        marker.penup()
        marker.goto(x_pos, y_pos)
        marker.pendown()
        marker.color("black")
        marker.write(f"{answer_state}", align="center", font=("Arial", 12, "normal"))
        Guessed_values.append(answer_state)

    elif answer_state == "Exit":
        game_on = False

learn_state=[]

for item in states:
    if item not in Guessed_values:
        learn_state.append(item)

df = pandas.DataFrame(learn_state)
df.to_csv("need_to_learn.csv")
print("done")