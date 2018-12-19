import chess.svg
import pygame


from IPython.display import SVG

WIDTH = 512
HEIGHT = 512

board = chess.Board("8/8/8/8/4N3/8/8/8 w - - 0 1")
squares = board.attacks(chess.E4)
a = SVG(chess.svg.board(board=board, squares=squares))

screen = pygame.display.set_mode([500, 500])


print(board)


