from lib.game import Game

print("Welcome to tic-tac-toe\n")

# Game('prompt', 'random', hideGameOutput=False).runLoop(1)
Game('random', 'random', True).runLoop(1000)
