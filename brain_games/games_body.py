import prompt


def welcome_brain_games():
    print('Welcome to the Brain Games!')


def user_name():
    global name
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')


def welcome(rule):
    welcome_brain_games()
    user_name()
    rule()


def question(expression):
    print(f'Question: {expression}')


def user_answer():
    return prompt.string('Your answer: ')


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


def body(rule, expressions, results):
    welcome(rule)
    count = 0
    while count < 3:
        question(expressions[count])
        answer = user_answer()
        result = str(results[count])
        correct = is_correct(answer, result)
        if correct:
            count += 1
            continue
        else:
            lose()
            break
    else:
        win()
