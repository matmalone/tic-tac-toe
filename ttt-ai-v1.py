import torch
from torch import nn
from sklearn.model_selection import train_test_split
import torchmetrics
import matplotlib.pyplot as plt
import random
import math
import sys
sys.path.insert(0, '/home/malone/Code/pytorch-bourke')
from helper_functions import plot_decision_boundary

from lib.game import Game

RANDOM_SEED = 1
NUM_GENERATION = 2000
NUM_MATCHES = 100
AI_PLAYER_ID = 1
NUM_EXPLORE = math.floor(NUM_GENERATION / 2)

def aiMove(game):
    # print("match", match)
    board = torch.Tensor(game.state.board).type(torch.float32)
    # board = board.reshape(1, 9).squeeze()
    # print("aiMove() board:", board)
    move = model(board)
    # print("move:", move)
    move = move.argmax().item()
    # print("AI moves to", move)
    
    return move

def runMatch(game, X, y):
    model.eval()
    winner = game.runGame()
    # print("winner is player", winner)
    # print("\n",game.frames, "\n")

    if winner == AI_PLAYER_ID:
        # record the frames as the training set
        frames = torch.Tensor(game.p1Frames)
        # print("frames:", frames)
        # frames = frames.reshape(frames.shape[0], 9).squeeze()
        # print(f"state:\n{game.state.render()}")
        X = torch.cat((X, frames), dim=0)

        moves = game.p1Moves
        # print("list moves: ", moves)
        movesLen = len(moves)
        moves = torch.Tensor(moves).type(torch.LongTensor)
        # print("tensor moves1: ", moves)
        # moves = moves.reshape(movesLen, 1)
        # print("tensor moves2: ", moves)
        y = torch.cat((y, moves), dim=0)
        
    return X, y, winner

class TttModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_stack = nn.Sequential(
            nn.Linear(in_features=10, out_features=16),
            nn.ReLU(),
            nn.Linear(in_features=16, out_features=32),
            nn.ReLU(),
            nn.Linear(in_features=32, out_features=16),
            nn.ReLU(),
            nn.Linear(in_features=16, out_features=10),
        )
    def forward(self, x):
        return self.linear_stack(x)

random.seed(RANDOM_SEED)
torch.manual_seed(RANDOM_SEED)


# set up the NN
model = TttModel()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
calcAccuracy = torchmetrics.Accuracy(task="multiclass", num_classes=10)


# play and training loop
for generation in range(NUM_GENERATION):
    # Play loop
    model.eval()
    # print("model state:", model.state_dict())
    winCount = 0
    
    
    X = torch.Tensor()
    y = torch.Tensor().type(torch.LongTensor)
    if generation > NUM_EXPLORE - 1:
        # start out playing randomly until we have some data to work with
        player1 = aiMove
    else: 
        player1 = 'random'
    
    # print("Generation", generation, ": player1:", player1)
    game = Game(player1, 'random', hideGameOutput=True, randomSeed=None)
    
    
    for match in range(NUM_MATCHES):
        X, y, winner = runMatch(game, X, y)
        if winner == AI_PLAYER_ID:
            winCount += 1
    
    print(f"=== Completed {match + 1} matches | AI won {winCount} matches | X size: {X.shape} | y size: {y.shape}")
    # print(X[:50])
    
    if y.shape[0] < 1: 
        print("Zero AI wins, skipping training.")
        continue
    
    # Train and testing
    
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=RANDOM_SEED)
    
    # print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    ## Training
    model.train()
    y_logits = model(X_train)
    # print("y_logits:", y_logits[:5])
    y_preds = torch.argmax(y_logits, dim=1)
    # print("y_preds:", y_preds[:5])
    # print("y_train:", y_train[:5])
    
    loss = loss_fn(y_logits, y_train)
    accuracy = calcAccuracy(y_preds, y_train) * 100

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    ## Testing
    model.eval()
    with torch.inference_mode():
        test_logits = model(X_test)
        test_preds = torch.argmax(test_logits, dim=1)    
        test_loss = loss_fn(test_logits, y_test)
        test_accuracy = calcAccuracy(test_preds, y_test) * 100
    
    print(f"### generation: {generation} | loss: {loss:.4f} | accuracy: {accuracy:.4f}% | test_loss: {test_loss:.4f} | test_accuracy: {test_accuracy:.4f}%")
        

