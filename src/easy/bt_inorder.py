from __future__ import annotations

from src.ds import BinaryTree


def inorder(tree: BinaryTree) -> list[int]:
    return [node.value for node in tree.inorder()]


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, None, 7, None, None, 6]

    tree = BinaryTree.fromarray(values=values)

    print(inorder(tree=tree))
