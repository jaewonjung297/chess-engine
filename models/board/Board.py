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
        self.board = [[Tile(row + 1, col + 1) for row in range(8)] for col in range(8)]
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

    def move_piece(self, current_player, start_row, start_col, end_row, end_col):
        start_tile = self.board[start_row][start_col]
        end_tile = self.board[end_row][end_col]

        if start_tile.is_empty():
            return False, "No piece at the starting position"
        
        piece = start_tile.get_piece()
        piece.valid_moves(self.board)

        if (end_row, end_col) not in piece.valid_moves(self.board):
            return False, "Invalid move!"

        #simulate move. if your king is still in check, then you can't make that move.
        current_king = self.find_king(current_player)
        if current_king.is_in_check(self.board):
            #store the current state
            start_piece = start_tile.get_piece()
            end_piece = end_tile.get_piece()
            #move pieces
            start_tile.remove_piece()
            end_tile.set_piece(piece)
            piece.move_piece(end_row, end_col)
            #if king still in check, invalid move
            if current_king.is_in_check(self.board):
                start_tile.set_piece(start_piece)
                end_tile.set_piece(end_piece)
                piece.move_piece(start_row, start_col)
                print("still in check")
                return False, "King is in check"
            else:
                return True, "Success"
        #at this point, remove piece from start and replace end piece with start piece
        start_tile.remove_piece()
        end_tile.set_piece(piece)
        piece.move_piece(end_row, end_col)
        opponent = Player.BLACK if current_player == Player.WHITE else Player.WHITE

        return True, "Success"


    def print_board(self):
        for row in self.board:
            row_string = ' '.join(
                [tile.get_piece().to_string() if not tile.is_empty() else "X" for tile in row]
            )
            print(row_string)

    def find_king(self, player):
        for row in self.board:
            for tile in row:
                if not tile.is_empty():
                    piece = tile.get_piece()
                    if type(piece) == King and piece.player == player:
                        return piece

    def is_checkmate(self, current_player):
        king = self.find_king(current_player)

        if not king.is_in_check(self.board):
            return False

        player_pieces = []
        for row in self.board:
            for tile in row:
                if not tile.is_empty() and tile.get_piece().player == current_player:
                    player_pieces.append(tile.get_piece())

        for piece in player_pieces:
            valid_moves = piece.valid_moves(self.board)

            for move in valid_moves:
                start_row, start_col = piece.row, piece.col
                end_row, end_col = move

                original_target_piece = self.board[end_row][end_col].get_piece()
                self.board[end_row][end_col].set_piece(piece)
                self.board[start_row][start_col].remove_piece()
                piece.move_piece(end_row, end_col)

                if not king.is_in_check(self.board):
                    piece.move_piece(start_row, start_col)
                    self.board[start_row][start_col].set_piece(piece)
                    self.board[end_row][end_col].set_piece(original_target_piece)
                    print(f"this must have triggered. start: f{start_row, start_col}, end: f{end_row, end_col}")
                    return False

                piece.move_piece(start_row, start_col)
                self.board[start_row][start_col].set_piece(piece)
                self.board[end_row][end_col].set_piece(original_target_piece)

        return True
