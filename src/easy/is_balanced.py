from src.ds import BinaryTree


def is_balanced(tree: BinaryTree) -> bool:
    return tree.is_balanced()


if __name__ == "__main__":
    values = [3, 9, 20, None, None, 15, 7]

    tree = BinaryTree.fromarray(values=values)

    print(is_balanced(tree))
