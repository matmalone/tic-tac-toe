from .state import State
import random
import copy

class Game:
    def __init__(self, p1Method, p2Method, hideGameOutput=False, randomSeed=None):
        self.p1Method = p1Method
        self.p2Method = p2Method
        self.hideGameOutput = hideGameOutput
        self.p1Frames = []
        self.p2Frames = []
        self.p1Moves = []
        self.p2Moves = []
        
        if randomSeed:
            random.seed(randomSeed)

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
        self.p1Frames = []
        self.p2Frames = []
        self.p1Moves = []
        self.p2Moves = []

        # choose a starting player at random
        self.activePlayer = random.randint(1, 2)

        while True:
            self.print(self.state.render())

            # record the old state for analysis later
            if self.activePlayer == 1:
                self.p1Frames.append(copy.copy(self.state.board))
            if self.activePlayer == 2:
                self.p2Frames.append(copy.copy(self.state.board))

            move = self.getMove()
            # print(f"Player {self.activePlayer} moves to {move}")
            success = self.state.move(self.activePlayer, move)
            if not success:
                self.print(f"??? Player {self.activePlayer} made an invalid move ???")

            # save the move for analysis later
            if self.activePlayer == 1:
                self.p1Moves.append(move)
            else:
                self.p2Moves.append(move)

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
        
        # if the method was a callback function, use that to call and pass a reference to the game
        if callable(method):
            func = method
            return func(self)
        else:
            # otherwise get the object's method to call
            func = getattr(self, method)
            return func()

    def keyToXy(self, key):
        key = int(key)
        match key:
            case 1:
                return (0, 0)
            case 2:
                return (1, 0)
            case 3:
                return (2, 0)
            case 4:
                return (1, 0)
            case 5:
                return (1, 1)
            case 6:
                return (1, 2)
            case 7:
                return (2, 0)
            case 8:
                return (2, 1)
            case 9:
                return (2, 2)
        return False

    def xyToKey(self, xy):
        if xy == (0,0): return 1
        if xy == (1,0): return 2
        if xy == (2,0): return 3
        if xy == (0,1): return 4
        if xy == (1,1): return 5
        if xy == (2,1): return 6
        if xy == (0,2): return 7
        if xy == (1,2): return 8
        if xy == (2,2): return 9
        return False


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

