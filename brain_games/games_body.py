import prompt


def show_welcome_brain_games():
    print('Welcome to the Brain Games!')


def show_game_rule(game_rule):
    print(game_rule)


def get_user_name():
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


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


# game engine. called by /scripts/, interacts with all other functions
def start_game(game):
    # unpacking game variables
    game_rule, expressions, results = game
    # shows greeting, takes username, shows game rule
    name = greet_user(game_rule)
    for count in range(3):
        # gets one expression and shows user
        show_question(expressions[count])
        answer = get_user_answer()
        # gets result that matches the expression
        result = str(results[count])
        # checks if the user's answer and result match
        correct = is_correct(answer, result)
        if not correct:
            show_user_lose(name)
            break
    else:
        show_user_win(name)
