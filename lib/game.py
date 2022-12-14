from lib.state import State

class Game:
    def __init__(self):
        self.state = State()
        self.activePlayer = 1

    def run(self):
        while True:
            print(self.state.render())
            move = self.prompt()
            self.state.move(self.activePlayer, move[0], move[1])

            # check to see if anyone won
            winner = self.state.getWinner()
            if (winner > 0): 
                print(f"!!!!!!! Player {winner} wins !!!!!!!")
                break
            elif (-1 == winner): 
                print("Draw")
                break

            # alternate players
            self.activePlayer %= 2
            self.activePlayer += 1
        # final display of the board
        print(self.state.render())
        return winner

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

