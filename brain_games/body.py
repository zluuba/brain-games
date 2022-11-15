import prompt


def welcome():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')


def is_correct(answer, result):
    if answer == result:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False


def win():
    print(f'Congratulations, {name}!')


def lose():
    print(f"Let's try again, {name}!")
