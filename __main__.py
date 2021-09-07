import pandas as pd
import click
import traceback

from ai import Problem, backtrace_template, first, nextBoard
from tree import build_root


@click.command()
@click.option('-filename', default="", help="Name of the file to read")
def n_queens(**kwargs):
    filename = kwargs.get('filename', None)
    try:
        board: pd.DataFrame = pd.read_csv(filename, header=None)
        root = build_root(board.values.tolist())
        if root == None:
            raise Exception("Initial Queen Not Specified")

        problem = Problem(n=len(board.columns), init_board=root)
        backtrace = backtrace_template(problem)
        backtrace(root)

    except Exception as e:
        # print(e)
        traceback.print_exc()
        return


n_queens()
