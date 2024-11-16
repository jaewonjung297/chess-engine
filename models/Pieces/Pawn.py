from typing import Tuple
from models.Enums.Player import Player


class Pawn():
    def __init__(self, row: int, col: int, player) -> None:
        self.row = row
        self.col = col
        self.player = player

    def move_piece(self, new_row, new_col) -> bool:
        self.row = new_row
        self.col = new_col
        return True

    def valid_moves(self, board) -> set[Tuple[int, int]]:
        #move forward
        moves = set()
        if self.player == Player.BLACK:
            if self.row + 1 < 8 and board[self.row + 1][self.col].is_empty():
                moves.add((self.row + 1, self.col))
            if self.row == 1 and board[self.row + 2][self.col].is_empty() and board[self.row + 1][self.col].is_empty():  # noqa: E501
                moves.add((self.row + 2, self.col))
            #process down right attack, check end bounds
            if self.col < 7 and not board[self.row + 1][self.col + 1].is_empty() and board[self.row + 1][self.col + 1].get_piece().player == Player.WHITE:  # noqa: E501
                moves.add((self.row + 1, self.col + 1))
            if self.col > 0 and not board[self.row + 1][self.col - 1].is_empty() and board[self.row + 1][self.col - 1].get_piece().player == Player.WHITE:  # noqa: E501
                moves.add((self.row + 1, self.col - 1))
        
        if self.player == Player.WHITE:
            if self.row - 1 > 0 and board[self.row - 1][self.col].is_empty():
                moves.add((self.row - 1, self.col))
            if self.row == 6 and board[self.row - 2][self.col].is_empty() and board[self.row - 1][self.col].is_empty():  # noqa: E501
                moves.add((self.row - 2, self.col))
            if self.col < 7 and not board[self.row - 1][self.col + 1].is_empty() and board[self.row - 1][self.col + 1].get_piece().player == Player.BLACK:  # noqa: E501
                moves.add((self.row - 1, self.col + 1))
            if self.col > 0 and not board[self.row - 1][self.col - 1].is_empty() and board[self.row - 1][self.col - 1].get_piece().player == Player.BLACK:  # noqa: E501
                moves.add((self.row - 1, self.col - 1))

        return moves

    def can_attack_king(self, opponent_king, board):
        if (opponent_king.row, opponent_king.col) in self.valid_moves(board):
            return True
        return False

    def to_string(self) -> str:
        return f"{'w' if self.player == Player.WHITE else 'b'}p"