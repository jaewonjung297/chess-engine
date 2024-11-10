from models.board.Board import Board
from models.board.Tile import Tile
from models.Pieces.Pawn import Pawn
from models.Pieces.King import King
from models.Pieces.Queen import Queen
from models.Pieces.Knight import Knight
from models.Pieces.Rook import Rook
from models.Pieces.Bishop import Bishop
import pygame


class Game():
    def __init__(self):
        self.board = Board()
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        self.run()
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                file = x // 100
                rank = 7 - (y // 100)
                self.process_click(file, rank)
        
    def process_click(self, file, rank):
        # Logic to process the click on the board
        print(f"Clicked on file: {file}, rank: {rank}")

    def run(self):
        while self.running:
            self.handle_input()
            self.update_screen()

    def update_screen(self):
        pass