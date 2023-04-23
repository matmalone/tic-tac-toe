from random import randint

def random_move(game):
    # get the open cells
    free = game.state.getFree()
    # pick one at random then return it
    idx = randint(0, len(free) - 1)
    pick = free[idx]
    return pick

