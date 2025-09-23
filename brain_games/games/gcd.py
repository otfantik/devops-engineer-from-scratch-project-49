import random

GAME_RULES = "Find the greatest common divisor of given numbers."
MIN_NUM = 1
MAX_NUM = 100


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    question = f"{num1} {num2}"
    correct_answer = str(find_gcd(num1, num2))
    return question, correct_answer

