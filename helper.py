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