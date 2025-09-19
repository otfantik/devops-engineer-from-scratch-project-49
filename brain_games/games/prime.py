import random
GAME_RULES ='Answer "yes" if given number is prime. Otherwise answer "no".'
def is_prime(number):
	if number < 2 or number == 2 or number % 2 == 0:
		return False
	for divisor in range (3, int(number ** 0.5) +1):
		if number % divisor == 0:
			return False
	return True
def generate_round():
	number = random.randint(1, 100)
	correct_answer = "yes" if is_prime(number) else "no"
	return number, correct_answer
