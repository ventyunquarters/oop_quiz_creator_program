class Question:
    def __init__(self, question_text, correct_answer, choices):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.choices = choices

    def is_correct(self, answer):
        return answer.lower() == self.correct_answer.lower()