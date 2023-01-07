# chess
A human-like bot for chess.com

The script uses the maia library to connect to Chess.com with the specified login credentials. It then enters a loop where it waits for a new game to start using the maia.wait_for_game() function.

When a new game is found, the script selects either the best move or an additional move for the current position, as specified by the user. The selected move is then made using the maia.make_move() function, with a random delay added to simulate a human player.

The script then continues to wait for the next game to start, and the process repeats. This continues indefinitely, until the script is interrupted or terminated.
