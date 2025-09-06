from tkinter import *
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizller")
        self.window.config(padx= 20, pady=20, bg=THEME_COLOR)
        self.written_score = Label(text="Score:0", font=("Arial", 16), fg="black", bg=THEME_COLOR, highlightthickness=0)
        self.written_score.grid(row=0, column=1)
        self.canvas = Canvas(self.window, height=300, width=300, bg=THEME_COLOR, highlightthickness=0)
        self.canvas.grid(row=2, column=0, columnspan=2, pady=20)
        self.tick = PhotoImage(file="tick.png")
        self.question_text = self.canvas.create_text(
            150, 125,
            text="",
            fill="black",  # Change color to something visible over the image
            font=("Arial", 20, "italic"),
            width=280  # optional: helps wrap long text inside canvas
        )

        self.tick_button = Button(self.window, image=self.tick, command=self.press_true)
        self.tick_button.config(bg=THEME_COLOR, highlightthickness=0)
        self.tick_button.grid(row=3, column=0)
        self.cross_img = PhotoImage(file="cross.png")
        self.cross_button = Button(self.window, image=self.cross_img, command=self.press_false)
        self.cross_button.config(bg=THEME_COLOR, highlightthickness=0)
        self.cross_button.grid(row=3, column=1)

        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_question():
            self.canvas.config(bg="white")
            self.written_score.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text="Sorry,You have reached the limit of the game")
            self.tick_button.config(state=DISABLED)
            self.cross_button.config(state=DISABLED)


    def press_true(self):
        self.answer = "TRUE"
        is_ok = self.quiz.check_answer(self.answer)
        self.feedback(is_ok)


    def press_false(self):
        self.answer = "FALSE"
        is_ok=self.quiz.check_answer(self.answer)
        self.feedback(is_ok)

    def feedback(self, is_ok):
        if is_ok:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)