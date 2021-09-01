import pandas as pd
import click

from ai import Problem, gen_backtrace_function
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

        problem = Problem(n=len(board.columns), board=root)
        backtrace = gen_backtrace_function(problem)
        backtrace(root)

    except Exception as e:
        print(e)
        return


n_queens()
