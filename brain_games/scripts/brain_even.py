import random
from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def run_even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_even(number) else "no"
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")


def main():
    run_even_game()


if __name__ == '__main__':
    main()
