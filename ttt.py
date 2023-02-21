from lib.game import Game

print("Welcome to tic-tac-toe\n")


def aiMove(game):
    return (1, 1)


# Game(aiMove, 'random', hideGameOutput=False).runLoop(1)
Game('random', 'random', True).runLoop(1000)
