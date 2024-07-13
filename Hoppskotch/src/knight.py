import os

class Knight():
    def __init__(self, color, texture = None, texture_rect = None):
        self.color = color
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        self.moves = []
        self.moved = False
    
    def set_texture(self, size = 80):
        self.texture = os.path.join(f'assets/images/imgs-{size}px/{self.color}_knight.png')

    def add_moves(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []



        