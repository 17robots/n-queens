# N-Queens Solver
# Program to Solve N-Queens
# University of Akron
# 9-15-21


import pandas as pd
import traceback
from time import time

from ai import backtrace, Board, Problem

def build_root(arrs: list) -> Board:
    root = []

    for i in range(len(arrs)):
        for j in range(len(arrs[i])):
            if arrs[i][j] == 1:
                root.append((i,j))
    return root

if __name__ == '__main__':
    try:
        board: pd.DataFrame = pd.read_csv("input.csv", header=None)
        root: Board = build_root(board.values.tolist())

        problem: Problem = (len(board.columns), root)
        start = time()
        result = backtrace(p=problem, col=0, board=problem[1])
        end = time()
        if not result:
            print("No Solution Found")
        print(f'result found in {end - start} seconds')
        

    except Exception as e:
        traceback.print_exc()
