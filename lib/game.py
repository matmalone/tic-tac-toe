from lib.state import State
import random

class Game:
    def __init__(self, p1Method, p2Method, hideGameOutput=False):
        self.p1Method = p1Method
        self.p2Method = p2Method
        self.hideGameOutput = hideGameOutput

    def runLoop(self, cycles):
        """
        Run the game loop.
        
        cycles : int
            The number of cycles to loop for.
        """
        p1Wins = p2Wins = draws = 0
        for i in range(cycles):
            winner = self.runGame()
            if winner == 1: p1Wins += 1
            elif winner == 2: p2Wins += 1
            else: draws += 1
        print(f"Player 1 ({self.p1Method}) wins: {p1Wins}; ", 100 * p1Wins / cycles, "%")
        print(f"Player 2 ({self.p2Method}) wins: {p2Wins}; ", 100 * p2Wins / cycles, "%")
        print("Draws: ", draws, "; ", 100 * draws / cycles, "%")


    def runGame(self):
        """
        Run a single game of TTT.

        Returns:
        int: Which player won the game: 1, 2, or -1 on a draw.
        """
        self.state = State()
        # choose a starting player at random
        self.activePlayer = random.randint(1, 2)

        while True:
            self.print(self.state.render())
            move = self.getMove()
            self.state.move(self.activePlayer, move[0], move[1])

            # check to see if anyone won
            winner = self.state.getWinner()
            if (winner > 0): 
                self.print(f"!!!!!!! Player {winner} wins !!!!!!!")
                break
            elif (-1 == winner): 
                self.print("???????? Draw ????????")
                break

            # alternate players
            self.activePlayer %= 2
            self.activePlayer += 1
        # final display of the board
        self.print(self.state.render())
        return winner

    def getMove(self):
        if self.activePlayer == 1: method = self.p1Method
        else: method = self.p2Method
        func = getattr(self, method)
        return func()

    def prompt(self):
        s = input(f"Enter player {self.activePlayer}'s move in xy format: ")
        x,y = list(s)

        # bounds checking
        if (not (x >= "0" and x <= "2")): return False
        if (not (y >= "0" and y <= "2")): return False

        # convert from characters to integers
        x = int(x)
        y = int(y)
        return (x, y)

    def random(self):
        # get the open cells
        free = self.state.getFree()
        # pick one at random then return it
        idx = random.randint(0, len(free[0]) - 1)
        pick = (free[0][idx], free[1][idx])
        return pick

    def print(self, s):
        if self.hideGameOutput == False:
            print(s)




# state = State()
# print(state)

# state.print()
# # state.move(1, 1, 1)
# state.move(2, 0, 0)
# state.print()
# state.move(1, 0, 2)
# state.print()
# state.move(2, 1, 0)
# state.print()
# state.move(2, 2, 0)
# state.print()
# state.move(1, 1, 2)
# state.print()
# state.move(0, 2, 2)
# state.print()

# winner = state.getWinner()
# print(f"winner: {winner}")

