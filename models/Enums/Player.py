from enum import Enum

class Player(Enum):
    WHITE = 0
    BLACK = 1

    def opponent(self):
        return Player.BLACK if self == Player.WHITE else Player.WHITE