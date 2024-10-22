import pygame
from const import *
from board import Board
from dragger import Dragger

class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()
        self.next_player = 'white'
        self.hovered = None

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if((row + col) % 2 == 0):
                    color = (234, 235, 200)
                else:
                    color = (119, 154, 88)

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):

                if self.board.squares[row][col].has_knight():
                    knight = self.board.squares[row][col].knight

                    if knight is not self.dragger.knight:
                        knight.set_texture(size = 80)
                        img = pygame.image.load(knight.texture)
                        img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                        knight.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, knight.texture_rect)

                if self.board.squares[row][col].has_ball():
                    ball = self.board.squares[row][col].ball
                    img = pygame.image.load(ball.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    ball.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, ball.texture_rect)

                if self.board.squares[row][col].has_post():
                    post = self.board.squares[row][col].post
                    img = pygame.image.load(post.texture)
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
                    post.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, post.texture_rect)

    def show_moves(self, surface):
        if(self.dragger.dragging):
            knight = self.dragger.knight
            for move in knight.moves:
                #For ball'#00cdff'
                color = '#C84646'
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):
        if(self.board.last_move):
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                color = (172,195,51)
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)

        '''
        if(self.board.last_ball_move):
            initial = self.board.last_ball_move.initial
            final = self.board.last_ball_move.final

            for pos in [initial, final]:
                color = (44,43,41)
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(surface, color, rect)
        '''

    def show_hover(self, surface):
        if self.hovered:
            color = (180,180,180)
            rect = (self.hovered.col * SQSIZE, self.hovered.row * SQSIZE, SQSIZE, SQSIZE)
            pygame.draw.rect(surface, color, rect)

    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self, row, col):
        self.hovered = self.board.squares[row][col]