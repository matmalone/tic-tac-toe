import numpy as np

class State:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.moves = 0

    def print(self):
        print(f"Moves: {self.moves}")
        print(self.board)
        print()

    def move(self, player, x, y):
        self.board[x, y] = player
        self.moves += 1
