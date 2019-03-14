"""
Tests for chess.board.board.Board
"""
from chess.board.board import Board
from chess.board.board import Position


def test_init_default_white_board_setup():
    # When
    board = Board()

    # Then
    pos = Position('a1')
    white_rook_left = board.get_piece(pos)
    assert white_rook_left.symbol == 'WR'

    pos = Position('b1')
    white_knight_left = board.get_piece(pos)
    assert white_knight_left.symbol == 'WK'

    pos = Position('c1')
    white_bishop_left = board.get_piece(pos)
    assert white_bishop_left.symbol == 'WB'

    pos = Position('d1')
    white_queen = board.get_piece(pos)
    assert white_queen.symbol == 'WQ'

    pos = Position('e1')
    white_king = board.get_piece(pos)
    assert white_king.symbol == 'WKi'

    pos = Position('f1')
    white_bishop_right = board.get_piece(pos)
    assert white_bishop_right.symbol == 'WB'

    pos = Position('g1')
    white_knight_right = board.get_piece(pos)
    assert white_knight_right.symbol == 'WK'

    pos = Position('h1')
    white_rook_right = board.get_piece(pos)
    assert white_rook_right.symbol == 'WR'

    for x in range(ord('a'), ord('h') + 1):
        square = '%s2' % chr(x)
        pos = Position(square)
        white_pawn = board.get_piece(pos)
        assert white_pawn.symbol == 'WP'
