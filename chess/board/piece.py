"""
Module for chess piece functionality.
"""
from enum import Enum


class Color(Enum):
    """ Color for chess pieces.
    """
    WHITE = 'W'
    BLACK = 'B'


class Piece:
    """Base class for chess pieces.

    Attributes
    ----------
    position : chess.board.Position
        Position of chess piece.
    color : chess.piece.Color
        Color of chess piece, which can be White or Black.
    symbol : str
        Display symbol of chess piece. Defaults to NA.
    """
    def __init__(self, position, color, symbol='NA'):
        self.position = position
        self.symbol = symbol
        self.color = color

    def __str__(self):
        return self.color.value + self.symbol


class Pawn(Piece):
    """Pawn chess piece.

    Attributes
    ----------
    position : chess.board.Position
        Position of chess piece.
    color : chess.piece.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, position, color, symbol='P'):
        super().__init__(position, color, symbol=symbol)


class Rook(Piece):
    """Rook chess piece.

    Attributes
    ----------
    position : chess.board.Position
        Position of chess piece.
    color : chess.piece.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, position, color, symbol='R'):
        super().__init__(position, color, symbol=symbol)


class Knight(Piece):
    """Knight chess piece.

    Attributes
    ----------
    position : chess.board.Position
        Position of chess piece.
    color : chess.piece.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, position, color, symbol='K'):
        super().__init__(position, color, symbol=symbol)
