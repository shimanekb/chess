"""
Acceptance tests for two player game of chess.
"""
import pytest
from chess.app.controller import game_controller


@pytest.fixture()
def feed_input(monkeypatch):
    def _feed_input(fed_input):
        monkeypatch.setattr('builtins.input', lambda x: fed_input)

    return _feed_input


def test_movement(capsys):
    game_controller.play_game()
    board = capsys.readouterr()
    print('LOOK\n')
    print(board)

    assert False


def test_movement_retry_bad_input_not_rank():
    assert False


def test_movement_retry_bad_input_not_file():
    assert False


def test_movement_retry_bad_input_no_space():
    assert False


def test_capture():
    assert False


@pytest.mark.timeout(1)
def test_quit(feed_input):
    feed_input('Q')
    game_controller.play_game()
