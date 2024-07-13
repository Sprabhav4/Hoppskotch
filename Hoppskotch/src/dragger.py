import pygame
from const import *

class Dragger:

    def __init__(self):
        self.knight = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initialRow = 0
        self.initialCol = 0

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initialRow = pos[1] // SQSIZE
        self.initialCol = pos[0] // SQSIZE  

    def drag_knight(self, knight):
        self.knight = knight
        self.dragging = True

    def undrag_knight(self):
        self.knight = None
        self.dragging = False

    def update_blit(self, surface):
        self.knight.set_texture(size = 128)
        texture = self.knight.texture
        img = pygame.image.load(texture)
        img_center = (self.mouseX, self.mouseY)
        self.knight.texture_rect = img.get_rect(center = img_center)
        surface.blit(img, self.knight.texture_rect)
    

        