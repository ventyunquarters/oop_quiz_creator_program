import os
from colorama import Fore

# Save the high score to a file if it's a new high
class HighScoreManager:
    def __init__(self, filename="highscore.txt"):
        self.filename = filename

    def save_score(self, score):
        high_score = 0

        # Check if a high score file already exists. Reads file
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    high_score = int(file.read().strip())
                except ValueError:
                    high_score = 0

        # Compare the current score to the saved high score
        if score > high_score:
            with open(self.filename, 'w') as file:
                file.write(str(score))
            print(Fore.MAGENTA + "🎉 New High Score!")
        else:
            print(Fore.BLUE + f"High Score to Beat: {high_score}")