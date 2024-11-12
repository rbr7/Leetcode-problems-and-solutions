from src.ds import AVLTree


def sorted_array_to_bst(nums: list[int]) -> AVLTree:
    tree = AVLTree.fromarray(nums)
    return tree


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]

    result = sorted_array_to_bst(nums=nums)

    for node in result.inorder():
        print(node.value)
