from brain_games.games.calc_game import calc_game_rule, calculator
from brain_games.games.body import welcome_user, user_name


def main():
    welcome_user()
    user_name()
    calc_game_rule()
    calculator()


if __name__ == '__main__':
    main()
