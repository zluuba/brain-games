from brain_games.games.calc_game import calc_rule, calculator
from brain_games.body import welcome


def calc_main():
    welcome()
    calc_rule()
    calculator()


if __name__ == '__main__':
    calc_main()
