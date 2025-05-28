import time
import random
from colorama import Fore, Style, init
from loader import QuizLoader
from highscore import HighScoreManager

# Initialize colorama
init(autoreset=True)

class QuizGame:
    bonus_time_limit = 15  # Add a timer to give bonuses for early answers
    bonus_points = 2       # Bonus points for fast answers
    normal_points = 1      # Default points for correct answers
    max_wrong = 3          # Stop the game when there's three incorrect answers

    def __init__(self, questions):
        self.questions = questions
        self.total_score = 0
        self.wrong_count = 0
        self.high_score_manager = HighScoreManager()

    # Ask one question and return the score earned and correctness
    def ask_question(self):
        question = random.choice(self.questions)
        choices = question.choices[:]
        random.shuffle(choices)

        # Display the question and all the choices numbered and colored
        print(Fore.CYAN + "\nQuestion: " + Style.BRIGHT + question.question_text)
        choice_labels = ['A', 'B', 'C', 'D']
        label_to_choice = {label: choice for label, choice in zip(choice_labels, choices)}

        for label, choice in label_to_choice.items():
            print(Fore.YELLOW + f"  {label}. {choice}")

        # Start the timer when the user sees the question
        start_time = time.time()
        try:
            # Get the user's answer
            user_input = input(Fore.WHITE + "Enter the letter of your answer: ").strip().upper()
            end_time = time.time()
        except ValueError:
            # If input is invalid (e.g., letters), count it as wrong
            print(Fore.RED + " Invalid input. Counting as incorrect.")
            return 0, False

        # Check if the input is a valid choice
        if user_input not in label_to_choice:
            print(Fore.RED + "Choice is invalid.")
            return 0, False

        # Track the letter input to the actual answer
        user_answer = label_to_choice[user_input]
        time_taken = end_time - start_time

        print(f"You answered in {time_taken:.2f} seconds.")

        # Check if the answer is correct and assign the score
        if question.is_correct(user_answer):
            if time_taken <= self.bonus_time_limit:
                print(Fore.GREEN + "Correct! Bonus points for speed!")
                return self.normal_points + self.bonus_points, True
            else:
                print(Fore.GREEN + "Correct!")
                return self.normal_points, True
        else:
            print(Fore.RED + f"Incorrect. The correct answer was: {question.correct_answer}")
            return 0, False

    # Run the quiz on the loop
    def start(self):
        # Welcome messages
        print(Fore.CYAN + Style.BRIGHT + "Welcome to the Quiz!")
        print("Pick the correct letter of the answer to earn points.")
        print(Fore.LIGHTBLACK_EX + "Answer within 15 seconds for bonus points.")
        print(Fore.RED + "Game ends after 3 incorrect answers.\n")

        # Will keep asking questions until the user gets 3 wrong
        while self.wrong_count < self.max_wrong:
            points, correct = self.ask_question()
            self.total_score += points

            # Track incorrect answers
            if not correct:
                self.wrong_count += 1
                print(Fore.RED + f"Wrong Answers: {self.wrong_count}/{self.max_wrong}")

            # Show updated score
            print(Fore.GREEN + f"Current Score: {self.total_score} point(s)\n")

        # Game over message
        print(Fore.RED + "\nGame Over! You reached 3 incorrect answers.")
        print(Fore.YELLOW + f"Final Score: {self.total_score} point(s)")

        # Save score if it's a high score
        self.high_score_manager.save_score(self.total_score)

# Load and start the quiz
if __name__ == "__main__":
    quiz_data = QuizLoader.load_quiz("quiz.txt")
    game = QuizGame(quiz_data)
    game.start()
