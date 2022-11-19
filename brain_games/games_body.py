import prompt


def show_welcome_brain_games():
    print('Welcome to the Brain Games!')


def get_user_name():
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def show_game_rule(game_rule):
    if game_rule == 'even_game':
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game_rule == 'calculator_game':
        print('What is the result of the expression?')
    elif game_rule == 'gcd_game':
        print('Find the greatest common divisor of given numbers.')
    elif game_rule == 'progression_game':
        print('What number is missing in the progression?')
    elif game_rule == 'prime_game':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')


def greet_user(game_rule):
    show_welcome_brain_games()
    name = get_user_name()
    show_game_rule(game_rule)
    return name


def show_question(expression):
    print(f'Question: {expression}')


def get_user_answer():
    return prompt.string('Your answer: ')


def is_correct(answer, result):
    if answer == result:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.")
        return False


def show_user_win(name):
    print(f'Congratulations, {name}!')


def show_user_lose(name):
    print(f"Let's try again, {name}!")


def start_game(game_rule, expressions, results):
    name = greet_user(game_rule)
    for count in range(3):
        show_question(expressions[count])
        answer = get_user_answer()
        result = str(results[count])
        correct = is_correct(answer, result)
        if correct:
            continue
        else:
            show_user_lose(name)
            break
    else:
        show_user_win(name)
