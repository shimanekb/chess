"""
Unit tests for board_view
"""
from chess.set.table import Board
from chess.app import board_view


def test_display_printed_board(capsys):
    # Given
    expected_board_display = \
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
    board = Board()

    # When
    board_view.display(board)

    # Then
    outerr = capsys.readouterr()

    assert expected_board_display in outerr.out
