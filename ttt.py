from lib.game import Game

print("Welcome to tic-tac-toe\n")


def aiMove(game):
    return 5


# Game(aiMove, 'random', hideGameOutput=False).runLoop(1)
Game('prompt', 'random', hideGameOutput=False).runLoop(1)
# Game('random', 'random', hideGameOutput=True).runLoop(1000)
