"""
Module for chess.board.board.Position tests.
"""
import pytest
from chess.board.board import Position
from chess.board.piece import Piece


def test_is_occupied_no_piece_unoccupied():
    # Given
    rank = '1'
    file = 'e'
    square = '%s%s' % (file, rank)

    # When
    position = Position(square)

    # Then
    assert not position.is_occupied()


def test_is_occupied_has_piece_occupied(mocker):
    # Given
    piece_mock = mocker.MagicMock(spec=Piece)
    rank = '1'
    file = 'e'
    square = '%s%s' % (file, rank)

    # When
    position = Position(square, piece=piece_mock)

    # Then
    assert position.is_occupied()


def test_init_bad_rank_range_value_error():
    with pytest.raises(ValueError):
        # Given
        rank = '0'
        file = 'e'
        square = '%s%s' % (file, rank)

        # When
        Position(square)

        # Then pytest checks Exception


def test_init_bad_rank_type_value_error():
    with pytest.raises(ValueError):
        # Given
        rank = 'A'
        file = 'e'
        square = '%s%s' % (file, rank)

        # When
        Position(square)

        # Then pytest checks Exception


def test_init_bad_file_range_value_error():
    with pytest.raises(ValueError):
        # Given
        rank = 1
        file = 'i'
        square = '%s%s' % (file, rank)

        # When
        Position(square)

        # Then pytest checks Exception


def test_init_bad_file_type_value_error():
    with pytest.raises(ValueError):
        # Given
        rank = 1
        file = 9
        square = '%s%s' % (file, rank)

        # When
        Position(square)

        # Then pytest checks Exception


def test_init_valid_file_rank_no_error():
    # Given
    rank = 1
    file = 'a'
    square = '%s%s' % (file, rank)

    # When
    pos = Position(square)

    # Then
    assert pos is not None
