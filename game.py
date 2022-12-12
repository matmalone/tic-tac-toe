from state import State

print("Welcome to tic-tac-toe")
state = State()
print(state)

state.print()
state.move(1, 0, 0)
state.print()