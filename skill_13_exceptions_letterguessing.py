import time
from collections import defaultdict
from string import ascii_lowercase
from random import choice
from icecream import ic

class LetterGuessingException(Exception):
    """
    The exception base class for the letter guessing app
    """

class LetterComesAfter(LetterGuessingException):
    pass

class LetterComesBefore(LetterGuessingException):
    pass

class NotLetter(LetterGuessingException):
    pass

class LetterGuessingGame:
    def __init__(self) -> None:
        self.start_time = time.time()
        self.performance = defaultdict(list)
        self._correct_guess = False

    def _display_performance(self):
        time_taken = time.time() - self.start_time
        return f"{'That was correct!' if self._correct_guess else 'Game interupted!'}" \
            f"You played for {round(time_taken,2)} seconds, and made "\
            f"{len(self.performance['before'])} before guesses and "\
            f"{len(self.performance['after'])} after guesses"
    
    @staticmethod
    def _pick_letter():
        ic("The computer has chosen a letter from the English Alphabet.. what do you think it was?!")
        return choice(list(ascii_lowercase))
    
    @staticmethod
    def _validate_user_input(computer_choice, user_guess):
        if user_guess not in ascii_lowercase:
            raise NotLetter
        elif user_guess < computer_choice:
            raise LetterComesAfter
        elif user_guess > computer_choice:
            raise LetterComesBefore


    def play(self):
        computer_choice = self._pick_letter()
        user_guess = None
        
        while True:
            try:
                user_guess = input().strip().lower()
                self._validate_user_input(computer_choice=computer_choice, user_guess=user_guess)
                
                #Correct Answer
                self._correct_guess = True
                ic("correct!")
                break
            except LetterComesAfter:
                ic("Nope, it was something after, guess again")
                self.performance["before"].append(user_guess)
            except LetterComesBefore:
                ic("Nope, it was something before, guess again")
                self.performance["after"].append(user_guess)
            except NotLetter:
                ic("Only English Alphabet letters are supported")
            except KeyboardInterrupt:
                ic(self._display_performance())

        ic(self._display_performance())


if __name__ == "__main__":
    game = LetterGuessingGame()
    game.play()