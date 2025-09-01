import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7385b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = "a"

def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    label1.config(text="Timer")
    label2.config(text="")
    canvas.itemconfig(text_timer, text="00:00")
    reps = 0
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        label1.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        label1.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        label1.config(text="Work", fg=GREEN)


def countdown(count):

    global label2
    count_min = (math.floor(count / 60))
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer=window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark =""
        for m in range(math.floor(reps / 2)):
            mark += "✔"
        label2.config(text=mark)

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label1 = Label(text="Title", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
label1.grid(row=0, column=1)

canvas = Canvas(width=600, height=600, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="pngwing.com.png")
canvas.create_image(280, 280, image=tomato_img)
text_timer=canvas.create_text(290,320, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



button1 = Button(text="Start", width=10, command=start_timer )
button1.grid(column=0, row=2)

button1 = Button(text="Exit", width=10, command=reset_timer)
button1.grid(column=3, row=2)


label2 = Label(bg=YELLOW, fg=RED, font=(FONT_NAME, 15, "bold"))
label2.grid(column=1, row=2)
window.mainloop()