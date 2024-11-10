
from models.board.Board import Board

board = Board()
print(board.board[1][7].get_piece().valid_moves(board.board))
board.print_board()