import prompt

from brain_games.cli import welcome_user

ROUND_GAMES = 3


def run_game(game_module):
    name = welcome_user()
    print(game_module.GAME_RULES)
    for _ in range(ROUND_GAMES):
        question, correct_answer = game_module.generate_round()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
