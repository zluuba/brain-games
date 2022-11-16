from brain_games.games.prime_game import prime_rule, prime_game
from brain_games.body import welcome


def prime_main():
    welcome()
    prime_rule()
    prime_game()


if __name__ == '__main__':
    prime_main()
