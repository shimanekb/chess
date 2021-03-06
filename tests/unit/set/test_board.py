"""
Tests for chess.board.board.Board
"""
import pytest
from chess.set.table import Board
from chess.set.table import IllegalMoveError
from chess.set.table import Position


def test_init_default_white_board_setup():
    # When
    board = Board()

    # Then
    pos = Position('a1')
    white_rook_left = board.get_piece(pos)
    assert str(white_rook_left) == 'WR'

    pos = Position('b1')
    white_knight_left = board.get_piece(pos)
    assert str(white_knight_left) == 'WK'

    pos = Position('c1')
    white_bishop_left = board.get_piece(pos)
    assert str(white_bishop_left) == 'WB'

    pos = Position('d1')
    white_queen = board.get_piece(pos)
    assert str(white_queen) == 'WQ'

    pos = Position('e1')
    white_king = board.get_piece(pos)
    assert str(white_king) == 'WKi'

    pos = Position('f1')
    white_bishop_right = board.get_piece(pos)
    assert str(white_bishop_right) == 'WB'

    pos = Position('g1')
    white_knight_right = board.get_piece(pos)
    assert str(white_knight_right) == 'WK'

    pos = Position('h1')
    white_rook_right = board.get_piece(pos)
    assert str(white_rook_right) == 'WR'

    for x in range(ord('a'), ord('h') + 1):
        square = '%s2' % chr(x)
        pos = Position(square)
        white_pawn = board.get_piece(pos)
        assert str(white_pawn) == 'WP'


def test_init_default_black_board_setup():
    # When
    board = Board()

    # Then
    pos = Position('a8')
    black_rook_left = board.get_piece(pos)
    assert str(black_rook_left) == 'BR'

    pos = Position('b8')
    black_knight_left = board.get_piece(pos)
    assert str(black_knight_left) == 'BK'

    pos = Position('c8')
    black_bishop_left = board.get_piece(pos)
    assert str(black_bishop_left) == 'BB'

    pos = Position('d8')
    black_queen = board.get_piece(pos)
    assert str(black_queen) == 'BQ'

    pos = Position('e8')
    black_king = board.get_piece(pos)
    assert str(black_king) == 'BKi'

    pos = Position('f8')
    black_bishop_right = board.get_piece(pos)
    assert str(black_bishop_right) == 'BB'

    pos = Position('g8')
    black_knight_right = board.get_piece(pos)
    assert str(black_knight_right) == 'BK'

    pos = Position('h8')
    black_rook_right = board.get_piece(pos)
    assert str(black_rook_right) == 'BR'

    for x in range(ord('a'), ord('h') + 1):
        square = '%s7' % chr(x)
        pos = Position(square)
        black_pawn = board.get_piece(pos)
        assert str(black_pawn) == 'BP'


def test_move_piece_move_piece_is_moved():
    # Given
    board = Board()
    pos_from = Position('a2')
    pos_to = Position('a3')

    # When
    board.move_piece(pos_from, pos_to)

    # Then
    assert board.get_piece(pos_from) is None
    assert board.get_piece(pos_to) is not None
    assert str(board.get_piece(pos_to)) == 'WP'


def test_move_piece_piece_captured_move_to_occupied_position():
    # Given
    board = Board()

    # Check current state
    assert board.get_piece(Position('a2')) is not None
    assert str(board.get_piece(Position('a2'))) == 'WP'
    assert board.get_piece(Position('b7')) is not None
    assert str(board.get_piece(Position('b7'))) == 'BP'

    pos_from_to = [('a2', 'a3'), ('b7', 'b6'), ('a3', 'a4'),
                   ('b6', 'b5'), ('a4', 'b5')]

    # When
    for pos_from, pos_to in pos_from_to:
        board.move_piece(Position(pos_from), Position(pos_to))

    # Then
    assert board.get_piece(Position('b5')) is not None
    assert str(board.get_piece(Position('b5'))) == 'WP'


def test_move_piece_illegal_move_error_raised_move_to_unoccupied_position():
    with pytest.raises(IllegalMoveError):
        # Given
        board = Board()

        # When
        board.move_piece(Position('a3'), Position('a4'))

        # Then PyUnit verifies error raised
