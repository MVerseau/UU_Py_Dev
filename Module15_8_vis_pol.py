from Module15_8 import GRID_SIZE
import numpy as np
import random
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def visualize_policy(Q):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0, GRID_SIZE, 1))
    ax.set_yticks(np.arange(0, GRID_SIZE, 1))
    ax.grid()

    for state in Q:
        row, col = state
        if (row, col) == (4, 4):
            ax.add_patch(patches.Rectangle((col, row), 1, 1, color='green'))  # Целевая клетка
        else:
            ax.add_patch(patches.Rectangle((col, row), 1, 1, color='white', fill=False))  # Обычная клетка

        if len(Q[state]) > 0:
            action = max(Q[state], key=Q[state].get)
            ax.text(col + 0.5, row + 0.5, action, fontsize=12, ha='center', va='center')

    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)
    ax.invert_yaxis()
    ax.set_aspect('equal')
    plt.show()