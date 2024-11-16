from models.Pieces.Piece import Piece

class Tile():
    def __init__(self, file: int, rank: int) -> None:
        self.file = file
        self.rank = rank
        self.piece = None

    def to_string(self) -> str:
        return f"{self.file}{self.rank}"

    def to_notation_string(self) -> str:
        file = chr(96+self.file)
        rank = 9 - self.rank
        return f"{file}{rank}"
        
    def is_empty(self) -> bool:
        return self.piece is None

    def get_piece(self) -> Piece:
        return self.piece
    
    def set_piece(self, piece: Piece) -> None:
        self.piece = piece
        return self.piece

    def remove_piece(self) -> Piece:
        piece = self.piece
        self.piece = None
        return piece