import torch
from torch import nn
from sklearn.model_selection import train_test_split
import torchmetrics
import matplotlib.pyplot as plt
import random
import sys
sys.path.insert(0, '/home/malone/Code/pytorch-bourke')
from helper_functions import plot_decision_boundary

from lib.game import Game

RANDOM_SEED = 1
NUM_GENERATION = 10
NUM_MATCHES = 100
AI_PLAYER_ID = 1
NUM_EXPLORE = 5

def aiMove(game):
    # print("match", match)
    board = torch.Tensor(game.state.board).type(torch.float32)
    board = board.reshape(1, 9).squeeze()
    # print(board)
    move = model(board)
    print(move)
    # move = move.argmax() + 1
    # print("AI moves to", move)
    
    return move

def runMatch(game, X, y):
    model.eval()
    winner = game.runGame()
    # print("winner is player", winner)
    # print("\n",game.frames, "\n")

    if winner == AI_PLAYER_ID:
        # record the frames as the training set
        frames = torch.Tensor(game.frames)
        print("frames:", frames)
        # frames = frames.reshape(frames.shape[0], 9).squeeze()
        # print(f"state:\n{game.state.render()}")
        X = torch.cat((X, frames), dim=0)

        moves = torch.Tensor([moves]).reshape()
        print("moves: ", moves)
        # y = torch.cat((y, moves), dim=0)
        # print("y:", y)
        
    return X, y, winner

class TttModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_stack = nn.Sequential(
            nn.Linear(in_features=9, out_features=16),
            nn.ReLU(),
            nn.Linear(in_features=16, out_features=16),
            nn.ReLU(),
            nn.Linear(in_features=16, out_features=9),
        )
    def forward(self, x):
        return self.linear_stack(x)

random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)


# set up the NN
model = TttModel()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
        
# play and training loop
for generation in range(NUM_GENERATION):
    # Play loop
    winCount = 0
    X = torch.Tensor()
    y = torch.Tensor().type(torch.int32)
    if generation > NUM_EXPLORE - 1:
        # start out playing randomly until we have some data to work with
        player1 = aiMove
    else: 
        player1 = 'random'
    
    print("Generation", generation, ": player1:", player1)
    game = Game(player1, 'random', hideGameOutput=True, randomSeed=None)
    
    for match in range(NUM_MATCHES):
        X, y, winner = runMatch(game, X, y)
        if winner == AI_PLAYER_ID:
            winCount += 1
    
    print(f"Completed {match + 1} matches | AI won {winCount} matches | X size: {X.shape} | y size: {y.shape}")
    # print(X[:50])
    
    # Train and testing
    
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X,
    #     y,
    #     test_size=0.2,
    #     random_state=RANDOM_SEED)

    ## Training
    
    
    
    ## Testing


