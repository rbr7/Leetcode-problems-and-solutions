from src.ds import BinaryTree


def same_tree(tree_a: BinaryTree, tree_b: BinaryTree) -> bool:
    return tree_a == tree_b


if __name__ == "__main__":
    a = BinaryTree.fromarray([1, 2, 3])
    b = BinaryTree.fromarray([1, 2, 3])

    print(same_tree(tree_a=a, tree_b=b))

    a = BinaryTree.fromarray([1, 1])
    b = BinaryTree.fromarray([1, None, 1])

    print(same_tree(tree_a=a, tree_b=b))
