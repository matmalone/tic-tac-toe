from state import State

print("Welcome to tic-tac-toe")
state = State()
print(state)

state.print()
# state.move(1, 1, 1)
state.move(2, 0, 0)
state.print()
state.move(1, 0, 2)
state.print()
state.move(2, 1, 0)
state.print()
state.move(2, 2, 0)
state.print()
state.move(1, 1, 2)
state.print()
state.move(0, 2, 2)
state.print()

winner = state.getWinner()
print(f"winner: {winner}")
