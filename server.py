import sys
import os
from flask import Flask, jsonify, request
from models.board.Board import Board


app = Flask(__name__)


board = Board()

@app.route('/', methods=['GET'])
def main():
    return 'Hello World'

@app.route('/api/board', methods=['GET'])
def get_board():
    board_data = [
        [tile.get_piece().to_string() if not tile.is_empty() else 'X' for tile in row]
        for row in board.board
    ]
    return jsonify(board_data)

def make_move():
    move_data = request.get_json()

    start_row = move_data['start_row']
    start_col = move_data['start_col']
    end_row = move_data['end_row']
    end_col = move_data['end_col']

    success = board.move_piece(start_row, start_col, end_row, end_col)
    
    return jsonify({"success": success})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
