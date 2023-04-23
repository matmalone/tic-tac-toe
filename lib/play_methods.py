from random import randint

def random_move(game):
    # get the open cells
    free = game.state.getFree()
    # pick one at random then return it
    idx = randint(0, len(free) - 1)
    pick = free[idx]
    return pick

class Sequential:
    def __init__(self):
        self.next_move = None
        self.reset()
    
    def get_move(self, game):
        if game.state.moves == 0: 
            self.reset()
        
        move = self.next_move
        self.next_move += 1
        return move
    
    def reset(self):
        self.next_move = 1
