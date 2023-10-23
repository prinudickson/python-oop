import random 
import string
from icecream import ic 



# ic(letters_lower_case)
# ic(letters_upper_case)
# ic(letters_all)

class Password():
    letters_lower_case = list(string.ascii_lowercase)
    letters_upper_case = list(string.ascii_uppercase)
    letters_all = list(string.ascii_letters)

    def __init__(self, strength, length=4) -> None:
        self.strength = strength
        self.length = length
        pass

