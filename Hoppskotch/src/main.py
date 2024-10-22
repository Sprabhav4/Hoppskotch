import pygame
import sys
import pyautogui 
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

                #hold
                elif event.type == pygame.MOUSEMOTION:
                    
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE
                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        currRow = dragger.mouseY // SQSIZE
                        currCol = dragger.mouseX // SQSIZE

                #release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        initial = Square(dragger.initialRow, dragger.initialCol)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        if board.valid_move(dragger.knight, move) and final.is_empty():
                            ballPos = Square(final.row, final.col)
                            initialBallPos = ballPos
                            ballFound = False

                            possiblePositions = [
                                (released_row - 1, released_col - 1),
                                (released_row - 1, released_col),
                                (released_row - 1, released_col + 1),
                                (released_row, released_col - 1),
                                (released_row, released_col + 1),
                                (released_row + 1, released_col - 1),
                                (released_row + 1, released_col),
                                (released_row + 1, released_col + 1),
                            ]

                            for possible_pos in possiblePositions:
                                possible_pos_row, possible_pos_col = possible_pos
                                if 0 <= possible_pos_row <= 7 and 0 <= possible_pos_col <= 7 and board.squares[possible_pos_row][possible_pos_col].has_ball():
                                    ballFound = True
                                    initialBallPos = Square(possible_pos_row, possible_pos_col)
                                    ballPos = Square(possible_pos_row, possible_pos_col)
                                    break

                            if ballFound:

                                dr, dc = ballPos.row - final.row, ballPos.col - final.col
                                if max(abs(dr), abs(dc)) == 1:
                                    ballPos.row += dr
                                    ballPos.col += dc
                                    while board.squares[ballPos.row][ballPos.col].has_knight() or board.squares[ballPos.row][ballPos.col].has_post() or ballPos.col in (0, 7) or (ballPos.row == 0 and (ballPos.col < board.whiteGoal[0] or ballPos.col > board.whiteGoal[1])) or (ballPos.row == 7 and (ballPos.col < board.blackGoal[0] or ballPos.col > board.blackGoal[1])):
                                        if board.squares[ballPos.row][ballPos.col].has_knight() or board.squares[ballPos.row][ballPos.col].has_post():
                                            dr, dc = -dr, -dc
                                        else:
                                            if ballPos.row in (0, 7):
                                                dr = -dr
                                            if ballPos.col in (0, 7):
                                                dc = -dc
                                        ballPos.row += dr
                                        ballPos.col += dc
                                    

                            if ballFound and ballPos != initialBallPos:

                                ballMove = Move(initialBallPos, ballPos)
                                board.move_ball(ballMove)

                                if ballPos.row == 0 and (ballPos.col > board.blackGoal[0] and ballPos.col < board.blackGoal[1]):
                                    pyautogui.alert('White Wins!!')
                                    pygame.quit()
                                    sys.exit()
                                elif ballPos.row == 7 and (ballPos.col > board.whiteGoal[0] and ballPos.col < board.whiteGoal[1]):
                                    pyautogui.alert('Black Wins!!')
                                    pygame.quit()
                                    sys.exit()

                            
                            board.move(dragger.knight, move)
                            
                            #Expand Goalpost
                            if move.final.row == 0:

                                if move.final.col == board.blackGoal[0] + 1 and board.blackGoal[0] != 0 and not board.squares[0][board.blackGoal[0] - 1].has_knight():
                                    initialPost = board.squares[0][board.blackGoal[0]]
                                    postPost = board.squares[0][board.blackGoal[0] - 1]
                                    rook_move = Move(initialPost, postPost)
                                    board.blackGoal[0] -= 1
                                    board.move_post(rook_move, initialPost.post)

                                elif move.final.col == board.blackGoal[1] - 1 and board.blackGoal[1] != 7 and not board.squares[0][board.blackGoal[1] + 1].has_knight():
                                    initialPost = board.squares[0][board.blackGoal[1]]
                                    postPost = board.squares[0][board.blackGoal[1] + 1]
                                    rook_move = Move(initialPost, postPost)
                                    board.blackGoal[1] += 1
                                    board.move_post(rook_move, initialPost.post)

                            if move.final.row == 7:

                                if move.final.col == board.whiteGoal[0] + 1 and board.whiteGoal[0] != 0 and not board.squares[7][board.whiteGoal[0] - 1].has_knight():
                                    initialPost = board.squares[7][board.whiteGoal[0]]
                                    postPost = board.squares[7][board.whiteGoal[0] - 1]
                                    rook_move = Move(initialPost, postPost)
                                    board.whiteGoal[0] -= 1
                                    board.move_post(rook_move, initialPost.post)

                                elif move.final.col == board.whiteGoal[1] - 1 and board.whiteGoal[1] != 7 and not board.squares[7][board.whiteGoal[1] + 1].has_knight():
                                    initialPost = board.squares[7][board.whiteGoal[1]]
                                    postPost = board.squares[7][board.whiteGoal[1] + 1]
                                    rook_move = Move(initialPost, postPost)
                                    board.whiteGoal[1] += 1
                                    board.move_post(rook_move, initialPost.post)

                            game.next_turn()

                    dragger.undrag_knight()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

main = Main()
main.mainLoop()