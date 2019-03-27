"""
Module of chess box items (pieces ...)
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
    color : chess.box.Color
        Color of chess piece, which can be White or Black.
    symbol : str, optional(default='NA')
        Display symbol of chess piece. Defaults to NA.
    """
    def __init__(self, color, symbol='NA'):
        self.symbol = symbol
        self.color = color

    def __str__(self):
        return self.color.value + self.symbol


class Pawn(Piece):
    """Pawn chess piece.

    Attributes
    ----------
    color : chess.box.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, color, symbol='P'):
        super().__init__(color, symbol=symbol)


class Rook(Piece):
    """Rook chess piece.

    Attributes
    ----------
    color : chess.box.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, color, symbol='R'):
        super().__init__(color, symbol=symbol)


class Knight(Piece):
    """Knight chess piece.

    Attributes
    ----------
    color : chess.box.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, color, symbol='K'):
        super().__init__(color, symbol=symbol)


class Bishop(Piece):
    """Bishop chess piece.

    Attributes
    ----------
    color : chess.box.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, color, symbol='B'):
        super().__init__(color, symbol=symbol)


class Queen(Piece):
    """Queen chess piece.

    Attributes
    ----------
    color : chess.box.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, color, symbol='Q'):
        super().__init__(color, symbol=symbol)


class King(Piece):
    """King chess piece.

    Attributes
    ----------
    color : chess.box.Color
        Color of chess piece, which can be White or Black.
    """
    def __init__(self, color, symbol='Ki'):
        super().__init__(color, symbol=symbol)
