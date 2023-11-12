import random
from icecream import ic 

class Student:
    education_platform = "Udemy"

    def __init__(self, name, age=30) -> None:
        self.name = name
        self.age = age

    def greet(self):
        intro = ["Hi I am {}. ", "My name is {}. ", "This is {}. "]
        greet = ["Nice to meet you", "Its wonderful to meet you", "How are you?"]

        choices = [0, 1, 2]
        intro_gen = random.choice(choices)
        greet_gen = random.choice(choices)

        construct_greeting = intro[intro_gen] + greet[greet_gen]
        return construct_greeting.format(self.name)


def class_create(student_names):
    return [Student(name) for name in student_names]


names = ["Aa", "Bb", "Cc", "Dd", "Ee"]

for student in class_create(names):
    ic(student.greet())