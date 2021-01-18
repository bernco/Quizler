from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.t_score = 0
        # --------------- window ----------------
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20)

        # ------------- label -----------------------
        self.score_label = Label(text=f"Score: {self.t_score}", bg=THEME_COLOR, fg="white")
        self.score_label.config(pady=20)
        self.score_label.grid(row=0, column=1)

        # ----------- canvas -------------------
        self.canvas = Canvas(bg="white", width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.canvas_text = self.canvas.create_text(
            150, 125,
            text="",
            width=280,
            font=FONT, fill=THEME_COLOR
        )

        # ------------ button ------------------
        self.good_button = Button(highlightthickness=0, command=self.true_clicked)
        g_button_img = PhotoImage(file="images/true.png")
        self.good_button.configure(bg=THEME_COLOR, image=g_button_img)
        self.good_button.grid(row=2, column=0, pady=20)

        self.bad_button = Button(highlightthickness=0, command=self.false_clicked)
        b_button_img = PhotoImage(file="images/false.png")
        self.bad_button.configure(bg=THEME_COLOR, image=b_button_img)
        self.bad_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        quiz_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=quiz_text)

    def false_clicked(self):
        user_answer = "False"
        if user_answer == self.quiz.current_question.answer:
            self.canvas.configure(bg="green")
            if self.quiz.still_has_questions():
                self.t_score += 1
                self.score_label.config(text=f"Score: {self.t_score}")
                self.window.after(1000, self.get_next_question)
            else:
                self.canvas.itemconfig(self.canvas_text, text="That is the end of the question")
                self.bad_button.config(state="disable")
                self.good_button.config(state="disable")
                self.canvas.configure(bg="white")

        else:
            self.canvas.configure(bg="red")
            if self.quiz.still_has_questions():
                self.window.after(1000, self.get_next_question)
            else:
                self.canvas.itemconfig(self.canvas_text, text="That is the end of the question")
                self.bad_button.config(state="disable")
                self.good_button.config(state="disable")
                self.canvas.configure(bg="white")

    def true_clicked(self):
        user_answer = "True"
        if user_answer == self.quiz.current_question.answer:
            self.canvas.configure(bg="green")
            if self.quiz.still_has_questions():
                self.t_score += 1
                self.score_label.config(text=f"Score: {self.t_score}")
                self.window.after(1000, self.get_next_question)
            else:
                self.canvas.itemconfig(self.canvas_text, text="That is the end of the question")
                self.good_button.config(state="disable")
                self.bad_button.config(state="disable")
                self.canvas.configure(bg="white")
        else:
            self.canvas.configure(bg="red")
            if self.quiz.still_has_questions():
                self.window.after(1000, self.get_next_question)
            else:
                self.canvas.itemconfig(self.canvas_text, text="That is the end of the question")
                self.good_button.config(state="disable")
                self.bad_button.config(state="disable")
                self.canvas.configure(bg="white")

