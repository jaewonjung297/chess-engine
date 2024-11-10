from abc import ABC, abstractmethod
class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position
    
    @abstractmethod
    def valid_moves(self, board):
        pass
    
    @abstractmethod
    def move(self, new_position):
        pass

    def is_opponent_piece(self, other_piece):
        return other_piece.color != self.color
