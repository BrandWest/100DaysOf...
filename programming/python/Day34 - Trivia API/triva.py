from modules.question import Question
from modules.quiz_brain import QuizBrain
from modules.api_calls import ApiCalls
from modules.ui import QuizInterface

'''
    age: int <-- This will set an age as an int, but its empty. When assigned it needs to be put into a int.
    name: str
    height: float
    is_human: bool
    
    #Type Hints
        #Specify the data type age as int expected in the function (def polic_check(age: int))
        #Specify the return type: def polic_check(age: int) -> bool
    def polic_check(age: int) -> bool:
        if age > 18:
            can_drive= True
        else: 
            can_drive=False
        return can_drive

    if police(check(19):
        print("You may pass")
    else:
        print("Pay a fine")

'''
if __name__ == "__main__":

    question_bank = []

    api = ApiCalls()
    api.get_questions()

    for question in api.question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)