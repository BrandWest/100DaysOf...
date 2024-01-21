from tkinter import *
from modules.quiz_brain import QuizBrain


class QuizInterface:     #Variable  Type
    def __init__(self, quiz_brain: QuizBrain):
        self.window_theme_color = "#375362"
        self.question = ""
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=self.window_theme_color)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=self.window_theme_color)
        self.score_label.grid(column=1, row=0)
    
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text=self.question, 
            font=("Arial", 20, "italic"), 
            width=280) 
        self.get_next_questions()
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="/home/caboose/codingProjects/python/udemy/Day34 - Trivia API/images/true.png")
        self.correct_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)

        false_image = PhotoImage(file="/home/caboose/codingProjects/python/udemy/Day34 - Trivia API/images/false.png")
        self.incorrect_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.incorrect_button.grid(column=1, row=2)


        self.window.mainloop()


    def true_pressed(self):
        self.check_result(self.quiz.check_answer("True"))


    def false_pressed(self):
        self.check_result(self.quiz.check_answer("False"))


    def get_next_questions(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=self.question)
            self.get_score()
        else:
            self.canvas.itemconfig(self.question_text, text=f"No more questions. You scored {self.quiz.score}/{self.quiz.question_number}")
            self.correct_button.config(state="disabled")
            self.incorrect_button.config(state="disabled")


    def get_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")


    def check_result(self, answer):
        if answer == True:
            self.canvas.config(bg="#1BD634")
        else:
            self.canvas.config(bg="#D61F13")
        self.window.after(ms=1000, func=self.get_next_questions)