from brain_games.games.calc_game import calc_rule, calculator
from brain_games.games.body import welcome_user, user_name


def main():
    welcome_user()
    user_name()
    calc_rule()
    calculator()


if __name__ == '__main__':
    main()
