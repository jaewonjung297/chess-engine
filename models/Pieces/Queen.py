from models.Pieces.Piece import Piece
from typing import List, Tuple


class Queen(Piece):
    def __init__(self, file: int, rank: int, player) -> None:
        self.file = file
        self.rank = rank
        self.player = player

    def valid_moves(self, board) -> List[Tuple[int, int]]:
        #move forward
        pass


    def to_string(self) -> str:
        return "Q"