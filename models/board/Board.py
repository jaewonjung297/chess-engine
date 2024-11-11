from models.Pieces.Pawn import Pawn
from models.Pieces.King import King
from models.Pieces.Queen import Queen
from models.Pieces.Knight import Knight
from models.Pieces.Rook import Rook
from models.Pieces.Bishop import Bishop

from models.board.Tile import Tile
from models.Enums.Player import Player

class Board():
    def __init__(self):
        self.board = [[Tile(row + 1, col + 1) for row in range(8)] for col in range(8)]
        self.setup_board()

    def setup_board(self):
        # Pawns
        for i in range(8):
            self.board[1][i].set_piece(Pawn(1, i, Player.BLACK))
            self.board[6][i].set_piece(Pawn(6, i, Player.WHITE))

        # Rooks
        self.board[0][0].set_piece(Rook(0, 0, Player.BLACK))
        self.board[0][7].set_piece(Rook(0, 7, Player.BLACK))
        self.board[7][0].set_piece(Rook(7, 0, Player.WHITE))
        self.board[7][7].set_piece(Rook(7, 7, Player.WHITE))

        # Knights
        self.board[0][1].set_piece(Knight(0, 1, Player.BLACK))
        self.board[0][6].set_piece(Knight(0, 6, Player.BLACK))
        self.board[7][1].set_piece(Knight(7, 1, Player.WHITE))
        self.board[7][6].set_piece(Knight(7, 6, Player.WHITE))

        # Bishops
        self.board[0][2].set_piece(Bishop(0, 2, Player.BLACK))
        self.board[0][5].set_piece(Bishop(0, 5, Player.BLACK))
        self.board[7][2].set_piece(Bishop(7, 2, Player.WHITE))
        self.board[7][5].set_piece(Bishop(7, 5, Player.WHITE))

        # Queens
        self.board[0][3].set_piece(Queen(0, 3, Player.BLACK))
        self.board[7][3].set_piece(Queen(7, 3, Player.WHITE))

        # Kings
        self.board[0][4].set_piece(King(0, 4, Player.BLACK))
        self.board[7][4].set_piece(King(7, 4, Player.WHITE))

        
        return self.board

    def move_piece(self, start_row, start_col, end_row, end_col) -> bool:
        start_tile = self.board[start_row][start_col]
        end_tile = self.board[end_row][end_col]

        if start_tile.is_empty():
            print("No piece at the starting position")
        
        piece = start_tile.get_piece()

        if (end_row, end_col) not in piece.valid_moves(self.board):
            print("Invalid move!")
            return False
        
        #at this point, remove piece from start and replace end piece with start piece
        start_tile.remove_piece()
        end_tile.set_piece(piece)

        return True


    def print_board(self):
        for row in self.board:
            # Use a list comprehension with a conditional expression
            row_string = ' '.join(
                [tile.get_piece().to_string() if not tile.is_empty() else "X" for tile in row]
            )
            print(row_string)
