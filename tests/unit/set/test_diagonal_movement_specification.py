"""Tests for diagonal movement specification.
"""
from chess.set import table
from chess.set import box


def test_is_satisfied_by_no_piece_is_false():
    position_from = table.Position('a2')
    position_to = table.Position('a3')
    movement_specification = table.DiagonalMovementSpecification()

    valid_move = movement_specification\
        .is_satisfied_by(position_from, position_to)

    assert valid_move is False


def test_is_satisfied_by_forward_move_is_false():
    piece = box.Piece(symbol='P', color=box.Color.WHITE)
    position_from = table.Position('a2', piece=piece)
    position_to = table.Position('a3')
    movement_specification = table.DiagonalMovementSpecification()

    valid_move = movement_specification\
        .is_satisfied_by(position_from, position_to)

    assert valid_move is False


def test_is_satisfied_by_side_move_is_false():
    piece = box.Piece(symbol='P', color=box.Color.WHITE)
    position_from = table.Position('a2', piece=piece)
    position_to = table.Position('b2')
    movement_specification = table.DiagonalMovementSpecification()

    valid_move = movement_specification\
        .is_satisfied_by(position_from, position_to)

    assert valid_move is False


def test_is_satisfied_by_diagonal_move_is_true():
    piece = box.Piece(symbol='P', color=box.Color.WHITE)
    position_from = table.Position('a4', piece=piece)
    position_to = table.Position('b5')
    movement_specification = table.DiagonalMovementSpecification()

    valid_move = movement_specification \
        .is_satisfied_by(position_from, position_to)

    assert valid_move is True
