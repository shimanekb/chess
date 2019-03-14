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


def test_init_default_black_board_setup():
    # When
    board = Board()

    # Then
    pos = Position('a8')
    black_rook_left = board.get_piece(pos)
    assert black_rook_left.symbol == 'BR'

    pos = Position('b8')
    black_knight_left = board.get_piece(pos)
    assert black_knight_left.symbol == 'BK'

    pos = Position('c8')
    black_bishop_left = board.get_piece(pos)
    assert black_bishop_left.symbol == 'BB'

    pos = Position('d8')
    black_queen = board.get_piece(pos)
    assert black_queen.symbol == 'BQ'

    pos = Position('e8')
    black_king = board.get_piece(pos)
    assert black_king.symbol == 'BKi'

    pos = Position('f8')
    black_bishop_right = board.get_piece(pos)
    assert black_bishop_right.symbol == 'BB'

    pos = Position('g8')
    black_knight_right = board.get_piece(pos)
    assert black_knight_right.symbol == 'BK'

    pos = Position('h8')
    black_rook_right = board.get_piece(pos)
    assert black_rook_right.symbol == 'BR'

    for x in range(ord('a'), ord('h') + 1):
        square = '%s7' % chr(x)
        pos = Position(square)
        black_pawn = board.get_piece(pos)
        assert black_pawn.symbol == 'BP'


def test_move_piece_move_piece_is_moved():
    # Given
    pos_from = Position('a2')
    pos_to = Position('a3')

    # When
    board = Board()
    board.move_piece(pos_from, pos_to)

    # Then
    assert board.get_piece(pos_from) is None
    assert board.get_piece(pos_to) is not None
    assert board.get_piece(pos_to).symbol == 'WP'


def test_move_piece_piece_captured_move_to_occupied_position():
    assert False
