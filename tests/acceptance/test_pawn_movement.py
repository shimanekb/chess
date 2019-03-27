"""
Acceptance tests for pawn movement.
"""
import pytest
from chess.set.table import IllegalMoveError
from chess.set.table import Board
from chess.set.table import Position
from chess.set.box import Color


def test_move_pawn_by_one_valid_movement():
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


def test_move_pawn_by_two_valid_movement():
    # Given
    board = Board()
    pawn_position_from = Position('a2')
    pawn_position_to = Position('a4')

    assert board.get_piece(pawn_position_to) is None
    assert board.get_piece(pawn_position_from).symbol == 'P'
    assert board.get_piece(pawn_position_from).color == Color.WHITE

    # When
    board.move_piece(pawn_position_from, pawn_position_to)

    # Then
    assert board.get_piece(pawn_position_to).symbol == 'P'


def test_move_pawn_diagonal_attack_valid_movement():
    # Given
    board = Board()
    setup_movements = [('a2', 'a4'), ('b7', 'b5')]

    for pos_to, pos_from in setup_movements:
        board.move_piece(Position(pos_to), Position(pos_from))

    pawn_position_from = Position('a4')
    pawn_position_to = Position('b5')

    assert board.get_piece(pawn_position_to).symbol == 'P'
    assert board.get_piece(pawn_position_to).color == Color.BLACK
    assert board.get_piece(pawn_position_from).symbol == 'P'
    assert board.get_piece(pawn_position_from).color == Color.WHITE

    # When
    board.move_piece(pawn_position_from, pawn_position_to)

    # Then
    assert board.get_piece(pawn_position_to).symbol == 'P'
    assert board.get_piece(pawn_position_to).color == Color.WHITE


def test_move_pawn_diagonal_on_empty_invalid_movement():
    with pytest.raises(IllegalMoveError):
        # Given
        board = Board()

        pawn_position_from = Position('a2')
        pawn_position_to = Position('a3')

        assert board.get_piece(pawn_position_to) is None
        assert board.get_piece(pawn_position_from).symbol == 'P'
        assert board.get_piece(pawn_position_from).color == Color.WHITE

        # When
        board.move_piece(pawn_position_from, pawn_position_to)


def test_move_pawn_sideways_invalid_movement():
    with pytest.raises(IllegalMoveError):
        # Given
        board = Board()

        board.move_piece(Position('a2'), Position('a3'))
        board.move_piece(Position('b7'), Position('b6'))

        pawn_position_from = Position('a3')
        pawn_position_to = Position('a4')

        assert board.get_piece(pawn_position_to) is None
        assert board.get_piece(pawn_position_from).symbol == 'P'
        assert board.get_piece(pawn_position_from).color == Color.WHITE

        # When
        board.move_piece(pawn_position_from, pawn_position_to)


def test_move_pawn_forward_by_three_invalid_movement():
    with pytest.raises(IllegalMoveError):
        # Given
        board = Board()

        pawn_position_from = Position('a2')
        pawn_position_to = Position('a5')

        assert board.get_piece(pawn_position_to) is None
        assert board.get_piece(pawn_position_from).symbol == 'P'
        assert board.get_piece(pawn_position_from).color == Color.WHITE

        # When
        board.move_piece(pawn_position_from, pawn_position_to)
