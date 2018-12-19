import chess.svg
import pygame


from IPython.display import SVG

WIDTH = 512
HEIGHT = 512

board = chess.Board()
'''squares = board.attacks(chess.E4)'''
a = SVG(chess.svg.board(board=board))

screen = pygame.display.set_mode([500, 500])

print(board)



