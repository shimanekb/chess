"""
Acceptance tests for two player game of chess.
"""
import pytest
from chess.app import game_controller


@pytest.fixture()
def feed_input(monkeypatch):
    def _feed_input(fed_input):
        input_itr = iter(fed_input)
        monkeypatch.setattr('builtins.input', lambda x: next(input_itr))

    return _feed_input


@pytest.mark.timeout(3)
def test_movement(capsys, feed_input):
    # Given
    expected_first_board = \
        '  -------------------------------------------------\n'\
        '8 | BR  | BK  | BB  | BQ  | BKi | BB  | BK  | BR  |\n'\
        '  -------------------------------------------------\n'\
        '7 | BP  | BP  | BP  | BP  | BP  | BP  | BP  | BP  |\n'\
        '  -------------------------------------------------\n'\
        '6 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '5 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '4 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '3 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '2 | WP  | WP  | WP  | WP  | WP  | WP  | WP  | WP  |\n'\
        '  -------------------------------------------------\n'\
        '1 | WR  | WK  | WB  | WQ  | WKi | WB  | WK  | WR  |\n' \
        '  -------------------------------------------------\n'\
        '     a     b     c     d    e     f     g     h'
    expected_second_board = \
        '  -------------------------------------------------\n'\
        '8 | BR  | BK  | BB  | BQ  | BKi | BB  | BK  | BR  |\n'\
        '  -------------------------------------------------\n'\
        '7 | BP  | BP  | BP  | BP  | BP  | BP  | BP  | BP  |\n'\
        '  -------------------------------------------------\n'\
        '6 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '5 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '4 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '3 |     | WP  |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '2 | WP  |     | WP  | WP  | WP  | WP  | WP  | WP  |\n'\
        '  -------------------------------------------------\n'\
        '1 | WR  | WK  | WB  | WQ  | WKi | WB  | WK  | WR  |\n' \
        '  -------------------------------------------------\n' \
        '     a     b     c     d    e     f     g     h'

    feed_input(['b2 b3', 'q'])

    # When
    game_controller.play_game()

    # Then
    outerr = capsys.readouterr()

    actual_board = outerr.out
    assert expected_first_board in actual_board

    actual_board = outerr.out
    assert expected_second_board in actual_board


@pytest.mark.timeout(3)
def test_movement_retry_bad_input_not_rank(capsys, feed_input):
    # Given
    expected_error_prompt = 'Invalid position format needs to be ' \
                            '[a-e][1-8]: b9'

    feed_input(['b2 b9', 'Q'])

    # When
    game_controller.play_game()

    # Then
    outerr = capsys.readouterr()

    assert expected_error_prompt in outerr.out


@pytest.mark.timeout(3)
def test_movement_retry_bad_input_not_file(capsys, feed_input):
    # Given
    expected_error_prompt = 'Invalid position format needs to be ' \
                            '[a-e][1-8]: z2'

    feed_input(['z2 b3', 'Q'])

    # When
    game_controller.play_game()

    # Then
    outerr = capsys.readouterr()

    assert expected_error_prompt in outerr.out


@pytest.mark.timeout(3)
def test_movement_retry_bad_input_no_space(capsys, feed_input):
    # Given
    expected_error_prompt = 'Invalid move, needs two positions'

    feed_input(['z2b3', 'Q'])

    # When
    game_controller.play_game()

    # Then
    outerr = capsys.readouterr()

    assert expected_error_prompt in outerr.out


@pytest.mark.timeout(3)
def test_capture(capsys, feed_input):
    # Given
    expected_first_board = \
        '  -------------------------------------------------\n'\
        '8 | BR  | BK  | BB  | BQ  | BKi | BB  | BK  | BR  |\n'\
        '  -------------------------------------------------\n'\
        '7 | BP  | BP  | BP  | BP  | BP  | BP  | BP  | BP  |\n'\
        '  -------------------------------------------------\n'\
        '6 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '5 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '4 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '3 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '2 | WP  | WP  | WP  | WP  | WP  | WP  | WP  | WP  |\n'\
        '  -------------------------------------------------\n'\
        '1 | WR  | WK  | WB  | WQ  | WKi | WB  | WK  | WR  |\n' \
        '  -------------------------------------------------\n'\
        '     a     b     c     d    e     f     g     h'
    expected_second_board = \
        '  -------------------------------------------------\n'\
        '8 | BR  | BK  | BB  | BQ  | BKi | BB  | BK  | BR  |\n'\
        '  -------------------------------------------------\n'\
        '7 | BP  |     | BP  | BP  | BP  | BP  | BP  | BP  |\n'\
        '  -------------------------------------------------\n'\
        '6 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '5 |     | WP  |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '4 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '3 |     |     |     |     |     |     |     |     |\n'\
        '  -------------------------------------------------\n'\
        '2 |     | WP  | WP  | WP  | WP  | WP  | WP  | WP  |\n'\
        '  -------------------------------------------------\n'\
        '1 | WR  | WK  | WB  | WQ  | WKi | WB  | WK  | WR  |\n' \
        '  -------------------------------------------------\n'\
        '     a     b     c     d    e     f     g     h'

    feed_input(['a2 a3', 'b7 b6', 'a3 a4', 'b6 b5', 'a4 b5', 'q'])

    # When
    game_controller.play_game()

    # Then
    outerr = capsys.readouterr()

    assert expected_first_board in outerr.out
    assert expected_second_board in outerr.out


@pytest.mark.timeout(1)
def test_quit(feed_input):
    # Given
    feed_input(['Q'])

    # When
    game_controller.play_game()

    # Then Pytest checks and timeouts
