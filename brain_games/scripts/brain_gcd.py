from brain_games.games.gcd_game import game_rule, greatest_cd
from brain_games.games.body import welcome_user, user_name


def gcd():
    game_rule()
    greatest_cd()


def main():
    welcome_user()
    user_name()
    gcd()


if __name__ == '__main__':
    main()
