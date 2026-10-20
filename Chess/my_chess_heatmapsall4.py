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
        row = 7 - chess.square_rank(square)  
        col = chess.square_file(square)

        white_attackers = len(board.attackers(chess.WHITE, square))
        black_attackers = len(board.attackers(chess.BLACK, square))

        net_control = (white_attackers - black_attackers) * center_weights[row, col]
        control_matrix[row, col] = net_control
    return control_matrix

# The four positions we want to compare (name: FEN)
positions = {
    "Najdorf Sicilian": "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq - 0 6",
    "Starting Position": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
    "Opera Game (Midgame)": "4kb1r/p2n1ppp/4q3/4p1B1/4P3/1Q6/PPP2PPP/2KR4 w k - 1 14",
    "Bare Endgame": "8/p3k3/8/2pP4/2P5/8/P3K3/8 w - - 0 1",
}

fig, axes = plt.subplots(2, 2, figsize=(15, 13))
cbar_ax = fig.add_axes([0.93, 0.25, 0.02, 0.5])

for ax, (name, fen) in zip(axes.flat, positions.items()):
    board = chess.Board(fen)
    matrix = calculate_phase_space(fen)

    sns.heatmap(matrix, ax=ax, cmap="RdBu_r", center=0, vmin=-6, vmax=6,
                annot=False, cbar_ax=cbar_ax,
                cbar_kws={'label': 'Net Control (White + / Black -)'})


    for square in chess.SQUARES:
        row = 7 - chess.square_rank(square)
        col = chess.square_file(square)
        value = matrix[row, col]
        ax.text(col + 0.95, row + 0.93, f"{value:.1f}", ha="right", va="bottom",
                fontsize=8, color="white" if abs(value) > 3.5 else "#333333")
        piece = board.piece_at(square)
        if piece:
            ax.text(col + 0.5, row + 0.42, piece.unicode_symbol(),
                    ha="center", va="center", fontsize=28)

    white_total = matrix[matrix > 0].sum()
    black_total = -matrix[matrix < 0].sum()
    ax.set_title(f"{name}\nWhite: {white_total:.1f}   Black: {black_total:.1f}")
    ax.set_xticks(np.arange(8) + 0.5)
    ax.set_xticklabels(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
    ax.set_yticks(np.arange(8) + 0.5)
    ax.set_yticklabels(['8', '7', '6', '5', '4', '3', '2', '1'], rotation=0)

fig.suptitle("Square Control Heatmaps Across Four Chess Positions", fontsize=18)
fig.subplots_adjust(left=0.05, right=0.9, top=0.9, bottom=0.05, wspace=0.15, hspace=0.25)
plt.savefig("openings.png", dpi=200, bbox_inches="tight")  
plt.show()
