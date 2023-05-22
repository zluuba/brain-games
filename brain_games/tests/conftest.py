from random import seed
import pytest
import os


def get_fixture_path(name):
    return os.path.join('brain_games/tests/fixtures/', name)


@pytest.fixture
def set_seed():
    seed(1)


@pytest.fixture
def input_win():
    return ['Mark', '24', '5', '10']


@pytest.fixture
def output_win():
    output1 = get_fixture_path("output_1.txt")
    with open(output1) as file:
        expected_output = file.read()
    return expected_output


@pytest.fixture
def input_loss():
    return ['Mark', '44']


@pytest.fixture
def output_loss():
    output1 = get_fixture_path("output_2.txt")
    with open(output1) as file:
        expected_output = file.read()
    return expected_output
