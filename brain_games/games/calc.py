import random

GAME_RULES = "What is the result of the expression?"
MIN_NUM = 1
MAX_NUM = 100


def calculate(num1, num2, operation):
    match operation:
        case '+':
            return str(num1 + num2)
        case '-':
            return str(num1 - num2)
        case _:
            return None


def generate_round():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    operation = random.choice(['+', '-'])
    question = f"{num1} {operation} {num2}"
    correct_answer = calculate(num1, num2, operation)
    return question, correct_answer
