from question import Question

# Define the quiz function to load it. It will come from a file with multiple choice questions
class QuizLoader:

    def load_quiz(filename):
        with open(filename, 'r') as file:
            raw_entries = file.read().strip().split('\n\n')
        quiz_data = []

        for entry in raw_entries:
            lines = entry.strip().split('\n')
            question = lines[0][3:]  # Remove Q: prefix
            answer = lines[1][3:]    # Remove A: prefix
            choices = lines[2][3:].split(';')  # Remove C: prefix
            quiz_data.append(Question(question, answer, choices))

        return quiz_data