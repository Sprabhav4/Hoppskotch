class Square:

    def __init__(self, row, col, knight = None, ball = None, post = None):
        self.row = row
        self.col = col
        self.knight = knight
        self.ball = ball
        self.post = post

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def has_knight(self):
        return self.knight != None
    
    def has_ball(self):
        return self.ball != None
    
    def has_post(self):
        return self.post != None
    
    def is_empty(self):
        return (self.knight == None and self.ball == None and self.post == None) 
    
    def can_have_ball(self):
        return (self.knight == None and self.ball == None and self.post == None and self.row > 0 and self.row < 7 and self.col > 0 and self.col < 7)
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < 0 or arg > 7:
                return False  
        return True