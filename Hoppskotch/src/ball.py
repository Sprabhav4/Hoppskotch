import os
from const import *

class Ball():
    def __init__(self, texture = None, texture_rect = None):
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self):
        self.texture = BALL_80
