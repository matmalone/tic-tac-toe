class Node:
    def __init__(self, game, args, state, parent=None, action_taken=None):
        self.game = game
        self.args = args
        self.state = state
        self.parent = parent
        self.action_take = action_taken
        
        self.children = []
        self.expandable_moves = game.get_valid_moves()
        
        self.visit_count = 0
        self.value_sum = 0
    
    def is_fully_expanded(self):
        return sum(self.expandable_moves) == 0 and len(self.children) > 0

    def select(self):
        best_child = None
        best_ucb = float('-inf')
        
        for child in self.children:
            ucb = self.get_ucb(child)
            if ucb > best_ucb:
                best_child = child
                best_ucb = ucb
            
        return best_child
    
    def get_ucb(self, child):
        q_value = ((child.value_sum / child.visit_count) + 1 ) / 2.
        
class Mcts:
    def __init__(self, game, args):
        self.game = game
        self.args = args
        
    def search(self, state):
        # define root
        root = Node(self.game, self.args, state)
        
        for search in range(self.args['num_searches']):
            node = root
            
            # selection
            while node.is_fully_expanded():
                node = node.select()
            
            
            # expansion
            # simulatino
            # back prop
        
        # return visit counts
        