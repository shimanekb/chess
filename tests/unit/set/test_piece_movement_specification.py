"""
Module for piece movement specification
"""
from chess.set.box import Pawn
from chess.set.box import Color
from chess.set.table import PawnMovementSpecification
from chess.set.table import Position


def test_is_valid_white_pawn_move_by_one_is_true():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.WHITE)

    is_valid_move = movement_specification.is_valid(pawn,
                                                    Position('a2'),
                                                    Position('a3'))

    assert is_valid_move


def test_is_valid_white_pawn_move_by_one_backwards_false():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.WHITE)

    is_valid_move = movement_specification.is_valid(pawn,
                                                    Position('a3'),
                                                    Position('a2'))

    assert is_valid_move is False


def test_is_valid_black_pawn_move_by_one_true():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.BLACK)

    is_valid_move = movement_specification.is_valid(pawn,
                                                    Position('a7'),
                                                    Position('a6'))

    assert is_valid_move


def test_is_valid_black_pawn_move_by_one_backwards_false():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.BLACK)

    is_valid_move = movement_specification.is_valid(pawn,
                                                    Position('a6'),
                                                    Position('a7'))

    assert is_valid_move is False


def test_is_valid_black_pawn_move_by_two_on_first_movement_true():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.BLACK)

    is_valid_move = movement_specification.is_valid(pawn,
                                                    Position('a7'),
                                                    Position('a5'))

    assert is_valid_move


def test_is_valid_black_pawn_move_by_two_not_on_first_movement_false():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.BLACK)
    pawn.been_moved = True

    is_valid_move = movement_specification.is_valid(pawn,
                                                    Position('a7'),
                                                    Position('a5'))

    assert is_valid_move is False


def test_is_valid_white_pawn_move_by_two_on_first_movement_true():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.WHITE)

    is_valid_move = movement_specification.is_valid(pawn,
                                                    Position('a2'),
                                                    Position('a4'))

    assert is_valid_move


def test_is_valid_white_pawn_move_by_two_not_on_first_movement_false():
    movement_specification = PawnMovementSpecification()
    pawn = Pawn(Color.WHITE)
    pawn.been_moved = True

    is_valid_move = movement_specification.is_valid(pawn,
                                                    Position('a2'),
                                                    Position('a4'))

    assert is_valid_move is False


def test_is_valid_white_pawn_diagonal_capture_black_piece_true():
    assert False
