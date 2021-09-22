from typing import Tuple, List

Board = List[Tuple]
Problem = (int, Board)

def isValidRectangle(queen1: Tuple, queen2: Tuple):
    if queen1[0] == queen2[0] or queen1[1] == queen2[1]:
        return False
    return not abs((queen1[1] - queen2[1]) / (queen1[0] - queen2[0])) == 1

def output(P: Problem, c: Board):
    with open('output.csv', 'w') as f:
        for i in range(P[0]):
            for j in range(P[0]):
                f.write(f"{str(int((i, j) in c)) + (',' if j < P[0] - 1 else '')}")
            f.write('\n')

def isSafe(row, col, board):
    for queen in board:
        if not isValidRectangle((row,col), queen):
            return False
    return True

didFind = False
def backtrace(p: Problem, col: int, board: Board):
        if col >= p[0]:
            global didFind
            if not didFind:
                if p[0] < 25:
                    output(P=p, c=board)
                print(f'Solution Found: {board}')
                didFind = True
            return True
        else:
            for i in range(p[0]):
                if (i,col) in board:
                    return backtrace(p=p, board=board, col=col+1)
                if isSafe(row=i, col=col, board=board):
                    if backtrace(p=p, board=board + [(i, col)], col=col+1):
                        return True
            return False