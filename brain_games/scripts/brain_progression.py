from brain_games.games.progression_game import progression_rule, progression
from brain_games.body import welcome


def progression_main():
    welcome()
    progression_rule()
    progression()


if __name__ == '__main__':
    progression_main()
