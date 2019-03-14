"""
Unit tests for piece module.
"""
from chess.board import board
from chess.board import piece


def test_str_constructor_white():
    # Given
    expected_symbol = 'WNA'
    chess_piece = piece.Piece(piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_constructor_black():
    # Given
    expected_symbol = 'BNA'
    chess_piece = piece.Piece(piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_pawn_white():
    # Given
    expected_symbol = 'WP'
    chess_piece = piece.Pawn(piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_pawn_black():
    # Given
    expected_symbol = 'BP'
    chess_piece = piece.Pawn(piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_rook_white():
    # Given
    expected_symbol = 'WR'
    chess_piece = piece.Rook(piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_rook_black():
    # Given
    expected_symbol = 'BR'
    chess_piece = piece.Rook(piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_knight_white():
    # Given
    expected_symbol = 'WK'
    chess_piece = piece.Knight(piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_knight_black():
    # Given
    expected_symbol = 'BK'
    chess_piece = piece.Knight(piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_bishop_white():
    # Given
    expected_symbol = 'WB'
    chess_piece = piece.Bishop(piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_bishop_black():
    # Given
    expected_symbol = 'BB'
    chess_piece = piece.Bishop(piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_queen_white():
    # Given
    expected_symbol = 'WQ'
    chess_piece = piece.Queen(piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_queen_black():
    # Given
    expected_symbol = 'BQ'
    chess_piece = piece.Queen(piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_king_white():
    # Given
    expected_symbol = 'WKi'
    chess_piece = piece.King(piece.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_king_black():
    # Given
    expected_symbol = 'BKi'
    chess_piece = piece.King(piece.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol
