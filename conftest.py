import pytest


@pytest.fixture()
def correct_word():
    return "шифоньер"


@pytest.fixture()
def incorrect_words():
    return "малако"
