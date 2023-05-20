from brain_games.games import calc
from brain_games.engine import start_game

from random import seed

seed(1)

# TODO: - add more user_inputs
#       - add more outputs
#       - add conftest.py and fixtures


OUTPUT1 = """Welcome to the Brain Games!
Hello, Mark!
What is the result of the expression?
Question: 5 + 19
Correct!
Question: 9 - 4
Correct!
Question: 25 - 15
Correct!
Congratulations, Mark!
"""


def user_inputs():
    strings = ['Mark', '24', '5', '10']
    for elem in strings:
        yield elem


def test_engine(monkeypatch, capsys):
    with monkeypatch.context() as m:
        answers = user_inputs()
        m.setattr('builtins.input', lambda _: next(answers))
        assert not start_game(calc)

        captured = capsys.readouterr()
        assert captured.out == OUTPUT1
