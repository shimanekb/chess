"""
Module for pawn piece movement specification
"""
from chess.set.box import Pawn
from chess.set.box import Piece
from chess.set.box import Color
from chess.set.table import PawnMovementSpecification
from chess.set.table import Position


def test_is_satisified_by_not_pawn_is_false():
    movement_specification = PawnMovementSpecification()
    piece = Piece(symbol='FOO', color=Color.WHITE)

    position_from = Position('a2', piece=piece)
    position_to = Position('a3')

    is_satisfied_by_move = movement_specification.is_satisfied_by(
        position_from, position_to)

    assert is_satisfied_by_move is False


def test_is_satisfied_by_white_pawn_move_by_one_is_true():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.WHITE)

    position_from = Position('a2', piece=pawn)
    position_to = Position('a3')

    is_satisfied_by_move = movement_specification.is_satisfied_by(
        position_from, position_to)

    assert is_satisfied_by_move


def test_is_satisfied_by_white_pawn_move_by_one_backwards_false():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.WHITE)

    position_from = Position('a3', piece=pawn)
    position_to = Position('a2')

    is_satisfied_by_move = movement_specification.is_satisfied_by(
        position_from, position_to)

    assert is_satisfied_by_move is False


def test_is_satisfied_by_black_pawn_move_by_one_true():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.BLACK)

    position_from = Position('a7', piece=pawn)
    position_to = Position('a6')

    is_satisfied_by_move = movement_specification.is_satisfied_by(
        position_from, position_to)

    assert is_satisfied_by_move


def test_is_satisfied_by_black_pawn_move_by_one_backwards_false():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.BLACK)

    position_from = Position('a6', piece=pawn)
    position_to = Position('a7')

    is_satisfied_by_move = movement_specification.is_satisfied_by(
        position_from, position_to)

    assert is_satisfied_by_move is False


def test_is_satisfied_by_white_pawn_diagonal_true():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.WHITE)

    position_from = Position('a6', piece=pawn)
    position_to = Position('b7')

    is_satisfied_by_move = movement_specification.is_satisfied_by(
        position_from, position_to)

    assert is_satisfied_by_move is True
