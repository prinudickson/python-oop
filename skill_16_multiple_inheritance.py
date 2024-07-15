from random import choices
import re
from icecream import ic

class VisaMixin:
    def generate(self):
        return [4,2] + super().generate()
    
class MasterCardMixin:
    def generate(self):
        return [5,3 ] + super().generate() 
    
class ValidMixin:
    def generate(self):
        number = super().generate()
        return number[:-1] + [self.calculate_checksum(number[:-1])]

    @staticmethod
    def calculate_checksum(numbers):
        cumulative_sum = 0

        for idx, num in enumerate(numbers[::-1]):
            if idx % 2 == 0: 
                if num * 2 > 9:
                    cumulative_sum += sum(map(int, str(num*2)))
                    #cumulative_sum += num * 2 - 9
                else:
                    cumulative_sum += num * 2    
            else:
                cumulative_sum += num 

        return 10 - cumulative_sum % 10

class CreditCard:
    DIGITS = list(range(9))

    def __init__(self) -> None:
        self._number = self.generate()

    def generate(self):
        return choices(self.DIGITS, k=14)
    
    @property
    def number(self):
        # 1234 5678 9012
        s = "".join(map(str, self._number))
        return " ".join(re.findall(".{4}", s))
    
class Visa(VisaMixin, CreditCard):
    pass

class ValidVisa(ValidMixin, VisaMixin, CreditCard):
    pass

class ValidMasterCard(ValidMixin, MasterCardMixin, CreditCard):
    pass

if __name__ == "__main__":
    random_visas = Visa()
    ic(random_visas.number)
    
    valid_visa = ValidVisa()
    ic(valid_visa.number)

    valid_mastercard = ValidMasterCard()
    ic(valid_mastercard.number)