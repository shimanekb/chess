"""
Module for chess board related classes and functions.
"""
import re
from chess.board import piece


class Board:
    """Chess board composed of rank file positions, and pieces at play.

    """
    def __init__(self):
        self._positions = dict()
        for file in range(ord('a'), ord('h') + 1):
            for rank in range(1, 9):
                square = '%s%s' % (chr(file), rank)
                self._positions[square] = Position(square)
        self._setup_white()

    def _setup_white(self):
        self._positions['a1'].piece = piece.Rook(piece.Color.WHITE)
        self._positions['b1'].piece = piece.Knight(piece.Color.WHITE)
        self._positions['c1'].piece = piece.Bishop(piece.Color.WHITE)
        self._positions['d1'].piece = piece.Queen(piece.Color.WHITE)
        self._positions['e1'].piece = piece.King(piece.Color.WHITE)
        self._positions['f1'].piece = piece.Bishop(piece.Color.WHITE)
        self._positions['g1'].piece = piece.Knight(piece.Color.WHITE)
        self._positions['h1'].piece = piece.Rook(piece.Color.WHITE)

        for file in range(ord('a'), ord('h') + 1):
            square = '%s2' % chr(file)
            self._positions[square].piece = piece.Pawn(piece.Color.WHITE)

    def get_piece(self, position):
        return self._positions[str(position)].piece


class Position:
    """
    Represents a chess position on the board.

    Parameters
    ----------
    square : str
        Chess board position string in the form [file][rank].

    Attributes
    ----------
    file : str
        Chess board column position, values in a-h
    rank : int
        Chess board row position, values 1-8
    piece : Piece
        Chess piece at position. Defaults to None.

    Raises
    ------
    ValueError
        If invalid square format.
    """

    def __init__(self, square, piece=None):
        if not re.match('^[a-hA-H][1-8]$', square):
            raise ValueError('Invalid square format needs to '
                             'be [a-e][1-8]: %s' % square)
        self.file = square[0]
        self.rank = int(square[1])
        self.piece = piece

    def is_occupied(self):
        """Informs if position is occupied by a chess piece.

        Returns
        -------
        bool
            Returns true if occupied by a chess piece, otherwise false.
        """
        return self.piece is not None

    def __str__(self):
        return '%s%s' % (self.file, self.rank)
