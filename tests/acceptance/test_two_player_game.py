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


@pytest.mark.timeout(1)
def test_movement(capsys, feed_input):
    # Given
    expected_first_board = '  ---------------------------------------------\n'\
                           '8 | BR  | BK  | BB  | BQ  | BKi| BB | BK | BR |\n'\
                           '  ---------------------------------------------\n'\
                           '7 | BP  | BP  | BP  | BP  | BP | BP | BP | BP |\n'\
                           '  ---------------------------------------------\n'\
                           '6 |     |     |     |     |    |    |    |    |\n'\
                           '  ---------------------------------------------\n'\
                           '5 |     |     |     |     |    |    |    |    |\n'\
                           '  ---------------------------------------------\n'\
                           '4 |     |     |     |     |    |    |    |    |\n'\
                           '  ---------------------------------------------\n'\
                           '3 |     |     |     |     |    |    |    |    |\n'\
                           '  ---------------------------------------------\n'\
                           '2 | WP  | WP  | WP  | WP  | WP | WP | WP | WP |\n'\
                           '  ---------------------------------------------\n'\
                           '1 | WR  | WK  | WB  | WQ  | WKi| WB | WK | WR |\n'\
                           '  ---------------------------------------------\n'\
                           '     a     b     c     d    e     f    g    h'
    expected_second_board = \
        '  ---------------------------------------------\n'\
        '8 | BR  | BK  | BB  | BQ  | BKi| BB | BK | BR |\n'\
        '  ---------------------------------------------\n'\
        '7 | BP  | BP  | BP  | BP  | BP | BP | BP | BP |\n'\
        '  ---------------------------------------------\n'\
        '6 |     |     |     |     |    |    |    |    |\n'\
        '  ---------------------------------------------\n'\
        '5 |     |     |     |     |    |    |    |    |\n'\
        '  ---------------------------------------------\n'\
        '4 |     |     |     |     |    |    |    |    |\n'\
        '  ---------------------------------------------\n'\
        '3 |     | WP  |     |     |    |    |    |    |\n'\
        '  ---------------------------------------------\n'\
        '2 | WP  |     | WP  | WP  | WP | WP | WP | WP |\n'\
        '  ---------------------------------------------\n'\
        '1 | WR  | WK  | WB  | WQ  | WKi| WB | WK | WR |\n'\
        '  ---------------------------------------------\n'\
        '     a     b     c     d    e     f    g    h'
    feed_input('b2 b3')
    feed_input('Q')

    # When
    game_controller.play_game()

    # Then
    board = capsys.readouterr()

    assert expected_first_board in board.out
    assert expected_second_board in board.out


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
    # Given
    feed_input('Q')

    # When
    game_controller.play_game()

    # Then Pytest checks and timeouts
