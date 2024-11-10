from models.Pieces.Piece import Piece
from models.Enums.Player import Player
from typing import List, Tuple


class Knight(Piece):
    def __init__(self, row: int, col: int, player) -> None:
        self.row = row
        self.col = col
        self.player = player

    def valid_moves(self, board) -> List[Tuple[int, int]]:
        moves = set()
        directions = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
        for x,y in directions:
            #if in bounds and not an allied piece, move
            new_row, new_col = self.row + x, self.col + y
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if (board[new_row][new_col].is_empty() or
                board[new_row][new_col].get_piece().player != self.player):
                    moves.add((new_row, new_col))
                
        return moves


    def to_string(self) -> str:
        return "N"