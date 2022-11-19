from brain_games.games.even_game import even
from brain_games.games_body import start_game


def is_even_game():
    start_game(even)


if __name__ == '__main__':
    is_even_game()
