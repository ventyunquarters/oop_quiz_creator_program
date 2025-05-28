from loader import QuizLoader
from quizgame import QuizGame

def main():
    quiz_data = QuizLoader.load_quiz("quiz.txt")
    game = QuizGame(quiz_data)
    game.start()

if __name__ == "__main__":
    main()