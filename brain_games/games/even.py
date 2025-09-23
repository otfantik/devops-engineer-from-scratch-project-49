import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(MIN_NUM, MAX_NUM)  # noces B311
    correct_answer = "yes" if is_even(number) else "no"
    question = str(number)
    return question, correct_answer
