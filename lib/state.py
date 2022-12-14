import numpy as np

class State:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=np.int8)
        self.moves = 0

    def print(self):
        # print(self.board)
        for y in range(2, -1, -1):
            print("[ ", end="")
            for x in range(0, 3):
                print(f"{self.board[x, y]} ", end="")
            print("]")


        print(f"Moves: {self.moves}")
        print()

    def move(self, player, x, y):
        self.board[x, y] = player
        self.moves += 1
        winner = self.getWinner()
        if (winner > 0): print(f"!!!!!!! Player {winner} wins !!!!!!!")
        elif (-1 == winner): print("Draw")

    def getWinner(self):
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
        
