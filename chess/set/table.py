"""
Module for chess table items (board ...)
"""
import re
from chess.set import box


class Board:
    """Chess board composed of rank file positions, and pieces at play.

    """
    def __init__(self):
        self._positions = dict()
        for file in range(ord('a'), ord('h') + 1):
            for rank in range(1, 9):
                square = '%s%s' % (chr(file), rank)
                self._positions[square] = Position(square)

        self._movement_specs = {'P': PawnMovementSpecification()}

        # Setup white
        self._setup_major_pieces(1, box.Color.WHITE)
        self._setup_minor_pieces(2, box.Color.WHITE)

        # Setup black
        self._setup_major_pieces(8, box.Color.BLACK)
        self._setup_minor_pieces(7, box.Color.BLACK)

    def _setup_major_pieces(self, rank, color):
        self._positions['a%s' % rank].piece = box.Rook(color)
        self._positions['b%s' % rank].piece = box.Knight(color)
        self._positions['c%s' % rank].piece = box.Bishop(color)
        self._positions['d%s' % rank].piece = box.Queen(color)
        self._positions['e%s' % rank].piece = box.King(color)
        self._positions['f%s' % rank].piece = box.Bishop(color)
        self._positions['g%s' % rank].piece = box.Knight(color)
        self._positions['h%s' % rank].piece = box.Rook(color)

    def _setup_minor_pieces(self, rank, color):
        for file in range(ord('a'), ord('h') + 1):
            square = '%s%s' % (chr(file), rank)
            self._positions[square].piece = box.Pawn(color)

    def move_piece(self, position_from, position_to):
        """Moves piece from one position to another. Capturing a piece occupied
        by the position to move to.

        Parameters
        ----------
        position_from : chess.set.table.Position
            Position to move piece from.
        position_to : chess.set.table.Position
            Position to move piece to.

        Returns
        -------
        None

        Raises
        ------
        chess.board.board.IllegalMoveError
            Raised when piece move is illegal.
        """
        piece = self.get_piece(position_from)
        board_position_from = self._positions[str(position_from)]
        board_position_to = self._positions[str(position_to)]

        if piece is None:
            raise IllegalMoveError('No piece to move at %s'
                                   % str(position_from))
        if not self._movement_specs[piece.symbol].is_satisfied_by(
                board_position_from, board_position_to):
            raise IllegalMoveError('Illegal move for piece %s' % str(piece))

        self._remove_piece(position_from)
        self._place_piece(position_to, piece)

    def _place_piece(self, position, piece):
        """ Places piece at given position, if a piece is already
        in the position, it is captured.

        Parameters
        ----------
        position : chess.set.table.Position
            Position to place the piece on.
        piece : chess.set.box.Piece
            Chess piece to place at position.

        Returns
        -------
        None

        """
        self._positions[str(position)].piece = piece

    def _remove_piece(self, position):
        self._positions[str(position)].piece = None

    def get_piece(self, position):
        """Gets chess piece at given position.

        Parameters
        ----------
        position: chess.set.table.Position
            Position to get chess piece from.

        Returns
        -------
        chess.box.Piece
            Chess piece if position is occupied, otherwise None.
        """
        return self._positions[str(position)].piece


class Position:
    """Represents a chess position on the board.

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
    piece : chess.set.box.Piece, optional(default=None)
        Chess piece at position. Defaults to None.

    Raises
    ------
    ValueError
        If invalid square format.
    """

    def __init__(self, square, piece=None):
        if not re.match('^[a-hA-H][1-8]$', square):
            raise ValueError('Invalid position format needs to '
                             'be [a-e][1-8]: %s' % square)
        self.file = square[0].lower()
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


