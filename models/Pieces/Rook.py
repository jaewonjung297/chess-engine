from models.Pieces.Piece import Piece
from typing import List, Tuple
from models.Enums.Player import Player


class Rook(Piece):
    def __init__(self, row: int, col: int, player) -> None:
        self.row = row
        self.col = col
        self.player = player

    def move_piece(self, new_row, new_col) -> bool:
        self.row = new_row
        self.col = new_col
        return True

    def valid_moves(self, board) -> List[Tuple[int, int]]:
        moves = set()

        directions = [[0,-1],[0,1],[1,0],[-1,0]]
        for x,y in directions:
            new_row, new_col = self.row, self.col
            #keep going in direction until you hit any piece, then process conditionally
            while True:
                new_row += x
                new_col += y
                if not 0 <= new_row < 8 or not 0 <= new_col < 8:
                    break
                #not out of bounds. see if you can move 
                if board[new_row][new_col].is_empty():
                    moves.add((new_row, new_col))
                    continue
                else:
                    if board[new_row][new_col].get_piece().player != self.player:
                        moves.add((new_row, new_col))
                    break
        return moves

    def to_string(self) -> str:
        return f"{'w' if self.player == Player.WHITE else 'b'}r"