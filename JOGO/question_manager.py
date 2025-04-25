import random

class QuestionManager:
    def __init__(self, questions):
        self.questions = questions

    def get_random_question(self):
        question = random.choice(list(self.questions.keys()))
        answers = self.questions.pop(question)
        return question, answers