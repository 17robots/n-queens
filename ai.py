from dataclasses import dataclass
from typing import Tuple, List
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename='log.txt')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

Board = List[Tuple]

@dataclass
class Problem:
    n: int
    init_board: Board


def isValidRectangle(x: Tuple, y: Tuple):
    return abs(abs(x[0] - y[0]) - abs(x[1] - y[1])) > 0


def accept(P: Problem, c: Board):
    if len(c) == P.n:
        if P.init_board[0] in c:
            for x in c:
                for y in c:
                    if x == y:
                        continue
                    if not isValidRectangle(x, y):
                        return False
            return True
        return False
    return False


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
        for i in range(0, P.n - 1, 1):
            for j in range(0, P.n - 1, 1):
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
    if len(s) == P.n:
        if s[:-1][0] >= P.n - 1 and s[:-1][1] >= P.n - 1: return None
    queen = newBoard.pop() # we will be moving this queen
    newQueen = (1 if queen[1] + 1 >= P.n - 1 else queen[0], 0 if queen[1] + 1 >= P.n - 1 else queen[1] + 1)
    while newQueen in s:
        newQueen = (1 if newQueen[1] + 1 >= P.n - 1 else newQueen[0], 0 if newQueen[1] + 1 >= P.n - 1 else newQueen[1] + 1)    

    return newBoard + [newQueen]



def backtrace_template(problem: Problem):
    didFind = False

    def backtrace(c):
        nonlocal didFind
        logger.debug(f'Board State: {c}')
        if reject(problem, c):
            logger.debug(f"rejecting {c}")
            return
        if accept(problem, c):
            logger.debug(f"accepting {c}")
            if not didFind:
                output(problem, c)
                didFind = True
            return
        s = first(problem, c)
        while s != None:
            backtrace(s)
            s = nextBoard(problem, s)
        if not didFind:
            print("No Solution")

    return backtrace

# c is solution
# P is problem
