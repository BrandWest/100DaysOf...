class Quiz:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    

    def next_question(self):        
        current_question = self.question_list[self.question_number].text
        result = input(f"Q.{self.question_number+1}. {current_question} (True/False) ").title()
        self.check_answer(result)
        self.question_number += 1
    

    def check_answer(self, result):
        if result == self.question_list[self.question_number].answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
        print(f"The correct answer was: {self.question_list[self.question_number].answer}.")
        print(f"Your current score is {self.score}/{self.question_number+1}.\n")


        
    def still_has_questions(self):
        return self.question_number == len(self.question_list)