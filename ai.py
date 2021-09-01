from dataclasses import dataclass
from typing import Tuple
from tree import Tree


@dataclass
class Problem:
    n: int
    init_board: Tree


def isValidRectangle(x: Tuple, y: Tuple):
    return abs(abs(x[0] - y[0]) - abs(x[1] - y[1])) > 1


def accept(P: Problem, c: Tree):
    if len(c.board) == P.n:
        if P.init_board[0] in c.board:
            for x in c.board:
                for y in c.board:
                    if x == y:
                        continue
                    if not isValidRectangle(x, y):
                        return False
            return True
        return False
    return False


# reject if any of the queens attack each other
def reject(P: Problem, c: Tree):
    if P.init_board[0] in c.board:
        for x in c.board:
            for y in c.board:
                if x == y:
                    continue
                if not isValidRectangle(x, y):
                    return True
        return False
    return True


def output(P: Problem, c):
    pass


def first(P: Problem, c):
    return None


def next(P: Problem, s):
    return None


def gen_backtrace_function(problem: Problem):
    didFind = False

    def backtrace(c):
        nonlocal didFind
        if reject(problem, c):
            return
        if accept(problem, c):
            if not didFind:
                output(problem, c)
                didFind = True
            return
        s = first(problem, c)
        while s != None:
            backtrace(s)
            s = next(problem, s)

    return backtrace

# c is solution
# P is problem
