from const import *
from square import *
from knight import *
from ball import *
from post import *
from move import Move

class Board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range(COLS)]
        self.last_move = None
        self._create()
        self._add_pieces()
    
    def _create(self):
        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)


    def _add_pieces(self):
        self.squares[0][0] = Square(0,0,Knight('black'), None, None)
        self.squares[0][7] = Square(0,7,Knight('black'), None, None)
        self.squares[7][0] = Square(7,0,Knight('white'), None, None)
        self.squares[7][7] = Square(7,7,Knight('white'), None, None)

        self.squares[0][2] = Square(0,2, None, None, Post('black'))
        self.squares[0][5] = Square(0,5, None, None,Post('black'))
        self.squares[7][2] = Square(7,2, None, None,Post('white'))
        self.squares[7][5] = Square(7,5, None, None,Post('white'))

        self.squares[3][3] = Square(3,3, None, Ball(), None)

    def calc_moves(self, knight, row, col):
            
            possibleMoves = [
                (row - 2, col + 1),
                (row - 2, col - 1),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col + 2),
                (row + 1, col - 2),
                (row - 1, col + 2),
                (row - 1, col - 2),
            ]

            for possible_move in possibleMoves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].is_empty():
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        knight.add_moves(move)

    
    def move_ball(self, ball, ball_move):
        inital = ball_move.initial
        final = ball_move.final

        self.squares[inital.row][inital.col].ball = None
        self.squares[final.row][final.col].ball = ball

        ball.clear_moves()
        self.last_ball_move = ball_move

    def checkForBall(self, sq):
        row = sq.row
        col = sq.col
        possiblePositions = [
                (row - 1, col - 1),
                (row - 1, col),
                (row - 1, col + 1),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col - 1),
                (row + 1, col),
                (row + 1, col + 1),
            ]
        for possible_pos in possiblePositions:
                possible_pos_row, possible_pos_col = possible_pos
                if self.squares[possible_pos_row][possible_pos_col].ball != None:
                    return self.squares[possible_pos_row][possible_pos_col]
                else:
                    return None

    def move(self, knight, move):
        inital = move.initial
        final = move.final

        self.squares[inital.row][inital.col].knight = None
        self.squares[final.row][final.col].knight = knight

        knight.clear_moves()
        self.last_move = move

    def valid_move(self, knight, move):
        return move in knight.moves
        