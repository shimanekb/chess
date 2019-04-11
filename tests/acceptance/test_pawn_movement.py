"""
Acceptance tests for pawn movement.
"""
import pytest
from chess.set.box import Color
from chess.set.table import Board
from chess.set.table import IllegalMoveError
from chess.set.table import Position


def test_move_white_pawn_forward_valid_movement():
    # Given
    board = Board()
    pawn_position_from = Position('a2')
    pawn_position_to = Position('a3')

    assert board.get_piece(pawn_position_to) is None
    assert board.get_piece(pawn_position_from).symbol == 'P'

    # When
    board.move_piece(pawn_position_from, pawn_position_to)

    # Then
    assert board.get_piece(pawn_position_to).symbol == 'P'


def test_move_black_pawn_forward_valid_movement():
    # Given
    board = Board()
    pawn_position_from = Position('b7')
    pawn_position_to = Position('b6')

    assert board.get_piece(pawn_position_to) is None
    assert board.get_piece(pawn_position_from).symbol == 'P'

    # When
    board.move_piece(pawn_position_from, pawn_position_to)

    # Then
    assert board.get_piece(pawn_position_to).symbol == 'P'


def test_move_white_pawn_diagonal_capture_valid_movement():
    # Given
    board = Board()
    board.move_piece(Position('a2'), Position('a4'))
    board.move_piece(Position('b7'), Position('b5'))

    pawn_position_from = Position('a4')
    pawn_position_to = Position('b5')

    assert board.get_piece(pawn_position_to).color == Color.BLACK
    assert board.get_piece(pawn_position_to).symbol == 'P'

    assert board.get_piece(pawn_position_from).color == Color.WHITE
    assert board.get_piece(pawn_position_from).symbol == 'P'

    # When
    board.move_piece(pawn_position_from, pawn_position_to)

    # Then
    assert board.get_piece(pawn_position_to).color == Color.WHITE
    assert board.get_piece(pawn_position_to).symbol == 'P'


def test_move_black_pawn_diagonal_capture_valid_movement():
    # Given
    board = Board()
    board.move_piece(Position('a2'), Position('a4'))
    board.move_piece(Position('b7'), Position('b5'))
    board.move_piece(Position('b2'), Position('b3'))

    pawn_position_from = Position('b5')
    pawn_position_to = Position('a4')

    assert board.get_piece(pawn_position_to).color == Color.WHITE
    assert board.get_piece(pawn_position_to).symbol == 'P'

    assert board.get_piece(pawn_position_from).color == Color.BLACK
    assert board.get_piece(pawn_position_from).symbol == 'P'

    # When
    board.move_piece(pawn_position_from, pawn_position_to)

    # Then
    assert board.get_piece(pawn_position_to).color == Color.BLACK
    assert board.get_piece(pawn_position_to).symbol == 'P'


def test_move_white_pawn_back_capture_invalid_movement():
    with pytest.raises(IllegalMoveError):
        # Given
        board = Board()
        board.move_piece(Position('a2'), Position('a3'))
        board.move_piece(Position('b7'), Position('b6'))

        pawn_position_from = Position('a3')
        pawn_position_to = Position('a2')

        assert board.get_piece(pawn_position_to) is None
        assert board.get_piece(pawn_position_from).color == Color.WHITE
        assert board.get_piece(pawn_position_from).symbol == 'P'

        # When
        board.move_piece(pawn_position_from, pawn_position_to)
