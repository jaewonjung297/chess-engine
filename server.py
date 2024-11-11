from flask_cors import CORS
from flask import Flask, jsonify, request
from models.board.Board import Board
from flask_socketio import SocketIO
from helper import evaluate_board


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])
socketio = SocketIO(app, cors_allowed_origins="*")


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
    socketio.emit('board_update', board_data)
    return jsonify(board_data)

@app.route('/api/make-move', methods=['OPTIONS', 'POST'])
def make_move():
    if request.method == 'OPTIONS':
        return '', 200  # Respond to preflight request

    move_data = request.get_json()

    start_row = move_data['startRow']
    start_col = move_data['startCol']
    end_row = move_data['endRow']
    end_col = move_data['endCol']

    success, message = board.move_piece(start_row, start_col, end_row, end_col)

    if success:
        board_data = [
            [tile.get_piece().to_string() if not tile.is_empty() else 'X' for tile in row]
            for row in board.board
        ]
        socketio.emit('board_update', board_data)

    
    return jsonify({"success": success, "message": message})

@app.route('/api/reset-game', methods=['OPTIONS', 'POST'])
def reset_game():
    board.setup_board()
    board_data = [
        [tile.get_piece().to_string() if not tile.is_empty() else 'X' for tile in row]
        for row in board.board
    ]
    socketio.emit('board_update', board_data)
    return jsonify({"success": "success"})

@app.route('/api/evaluate', methods=['GET'])
def evaluate():
    score = evaluate_board(board.board)
    return jsonify({"success": "success", "score": score})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True)