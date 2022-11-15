from brain_games.games.calc_game import game_rule, calculator
from brain_games.games.body import welcome_user, user_name


def calc():
    game_rule()
    calculator()


def main():
    welcome_user()
    user_name()
    calc()


if __name__ == '__main__':
    main()
