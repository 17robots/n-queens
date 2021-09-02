from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Tree:
    board: List[Tuple]
    children: List = field(init=False, default_factory=list)


def build_root(arrs: list) -> List[Tuple] or None:
    root = None
    for i in range(0, len(arrs), 1):
        for j in range(0, len(arrs[i]), 1):
            if arrs[i][j] == 1:
                if root == None:
                    root = [(i, j)]
                else:
                    raise Exception("Multiple Queens Specified In File")

    return root
