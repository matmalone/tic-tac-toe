class State:
    def __init__(self):
        self.board = [0] * 10
        self.board[0] = -1
        self.moves = 0
        self.disqualifiedPlayer = None

    def render(self):
        # print(self.board)
        s = ""
        s += f"[ {self.board[7]} {self.board[8]} {self.board[9]} ]\n"
        s += f"[ {self.board[4]} {self.board[5]} {self.board[6]} ]\n"
        s += f"[ {self.board[1]} {self.board[2]} {self.board[3]} ]\n"
        s += f"Moves: {self.moves}\n"
        return s

    def move(self, player, pos):
        if self.board[pos] != 0:
            # don't allow a player to stomp on another player
            self.disqualifiedPlayer = player
            return False
        
        self.board[pos] = player
        self.moves += 1
        return True

    def getWinner(self):
        # check to see if a player was disqualified
        if self.disqualifiedPlayer:
            # if someone was disqualified, it's the opposite player
            return 2 - (1 % self.disqualifiedPlayer)
        
        # check player 1
        if self.board[7] == 1 and self.board[8] == 1 and self.board[9] == 1: return 1
        if self.board[4] == 1 and self.board[5] == 1 and self.board[6] == 1: return 1
        if self.board[1] == 1 and self.board[2] == 1 and self.board[3] == 1: return 1
        if self.board[1] == 1 and self.board[4] == 1 and self.board[7] == 1: return 1
        if self.board[2] == 1 and self.board[5] == 1 and self.board[8] == 1: return 1
        if self.board[3] == 1 and self.board[6] == 1 and self.board[9] == 1: return 1
        if self.board[1] == 1 and self.board[5] == 1 and self.board[9] == 1: return 1
        if self.board[3] == 1 and self.board[5] == 1 and self.board[7] == 1: return 1
        
        # check player 2
        if self.board[7] == 2 and self.board[8] == 2 and self.board[9] == 2: return 2
        if self.board[4] == 2 and self.board[5] == 2 and self.board[6] == 2: return 2
        if self.board[1] == 2 and self.board[2] == 2 and self.board[3] == 2: return 2
        if self.board[1] == 2 and self.board[4] == 2 and self.board[7] == 2: return 2
        if self.board[2] == 2 and self.board[5] == 2 and self.board[8] == 2: return 2
        if self.board[3] == 2 and self.board[6] == 2 and self.board[9] == 2: return 2
        if self.board[1] == 2 and self.board[5] == 2 and self.board[9] == 2: return 2
        if self.board[3] == 2 and self.board[5] == 2 and self.board[7] == 2: return 2
        
        # check for a draw
        if (self.moves >= 9): return -1

        return 0
        
    def getFree(self):
        return [i for i, e in enumerate(self.board) if e == 0]



