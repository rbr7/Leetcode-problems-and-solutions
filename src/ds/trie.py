from __future__ import annotations

from collections import OrderedDict


class Node:
    def __init__(self, is_leaf: bool = False, value: str = None) -> None:
        self.is_leaf = is_leaf
        self.value = value
        self.children: dict[int, Node] = OrderedDict()

    def __repr__(self) -> str:
        attrs = ("is_leaf", "value")
        string = ", ".join(f"{attr}={getattr(self, attr)}" for attr in attrs)
        return f"{self.__class__.__name__}({string})"

    def child_at(self, idx: int) -> Node:
        return self.children.get(idx)

    def add_or_update_child(self, idx: int, node: Node) -> None:
        self.children[idx] = node

    def n_children(self) -> int:
        return len(self.children)

    def first_child(self) -> Node:
        children = iter(self.children.values())
        val = next(children)
        return val

    def last_child(self) -> Node:
        children = reversed(self.children.values())
        val = next(children)
        return val


class Trie:
    def __init__(self, alphabet_size: int = 26) -> None:
        self.alphabet_size = alphabet_size
        self.root = Node()

    @classmethod
    def fromarray(
        cls, keys: list[str], values: list[str] = None, alphabet_size: int = 26
    ) -> Trie:
        if values is None:
            values = [None] * len(keys)

        trie = cls(alphabet_size=alphabet_size)

        for key, value in zip(keys, values):
            trie.insert(key=key, value=value)

        return trie

    def get_idx(self, char: str) -> int:
        return ord(char.lower()) - ord("a")

    def insert(self, key: str, value: str = None) -> Node:
        current_node = self.root

        for char in key:
            idx = self.get_idx(char)

            if current_node.child_at(idx) is None:
                node = Node(value=char)
                current_node.add_or_update_child(idx, node)

            current_node = current_node.child_at(idx)

        if value is None and len(key) != 0:
            value = char

        current_node.value = value
        current_node.is_leaf = True

    def search(self, key: str) -> Node | None:
        current_node = self.root

        for char in key:
            idx = self.get_idx(char)

            if current_node.child_at(idx) is None:
                return
            current_node = current_node.child_at(idx)

        return current_node

    def _delete(self, node: Node, key: str) -> Node | None:
        if key == "" and node.is_leaf is True:
            node.is_leaf = False
            node.value = None
            return node

        idx = self.get_idx(key[0])
        res = self._delete(node.child_at(idx), key[1:])
        node.add_or_update_child(idx, res)
        return node

    def delete(self, key: str) -> Node | None:
        return self._delete(self.root, key)


if __name__ == "__main__":
    keys = ["flower", "flight", "flow"]
    trie = Trie.fromarray(keys=keys)
