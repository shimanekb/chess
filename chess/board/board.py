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

        # Setup white
        self._setup_major_pieces(1, piece.Color.WHITE)
        self._setup_minor_pieces(2, piece.Color.WHITE)

        # Setup black
        self._setup_major_pieces(8, piece.Color.BLACK)
        self._setup_minor_pieces(7, piece.Color.BLACK)

    def _setup_major_pieces(self, rank, color):
        self._positions['a%s' % rank].piece = piece.Rook(color)
        self._positions['b%s' % rank].piece = piece.Knight(color)
        self._positions['c%s' % rank].piece = piece.Bishop(color)
        self._positions['d%s' % rank].piece = piece.Queen(color)
        self._positions['e%s' % rank].piece = piece.King(color)
        self._positions['f%s' % rank].piece = piece.Bishop(color)
        self._positions['g%s' % rank].piece = piece.Knight(color)
        self._positions['h%s' % rank].piece = piece.Rook(color)

    def _setup_minor_pieces(self, rank, color):
        for file in range(ord('a'), ord('h') + 1):
            square = '%s%s' % (chr(file), rank)
            self._positions[square].piece = piece.Pawn(color)

    def get_piece(self, position):
        """
        Gets chess piece at given position.

        Parameters
        ----------
        position : Position
            Position to get chess piece from.

        Returns
        -------
        chess.board.piece.Piece
            Chess piece if position is occupied, otherwise None.
        """
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
