import random
GAME_RULES = "What is the result of the expression?"
def calculate(num1, num2, operation):
    match operation:
        case '+':
            return str(num1 + num2)
        case '-':
            return str(num1 - num2)
        case _:
            return None
def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operation = random.choice(['+', '-'])
    question = f"{num1} {operation} {num2}"
    correct_answer = calculate(num1, num2, operation)
    return question, correct_answer
