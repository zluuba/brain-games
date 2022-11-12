from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')


def user_name():
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def question():
    global random_number
    random_number = randint(1, 1000)
    print(f'Question: {random_number}')
    global answer
    answer = prompt.string('Your answer: ')


def true_answer():
    opposite_answer = ''
    if random_number % 2 == 0:
        opposite_answer += 'yes'
    else:
        opposite_answer += 'no'
    return opposite_answer


def is_even_game():
    welcome_user()
    name = user_name()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        question()
        if answer == 'yes' and random_number % 2 == 0:
            print('Correct!')
            i += 1
        elif answer == 'no' and random_number % 2 != 0:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{true_answer()}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
