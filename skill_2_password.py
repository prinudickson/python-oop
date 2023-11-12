from random import choices
from string import ascii_letters, punctuation
from icecream import ic 
from copy import copy


class Password():
    """_summary_
    Creates a random password based on the user defined strength and length.
    The length is optional and can be set based on strength (low --> 8, Medium --> 12, high --> 16)
    If a length is user-specified these presets are over-ridden

    :param strength: A measure of password's effectiveness against brute force guessing
    :type strength: str, optional
    
    :param length:  The length of the password
    :param length: int, optional
    """
    # letters_lower_case = list(string.ascii_lowercase)
    # letters_upper_case = list(string.ascii_uppercase)
    # letters_all = list(string.ascii_letters)

    INPUT_UNIVERSE = {
        "numbers": list(range(10)),
        "letters": list(ascii_letters),
        "punctuations": list(punctuation) 
    }

    DEFAULT_LENGTHS = {
        "low": 8,
        "medium": 12,
        "high": 16
    }

    @classmethod
    def show_input_universe(cls):
        """_summary_
        Return the complete universe from the characters are sampled. 
        
        :return: The universe of chracters from the which the random sampling is done. 
        :rtype: dict (of lists)
        """
        return cls.INPUT_UNIVERSE

    def __init__(self, strength="medium", length=None) -> None:
        self.strength = strength
        self.length = length

        self._generate()

    def _generate(self):
        population = copy(self.INPUT_UNIVERSE["letters"])
        length = self.length or self.DEFAULT_LENGTHS.get(self.strength)

        if self.strength == "high":
            population += self.INPUT_UNIVERSE["numbers"] + self.INPUT_UNIVERSE["punctuations"]
        else:
            population += self.INPUT_UNIVERSE["numbers"]

        self.password = "".join(list(map(str, choices(population, k=length))))



if __name__ == "__main__":
    p_weak = Password(strength="low")
    ic(p_weak.password)

    p_medium = Password(strength="medium")
    ic(p_medium.password)

    p_high = Password(strength="high", length=30)
    ic(p_high.password)

    P_default = Password()
    ic(P_default.password)
