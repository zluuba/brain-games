from brain_games.games import calc
from brain_games.engine import start_game


def get_user_inputs(inputs):
    for elem in inputs:
        yield elem


def test_engine_win(monkeypatch, capsys, set_seed, input_win, output_win):
    with monkeypatch.context() as m:
        answers = get_user_inputs(input_win)
        m.setattr('builtins.input', lambda _: next(answers))
        assert not start_game(calc)

        captured = capsys.readouterr()
        assert captured.out == output_win


def test_engine_loss(monkeypatch, capsys, set_seed, input_loss, output_loss):
    with monkeypatch.context() as m:
        answers = get_user_inputs(input_loss)
        m.setattr('builtins.input', lambda _: next(answers))
        assert not start_game(calc)

        captured = capsys.readouterr()
        assert captured.out == output_loss
