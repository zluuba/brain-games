from brain_games.games.even_game import even_rule, is_even_game
from brain_games.body import welcome


def even_main():
    welcome()
    even_rule()
    is_even_game()


if __name__ == '__main__':
    even_main()
