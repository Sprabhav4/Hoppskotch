import os
from const import *

class Knight():
    def __init__(self, color, texture = None, texture_rect = None):
        self.color = color
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        self.moves = []
        self.moved = False
    
    def set_texture(self, size = 80):
        if self.color == 'white':
            self.texture = KNIGHT_80W if size == 80 else KNIGHT_128W
        else:
            self.texture = KNIGHT_80B if size == 80 else KNIGHT_128B

    def add_moves(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []



        