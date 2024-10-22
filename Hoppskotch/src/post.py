import os
from const import *

class Post():
    def __init__(self, color, texture = None, texture_rect = None):
        self.color = color
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self):
        self.texture = POST_80W if self.color == 'white' else POST_80B
