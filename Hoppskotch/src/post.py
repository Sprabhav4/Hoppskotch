import os

class Post():
    def __init__(self, color, texture = None, texture_rect = None):
        self.color = color
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size = 80):
        self.texture = os.path.join(f'assets/images/imgs-{size}px/{self.color}_rook.png')
