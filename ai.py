from dataclasses import dataclass
from typing import Tuple, List

Board = List[Tuple]


@dataclass
class Problem:
    n: int
    init_board: Board


def isValidRectangle(x: Tuple, y: Tuple):
    if x[0] == y[0]:
        return False
    if x[1] == y[1]:
        return False
    return not abs((x[1] - y[1]) / (x[0] - y[0])) == 1


def accept(P: Problem, c: Board):
    return len(c) == P.n and P.init_board[0] in c


# reject if any of the queens attack each other
def reject(P: Problem, c: Board):
    if P.init_board[0] in c:
        for x in c:
            for y in c:
                if x == y:
                    continue
                if not isValidRectangle(x, y):
                    return True
        return False
    return True


def output(P: Problem, c: Board):
    with open('output.csv', 'w') as f:
        for i in range(0, P.n, 1):
            for j in range(0, P.n, 1):
                f.write(f"{1 if (i, j) in c else 0},")
            f.write('\n')


def first(P: Problem, c):
    returnBoard = c
    for i in range(0, P.n - 1, 1):
        for j in range(0, P.n - 1, 1):
            queen = (i, j)
            if queen not in P.init_board:
                return returnBoard + [queen]


def nextBoard(P: Problem, s: Board):
    newBoard = s
    queen = newBoard.pop()  # we will be moving this queen
    newQueen = (queen[0] + 1 if queen[1] + 1 >= P.n else queen[0],
                0 if queen[1] + 1 >= P.n else queen[1] + 1)
    if newQueen[0] >= P.n:
        return None
    while newQueen in s:
        newQueen = (newQueen[0] + 1 if newQueen[1] + 1 >= P.n - 1 else newQueen[0],
                    0 if newQueen[1] + 1 >= P.n - 1 else newQueen[1] + 1)
    return newBoard + [newQueen]


def backtrace_template_faster(problem: Problem):
    didFind - False
    pass


def backtrace_template(problem: Problem):
    didFind = False

    def backtrace(c):
        nonlocal didFind
        if reject(P=problem, c=c):
            return
        if accept(P=problem, c=c):
            if not didFind:
                output(P=problem, c=c)
                didFind = True
            return
        s = first(P=problem, c=c)
        while s != None:
            if didFind:
                break
            backtrace(c=s)
            s = nextBoard(P=problem, s=s)
        if c == problem.init_board and not didFind:
            print('no solution')
    return backtrace

# c is solution
# P is problem
