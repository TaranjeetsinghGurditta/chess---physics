import numpy as np
import matplotlib.pyplot as plt 
import chess    
import seaborn as sns

def calculate_phase_space(board_fen):
    board = chess.Board(board_fen)
    control_matrix = np.zeros((8, 8))
#this is like working as gravitational well, the more pieces you have in the center the more control you have over the board
    center_weights = np.array([
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        [1.0, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.0],
        [1.0, 1.1, 1.2, 1.2, 1.2, 1.2, 1.1, 1.0],
        [1.0, 1.1, 1.2, 1.5, 1.5, 1.2, 1.1, 1.0],
        [1.0, 1.1, 1.2, 1.5, 1.5, 1.2, 1.1, 1.0],
        [1.0, 1.1, 1.2, 1.2, 1.2, 1.2, 1.1, 1.0],
        [1.0, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.0],
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    ])

    for square in chess.SQUARES:
        row = 7 - chess.square_rank(square)  # Invert row for matrix representation
        col = chess.square_file(square)

        white_attackers = len(board.attackers(chess.WHITE, square))
        black_attackers = len(board.attackers(chess.BLACK, square))

        net_control = (white_attackers - black_attackers) * center_weights[row, col]
        control_matrix[row, col] = net_control
    return control_matrix

# using the Najdorf Sicilian Defense as an example 
#3 different positions other than this which we will be using to compare the heatmaps of control on the board
#"4kb1r/p2n1ppp/4q3/4p1B1/4P3/1Q6/PPP2PPP/2KR4 w k - 1 14"
#"rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
#"8/p3k3/8/2pP4/2P5/8/P3K3/8 w - - 0 1"
# "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq - 0 6"

fen_najdorf = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
matrix = calculate_phase_space(fen_najdorf)

# Visualize the phase space control matrix
plt.figure(figsize=(8, 8))
sns.heatmap(matrix, cmap="RdBu_r", center=0, annot=True, fmt=".1f", vmin=-6, vmax=6,
            cbar_kws={'label': 'Net Control (White + / Black -)'})

plt.title("Chess Board Phase Space: Potential Energy & Control")
plt.xticks(np.arange(8) + 0.5, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
plt.yticks(np.arange(8) + 0.5, ['8', '7', '6', '5', '4', '3', '2', '1'], rotation=0)

plt.tight_layout()
plt.show()




#for all 4 positions, we can create a single figure with 4 subplots, each showing the heatmap for one of the positions. This allows for easy comparison of control across different stages of the game.


