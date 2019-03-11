"""
Module for chess board related classes and functions.
"""
import re


class Board:
    """Chess board composed of rank file positions, and pieces at play.

    """
    def __init__(self):
        raise NotImplementedError()


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
