"""
Unit tests for piece module.
"""
from chess.board import board
from chess.board import piece


def test_str_constructor_white(mocker):
    # Given
    expected_symbol = 'WNA'
    position = mocker.MagicMock(rank='b', file='2', piece=None, spec=board.Position)
    chess_piece = piece.Piece(position, piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_constructor_black(mocker):
    # Given
    expected_symbol = 'BNA'
    position = mocker.MagicMock(rank='b', file='2', piece=None, spec=board.Position)
    chess_piece = piece.Piece(position, piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_pawn_white(mocker):
    # Given
    expected_symbol = 'WP'
    position = mocker.MagicMock(rank='b', file='2', piece=None, spec=board.Position)
    chess_piece = piece.Pawn(position, piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_pawn_black(mocker):
    # Given
    expected_symbol = 'BP'
    position = mocker.MagicMock(rank='b', file='2', piece=None, spec=board.Position)
    chess_piece = piece.Pawn(position, piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_rook_white(mocker):
    # Given
    expected_symbol = 'WR'
    position = mocker.MagicMock(rank='b', file='2', piece=None, spec=board.Position)
    chess_piece = piece.Rook(position, piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_rook_black(mocker):
    # Given
    expected_symbol = 'BR'
    position = mocker.MagicMock(rank='b', file='2', piece=None, spec=board.Position)
    chess_piece = piece.Rook(position, piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_knight_white(mocker):
    # Given
    expected_symbol = 'WK'
    position = mocker.MagicMock(rank='b', file='2', piece=None, spec=board.Position)
    chess_piece = piece.Knight(position, piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_knight_black(mocker):
    # Given
    expected_symbol = 'BK'
    position = mocker.MagicMock(rank='b', file='2', piece=None, spec=board.Position)
    chess_piece = piece.Knight(position, piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol
