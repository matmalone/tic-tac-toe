#!python3
from lib.game import Game
from lib import play_methods

p1_method = play_methods.random_move
p2_method = play_methods.random_move
num_cycles = 100
hide_game_output = False
random_seed = None

print("Welcome to tic-tac-toe\n")




# Game(aiMove, 'random', hideGameOutput=False).runLoop(1)
Game(
    p1Method=p1_method, 
    p2Method=p2_method,
    hideGameOutput=hide_game_output,
    randomSeed=random_seed,
    ).runLoop(num_cycles)
# Game('random', 'random', hideGameOutput=True).runLoop(1000)
