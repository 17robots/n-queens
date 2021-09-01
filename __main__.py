import pandas as pd
from dataclasses import dataclass, field
import click
from pandas.core.frame import DataFrame


@dataclass
class Tree:
    data: list = field(default_factory=[], init=False)
    children: list = field(default_factory=[], init=False)

def createRoot(board: DataFrame) -> Tree:
    return Tree()

@click.command()
@click.option('-filename', default="", help="Name of the file to read")
def n_queens(**kwargs):
    filename = kwargs.get('filename', None)
    try:
        board: pd.DataFrame = pd.read_csv(filename, header=None)
        item = createRoot(board=board)
    except Exception as e:
        print(e)
        return
n_queens()