from collections import deque

from src.ds import BinaryTree


def is_symmetric(tree: BinaryTree) -> bool:
    root = tree.root

    if root is None:
        return True

    left = root.left
    right = root.right

    if (left is None) ^ (right is None):
        return False

    if left is None and right is None:
        return True

    lqueue = deque()
    rqueue = deque()

    while True:
        if left.value != right.value:
            return False

        left_c = left.left
        right_c = right.right

        if (left_c is None) ^ (right_c is None):
            return False

        if left_c is not None and right_c is not None:
            lqueue.append(left_c)
            rqueue.append(right_c)

        left_c = left.right
        right_c = right.left

        if (left_c is None) ^ (right_c is None):
            return False

        if left_c is not None and right_c is not None:
            lqueue.append(left_c)
            rqueue.append(right_c)

        if not lqueue and not rqueue:
            return True

        left = lqueue.popleft()
        right = rqueue.popleft()


if __name__ == "__main__":
    tree = BinaryTree.fromarray([1, 2, 2, 2, None, 2])

    print(is_symmetric(tree=tree))
