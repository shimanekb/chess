"""
Unit tests for piece module.
"""
from chess.set import box


def test_str_constructor_white():
    # Given
    expected_symbol = 'WNA'
    chess_piece = box.Piece(box.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_constructor_black():
    # Given
    expected_symbol = 'BNA'
    chess_piece = box.Piece(box.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_pawn_white():
    # Given
    expected_symbol = 'WP'
    chess_piece = box.Pawn(box.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_pawn_black():
    # Given
    expected_symbol = 'BP'
    chess_piece = box.Pawn(box.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_rook_white():
    # Given
    expected_symbol = 'WR'
    chess_piece = box.Rook(box.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_rook_black():
    # Given
    expected_symbol = 'BR'
    chess_piece = box.Rook(box.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_knight_white():
    # Given
    expected_symbol = 'WK'
    chess_piece = box.Knight(box.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_knight_black():
    # Given
    expected_symbol = 'BK'
    chess_piece = box.Knight(box.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_bishop_white():
    # Given
    expected_symbol = 'WB'
    chess_piece = box.Bishop(box.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_bishop_black():
    # Given
    expected_symbol = 'BB'
    chess_piece = box.Bishop(box.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_queen_white():
    # Given
    expected_symbol = 'WQ'
    chess_piece = box.Queen(box.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_queen_black():
    # Given
    expected_symbol = 'BQ'
    chess_piece = box.Queen(box.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_king_white():
    # Given
    expected_symbol = 'WKi'
    chess_piece = box.King(box.Color.WHITE)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol


def test_str_king_black():
    # Given
    expected_symbol = 'BKi'
    chess_piece = box.King(box.Color.BLACK)

    # When
    actual_symbol = str(chess_piece)

    # Then
    assert actual_symbol == expected_symbol
