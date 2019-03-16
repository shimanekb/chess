"""
Module for two player game of chess.
"""
from chess.board import Board
from chess.app.view import board_view


QUIT = 'Q'


def play_game():
    """Play two player game of chess.

    Returns
    -------
    None
    """
    board = Board()
    while True:
        display_board(board)
        user_input = ask_move()

        if user_input.upper() == QUIT:
            break


def display_board(board):
    """Displays current chess board state

    Parameters
    ----------
    board : chess.board.Board
        Board to display.

    Returns
    -------
    None
    """
    return board_view.display(board)


def ask_move():
    """Ask user for move to make.

    Returns
    -------
    str
        User movement input.
    """
    user_input = input('Make a move(ex. b2 b3) or Q to quit:')
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
