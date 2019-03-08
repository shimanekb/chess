"""
Module for two player game of chess.
"""


def play_game():
    """Play two player game of chess.

    Returns
    -------
    None
    """
    raise NotImplementedError()


def quit_game():
    """Quits current game of chess.

    Returns
    -------
    None
    """
    raise NotImplementedError()


def move_piece(positionFrom, positionTo):
    """
    Move piece from one position to another on the board, possibly capturing an
    opponents piece.

    Parameters
    ----------
    positionFrom : Position
    positionTo : Position

    Returns
    -------
    None
    """
    raise NotImplementedError()
