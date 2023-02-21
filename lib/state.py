import numpy as np

class State:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=np.int8)
        self.moves = 0
        self.disqualifiedPlayer = None

    def render(self):
        # print(self.board)
        s = ""
        for y in range(2, -1, -1):
            s += "[ "
            for x in range(0, 3):
                val = self.board[x, y]
                if val == 0: symbol = " "
                else: symbol = val
                s += f"{symbol} "
            s += "]\n"

        s += f"Moves: {self.moves}\n"
        return s

    def move(self, player, x, y):
        if self.board[x, y] > 0:
            # don't allow a player to stomp on another player
            self.disqualifiedPlayer = player
            return False
        
        self.board[x, y] = player
        self.moves += 1
        return True

    def getWinner(self):
        # check to see if a player was disqualified
        if self.disqualifiedPlayer:
            # if someone was disqualified, it's the opposite player
            return 2 - (1 % self.disqualifiedPlayer)
        
        # check player 1
        p1 = [1, 1, 1]
        if (np.array_equal(self.board[:,0], p1)): return 1
        if (np.array_equal(self.board[:,1], p1)): return 1
        if (np.array_equal(self.board[:,2], p1)): return 1
        if (np.array_equal(self.board[0,:], p1)): return 1
        if (np.array_equal(self.board[1,:], p1)): return 1
        if (np.array_equal(self.board[2,:], p1)): return 1
        if (np.array_equal(np.diagonal(self.board), p1)): return 1

        # check player 2
        p2 = [2, 2, 2]
        if (np.array_equal(self.board[:,0], p2)): return 2
        if (np.array_equal(self.board[:,1], p2)): return 2
        if (np.array_equal(self.board[:,2], p2)): return 2
        if (np.array_equal(self.board[0,:], p2)): return 2
        if (np.array_equal(self.board[1,:], p2)): return 2
        if (np.array_equal(self.board[2,:], p2)): return 2
        if (np.array_equal(np.diagonal(self.board), p2)): return 2

        # check for a draw
        if (self.moves >= 9): return -1

        return 0
        
    def getFree(self):
        return np.where(self.board == 0)
