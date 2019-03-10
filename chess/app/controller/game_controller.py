"""
Module for two player game of chess.
"""


QUIT = 'Q'


def play_game():
    """Play two player game of chess.

    Returns
    -------
    None
    """
    while True:
        display_board()
        user_input = ask_move()

        if user_input.upper() == QUIT:
            break


def display_board():
    """Displays current chess board state

    Returns
    -------
    None
    """
    # does nothing


def ask_move():
    """Ask user for move to make.

    Returns
    -------
    str
        User movement input.
    """
    user_input = input('Please make a move (example a5 a6) or quit (Q):')
    return user_input


def move_piece(positionFrom, positionTo):
    """
    Move piece from one position to another on the board, possibly capturing an
    opponents piece.

    Parameters
    ----------
    positionFrom : Position
        Position to move piece from.
    positionTo : Position
        Position to move piece to.

    Returns
    -------
    None
    """
    raise NotImplementedError()


def capture_piece(position):
    """
    Capture piece if one is at given position.

    Parameters
    ----------
    position : Position

    Returns
    -------
    None
    """
    raise NotImplementedError()