class MovementCompositeSpecification:

    def is_satisfied_by(self, position_from, position_to):
        """Is the position change a valid move.

        Parameters
        ----------
        position_from : chess.set.table.Position
            Position to move piece from.
        position_to : chess.set.table.Position
            Position to move piece to.

        Returns
        -------
        bool
            If move is valid.

        """
        raise NotImplementedError()

    def __and__(self, movement_specification):
        return AndMovementSpecification(self, movement_specification)

    def __or__(self, movement_specification):
        return OrMovementSpecification(self, movement_specification)

    @staticmethod
    def rank_distance(position_from, position_to):
        """Calculates position distance between ranks.

        Parameters
        ----------
        position_from : chess.set.table.Position
            Position to move piece from.
        position_to : chess.set.table.Position
            Position to move piece to.

        Returns
        -------
        int
            Distance in positions between ranks.

        """
        return position_to.rank - position_from.rank

    @staticmethod
    def file_distance(position_from, position_to):
        """Calculates distance between files (ordinal).

        ----------
        position_from : chess.set.table.Position
            Position to move piece from.
        position_to : chess.set.table.Position
            Position to move piece to.

        Returns
        -------
        int
            Ordinal distance in positions between files.
        """
        return ord(position_to.file) - ord(position_from.file)


class OrMovementSpecification(MovementCompositeSpecification):
    """Combines two MovementSpecifications logically by Or.

    Attributes
    ----------
    movement_specification_one: MovementCompositeSpecification
        Movement specification one (left) to combine
    movement_specification_two: MovementCompositeSpecification
        Movement specification two (right) to combine
    """

    def __init__(self, movement_specification_one, movement_specification_two):
        self.movement_specification_one = movement_specification_one
        self.movement_specification_two = movement_specification_two

    def is_satisfied_by(self, position_from, position_to):
        """Is the position change a valid move.

        Parameters
        ----------
        position_from : chess.set.table.Position
            Position to move piece from.
        position_to : chess.set.table.Position
            Position to move piece to.

        Returns
        -------
        bool
            If move is valid.
        """
        return self.movement_specification_one.is_satisified_by(
            position_from, position_to) \
            or self.movement_specification_two.is_satisfied_by(
            position_from, position_to)


class AndMovementSpecification(MovementCompositeSpecification):
    """Combines two MovementSpecifications logically by And.

    Attributes
    ----------
    movement_specification_one: MovementCompositeSpecification
        Movement specification one (left) to combine
    movement_specification_two: MovementCompositeSpecification
        Movement specification two (right) to combine
    """

    def __init__(self, movement_specification_one, movement_specification_two):
        self.movement_specification_one = movement_specification_one
        self.movement_specification_two = movement_specification_two

    def is_satisfied_by(self, position_from, position_to):
        """Is the position change a valid move.

        Parameters
        ----------
        position_from : chess.set.table.Position
            Position to move piece from.
        position_to : chess.set.table.Position
            Position to move piece to.

        Returns
        -------
        bool
            If move is valid.
        """
        return self.movement_specification_one.is_satisified_by(
            position_from, position_to) \
            and self.movement_specification_two.is_satisfied_by(
            position_from, position_to)


class ForwardMovementSpecification(MovementCompositeSpecification):
    """Specification for forward piece movement."""

    def is_satisfied_by(self, position_from, position_to):
        """Is piece moving forward.

        Parameters
        ----------
        position_from : chess.set.table.Position
            Position to move piece from.
        position_to : chess.set.table.Position
            Position to move piece to.

        Returns
        -------
        bool
            If move is valid.
        """
        piece = position_from.piece
        if piece is not None:
            return self._is_movement_forward(position_from, position_to)
        else:
            return False

    def _is_movement_forward(self, position_from, position_to):
        file_distance = self.file_distance(position_from, position_to)
        rank_distance = self.rank_distance(position_from, position_to)
        piece = position_from.piece

        if piece.color is box.Color.WHITE:
            return file_distance == 0 and rank_distance > 0
        else:
            return file_distance == 0 and rank_distance < 0


class PawnMovementSpecification(MovementCompositeSpecification):
    """Movement specification for valid pawn movements.
    """

    def is_satisfied_by(self, position_from, position_to):
        """Is valid pawn move.

        Parameters
        ----------
        position_from : chess.set.table.Position
            Position to move piece from.
        position_to : chess.set.table.Position
            Position to move piece to.

        Returns
        -------
        bool
            If move is valid.
        """
        piece = position_from.piece
        if piece is not None and piece.symbol == 'P':
            return ForwardMovementSpecification()\
                .is_satisfied_by(position_from, position_to)
        else:
            return False


class ChessError(Exception):
    """Base class for chess exceptions."""
    pass


class IllegalMoveError(ChessError):
    """Illegal chess move was attempted."""
    pass
