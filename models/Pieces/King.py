from models.Pieces.Piece import Piece
from typing import List, Tuple
from models.Enums.Player import Player


class King(Piece):
    def __init__(self, row: int, col: int, player) -> None:
        self.row = row
        self.col = col
        self.player = player
        self.moved_yet = False

    def move_piece(self, new_row, new_col) -> bool:
        self.row = new_row
        self.col = new_col
        self.moved_yet |= True
        return True

    def valid_moves(self, board) -> List[Tuple[int, int]]:
        moves = set()

        directions = [[0,-1],[0,1],[1,0],[-1,0], [1, -1], [1, 1], [-1, 1], [-1, -1]]
        for x,y in directions:
            new_row, new_col = self.row + x, self.col + y
            if not 0 <= new_row < 8 or not 0 <= new_col < 8:
                continue
            if board[new_row][new_col].is_empty():
                moves.add((new_row, new_col))
                continue
            if board[new_row][new_col].get_piece().player != self.player:
                moves.add((new_row, new_col))

        return moves

    def to_string(self) -> str:
        return f"{'w' if self.player == Player.WHITE else 'b'}k"

    def is_in_check(self, board):
        for row in board:
            for tile in row:
                if not tile.is_empty() and tile.get_piece().player != self.player:
                    if (self.row, self.col) in tile.get_piece().valid_moves(board):
                        return True
        return False