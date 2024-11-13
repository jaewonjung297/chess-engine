from models.Pieces.King import King

def evaluate_board(board):
    piece_values = {
        'wp': 1,
        'wn': 3, 
        'wb': 3, 
        'wr': 5, 
        'wq': 9,
        'wk': 0,  

        'bp': -1, 
        'bn': -3, 
        'bb': -3, 
        'br': -5, 
        'bq': -9,  
        'bk': 0   
    }
    
    score = 0
    for row in board:
        for tile in row:
            if tile.is_empty():
                continue
            piece = tile.get_piece()
            if piece.to_string() in piece_values:
                score += piece_values[piece.to_string()]

    return score

def find_king(player):
    for row_index, row in enumerate(self.board):
        for col_index, tile in enumerate(row):
            if not tile.is_empty():
                piece = tile.get_piece()
                if type(piece) == King and piece.player == player:
                    return (row_index, col_index)
    return None
