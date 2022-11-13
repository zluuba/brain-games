import random
from random import randint
import prompt


def welcome():
	print('Welcome to the Brain Games!')


def user_name():
	name = prompt.string("May I have your name? ")
	print(f'Hello, {name}!')
	return name


def calc_question():
	operators = ['+', '-', '*']
	num1 = randint(1, 50)
	num2 = randint(1, 50)
	operator = random.choice(operators)
	print(num1, operator, num2)
	global answer
	answer = prompt.string('Your answer: ')

	if operator == "+":
		result = num1 + num2
	elif operator == "-":
		result = num1 - num2
	else:
		result = num1 * num2
	return result


def calculator():
	name = user_name()
	print('What is the result of the expression?')
	i = 0
	while i < 3:
		result = str(calc_question())
		if answer == result:
			print('Correct!')
			i += 1
		else:
			print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
			print(f"Let's try again, {name}!")
			break
	else:
		print(f'Congratulations, {name}!')
