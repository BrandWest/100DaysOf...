import requests
import html

class ApiCalls():
    def __init__(self):    
        self.url = "https://opentdb.com/api.php"
        self.params = {"amount": 10, "type": "boolean"}
        self.question_data = []
        self.response = requests.get(self.url, params=self.params)
        self.category = ""
        self.difficulty = ""
        self.answer = ""
    
    def get_questions(self):
        data = self.response.json()
        if data["response_code"] == 0:
            for questions in data["results"]:
                question = questions["question"]
                answer = questions["correct_answer"]
                question, answer = self.format_question(question, answer)
                self.question_data.append({"question": question, "correct_answer": answer})
    
  
    def format_question(self, question, answer):
        return html.unescape(question), html.unescape(answer)
