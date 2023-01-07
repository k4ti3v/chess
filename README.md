# chess
A human-like bot for chess.com

The script uses the maia library to connect to Chess.com with the specified login credentials. It then enters a loop where it waits for a new game to start using the maia.wait_for_game() function.

When a new game is found, the script selects either the best move or an additional move for the current position, as specified by the user. The selected move is then made using the maia.make_move() function, with a random delay added to simulate a human player.

The script then continues to wait for the next game to start, and the process repeats. This continues indefinitely, until the script is interrupted or terminated.


Future updates:

Use a thread to run the maia.wait_for_game() function in the background, so that the script can do other things while waiting for a new game to start.

Use a timer to control the frequency at which the script checks for new games, rather than running the maia.wait_for_game() function in a continuous loop.

Use a cache to store the best moves and additional moves for each game, rather than calculating them on the fly. This will reduce the number of API calls and improve the performance of the script.

Consider using a different chess engine to calculate the best moves and additional moves. Some engines may be faster or more accurate than the one used by the maia library.
