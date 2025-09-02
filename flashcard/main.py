from tkinter import *
import  pandas, random
current_card= {}
learn = {}
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pandas.read_csv("to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("Untitled spreadsheet - Sheet1.csv")
    learn = data.to_dict(orient="records")
else:
    learn = data.to_dict("records")


def is_known():
    learn.remove(current_card)
    data = pandas.DataFrame(learn)
    data.to_csv("to_learn.csv", index =False)
    next_card()


def next_card():
    global current_card,timer
    window.after_cancel(timer)
    current_card = random.choice(learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    canvas.itemconfig(card_front_img, image = card_front)
    timer=window.after(3000, func=flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_title, text = "English", fill="white")
    canvas.itemconfig(card_word, text = current_card["English"], fill="white")
    canvas.itemconfig(card_front_img, image = card_back)

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer= window.after(3000, func = flip_card)

canvas =Canvas(width=800, height=526)
card_front= PhotoImage(file="purple.png")
card_front_img = canvas.create_image(400, 263, image=card_front)
card_back = PhotoImage(file="greem.png")
# card_back_img = canvas.create_image(400, 263, image=card_back)
canvas.config(bg=BACKGROUND_COLOR,  highlightthickness=0)
card_title = canvas.create_text(400, 150 ,text = "Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "Author", font=("Ariel", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

create_image = PhotoImage(file = "cross.png")
cross_button = Button(image = create_image )
cross_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
cross_button.grid(row =1, column=0)

new_img = PhotoImage(file = "tick.png")
tick_button = Button(image = new_img )
tick_button.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
tick_button.grid(row =1, column=1)

next_card()
window.mainloop()