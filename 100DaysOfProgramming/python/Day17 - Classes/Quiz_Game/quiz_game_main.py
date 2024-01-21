from data.data import question_data
from module.question_model import Question
from module.quiz_brain import Quiz

def assign_questions():
    question_bank = []

    for question in question_data:
        question_bank.append(Question(question['question'], question['correct_answer']))
    
    return question_bank


if __name__ == '__main__':
    question_bank = assign_questions()
    quiz = Quiz(question_bank)
    next_question = True
    while next_question:
        result = quiz.next_question()
        if quiz.still_has_questions() == True:
            print("\nYou've completed the quiz!")
            print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
            next_question = False
    
    

