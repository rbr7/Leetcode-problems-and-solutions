from src.ds import Trie


def longest_common_prefix_sol1(strs: list[str]) -> str:
    if len(strs) == 0:
        return ""

    first, *remaining = strs

    for idx, char in enumerate(first):
        for string in remaining:
            if idx >= len(string) or string[idx] != char:
                return first[:idx]

    return first


def longest_common_prefix_sol2(strs: list[str]) -> str:
    trie = Trie.fromarray(keys=strs)

    node = trie.root

    prefix = ""

    while node.n_children() == 1 and node.is_leaf is False:
        node = node.last_child()
        prefix += node.value

    return prefix


if __name__ == "__main__":

    strs = ["flower", "flow", "flight"]

    print(longest_common_prefix_sol1(strs=strs))

    print(longest_common_prefix_sol2(strs=strs))
