from brain_games.games.even_game import even_game_rule, is_even_game
from brain_games.games.body import welcome_user, user_name


def main():
    welcome_user()
    user_name()
    even_game_rule()
    is_even_game()


if __name__ == '__main__':
    main()
