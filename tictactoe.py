"""Defines objects and logic for a basic game of TicTacToe
"""

import numpy as np
from typing import List


class Player:
    """A participant in a Tic Tac Toe Game

    Attributes:
        name: String referencing the player name.
        marker: The piece placed on the board to show the player's move.
    """

    def __init__(self, name: str, marker: str):
        self.name = name
        self.marker = marker

    def __str__(self) -> str:
        return f"{self.name}: {self.marker}"


class Board:
    """A playing board for a game of Tic Tac Toe

    Attributes:
        pieces: a 3x3 character array defining the current placement of pieces
        num_rows: an int describing how many rows there are.
        num_cols: an int describing how many cols there are.
    """

    def __init__(self):
        self.num_rows = 3
        self.num_cols = 3
        self.pieces = np.empty((self.num_rows, self.num_cols), dtype=str)
    
    def __str__(self) -> str:
        board_str = ''
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if marker:= self.pieces[i,j]:
                    board_str += marker
                else:
                    board_str += ' '
                if j < self.num_cols - 1:
                    board_str += ' | '
            board_str += '\n'
            if i < self.num_rows - 1:
                board_str += '-' * (self.num_cols * 4 - 3)
                board_str += '\n'
        return board_str 


class Game:
    """Holds the logic for coordinating a game of Tic Tac Toe

    Attributes
        players: ordered list of players, in turn order.
        board: a playing board.
        next_player: int index of the next player to move, in the player array.
    """

    def __init__(
        self,
        p1_name: str = "Player 1",
        p1_marker: str = "X",
        p2_name="Player 2",
        p2_marker: str = "O",
    ):
        self.players = [Player(p1_name, p1_marker), Player(p2_name, p2_marker)]
        self.board = Board()
        self.next_player = 0

    def _evaluate_markers_for_win(self, markers: List[str]) -> Player:
        first_char = markers[0]
        distinct_markers = set(markers)
        if len(distinct_markers) == 1 and markers[0]:
            return next(
                filter(lambda player: player.marker == first_char, self.players)
            )
        else:
            return None

    def is_won(self) -> Player:
        """If a player has won, returns that player. O/w returns None

        This could be improved by a more general method for evaluating a set of
        peices for winning, and then this method is just in charge of passing
        the sets to check in... but for now this is fine.
        """
        # check rows
        for i in range(self.board.num_rows):
            if winning_player := self._evaluate_markers_for_win(
                self.board.pieces[i, :]
            ):
                return winning_player

        # check cols
        for i in range(self.board.num_cols):
            if winning_player := self._evaluate_markers_for_win(
                self.board.pieces[:, i]
            ):
                return winning_player

        # Check Diagonals
        if winning_player := self._evaluate_markers_for_win(np.diag(self.board.pieces)):
            return winning_player

        if winning_player := self._evaluate_markers_for_win(
            np.diag(np.fliplr(self.board.pieces))
        ):
            return winning_player

    def place_piece(self, col_id: int, row_id: int, marker: str) -> None:
        """Places the marker at the specified coordinates

        TODO: Raise an error if coords are out of bounds, or already used.
        """
        self.board.pieces[col_id][row_id] = marker

    def __str__(self) -> str:
        to_return = [player.__str__() for player in self.players]
        to_return.append(self.board.__str__())
        return "\n".join(to_return)
