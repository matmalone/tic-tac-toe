from lib.state import State

class Game:
    def __init__(self):
        self.state = State()
        self.activePlayer = 1

    def run(self):
        while True:
            self.state.print()
            move = self.prompt()
            self.state.move(self.activePlayer, move[0], move[1])

            # alternate players
            self.activePlayer %= 2
            self.activePlayer += 1

    def prompt(self):
        s = input(f"Enter player {self.activePlayer}'s move in xy format: ")
        xy = list(s)
        x = int(xy[0])
        y = int(xy[1])

        return (x,y)


print("Welcome to tic-tac-toe")

Game().run()

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

