import pygame
import sys
from const import *
from game import Game
from dragger import Dragger
from square import Square
from move import Move

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Hoppskotch')
        self.game = Game()

    def mainLoop(self):

        game = self.game
        screen = self.screen
        dragger = game.dragger
        board = game.board

        while True:
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_hover(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)             

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    if board.squares[clicked_row][clicked_col].has_knight():
                        knight = board.squares[clicked_row][clicked_col].knight
                        if knight.color == game.next_player:
                            board.calc_moves(knight, clicked_row, clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_knight(knight)
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)

                #hold
                elif event.type == pygame.MOUSEMOTION:
                    
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE
                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        currRow = dragger.mouseY // SQSIZE
                        currCol = dragger.mouseX // SQSIZE


                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_hover(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)

                #release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        initial = Square(dragger.initialRow, dragger.initialCol)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        """
                        ballAt = board.checkForBall(final)

                        if ballAt != None:
                            ball = ballAt.ball
                            lastAt = ballAt
                            rowDiff = final.row - lastAt.row
                            colDiff = final.col - lastAt.col
                            moveTo = Square(final.row - (2 * rowDiff), final.col - (2 * colDiff))
                            
                            if moveTo.can_have_ball == False:
                                if rowDiff == 0 or colDiff == 0:
                                    pass
                                else:
                        """



                        if board.valid_move(dragger.knight, move):
                            board.move(dragger.knight, move) 
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)
                            game.next_turn()

                    dragger.undrag_knight()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.mainLoop()