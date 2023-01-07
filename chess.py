import random
import time

import maia
from maia import Maia

# Replace YOUR_USERNAME and YOUR_PASSWORD with your Chess.com login credentials
maia = Maia(username='YOUR_USERNAME', password='YOUR_PASSWORD')

# Connect to Chess.com
maia.connect()

# Select a random delay between 1 and 5 seconds for each move
random_delay = random.randint(1, 5)

# Function to make a move
def make_move(move):
    time.sleep(random_delay)
    maia.make_move(move)

# Function to select between the best move and an additional move
def select_move(best_move, additional_move):
    if random.randint(0, 1) == 0:
        return best_move
    else:
        return additional_move

while True:
    # Wait for a new game to start
    game = maia.wait_for_game()

    # Make the best move or an additional move, as selected by the user
    move = select_move(game.best_move, game.additional_move)
    make_move(move)
