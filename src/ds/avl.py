from __future__ import annotations

from collections.abc import Iterator
from typing import Generic, TypeVar

from .binary_tree import BinaryTree

T1 = TypeVar("T1")
T2 = TypeVar("T2")


class AVLNode(Generic[T1]):
    def __init__(self, value: T1 = None) -> None:
        self.value = value
        self.left: AVLNode[T1] = None
        self.right: AVLNode[T1] = None
        self.p: AVLNode[T1] = None
        self.balance = 0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(val={self.value}, balance={self.balance})"


class AVLTree(BinaryTree, Generic[T2]):
    def __init__(self) -> None:
        self.root: AVLNode[T2] = None

    def __eq__(self, other: AVLTree[T2]) -> bool:
        return super().__eq__(other)

    @classmethod
    def fromarray(cls, arr: list[T2]) -> AVLTree[T2]:
        tree = cls()

        for value in arr:
            tree.insert(value)

        return tree

    def lr(self, node: AVLNode[T2]) -> None:
        y = node.right

        node.right = y.left

        if y.left is not None:
            y.left.p = node

        y.p = node.p

        if node.p is None:
            self.root = y

        elif node is node.p.left:
            node.p.left = y
        else:
            node.p.right = y

        y.left = node
        node.p = y

    def rr(self, node: AVLNode[T2]) -> None:
        x = node.left

        node.left = x.right

        if x.right is not None:
            x.right.p = node

        x.p = node.p

        if node.p is None:
            self.root = x
        elif node is node.p.right:
            node.p.right = x
        else:
            node.p.left = x

        x.right = node
        node.p = x

    def _update_balance(self, ya: AVLNode[T2], z: AVLNode[T2]) -> None:
        y = ya.left if z.value < ya.value else ya.right

        while y is not z:
            if z.value < y.value:
                y.balance = 1
                y = y.left
                continue

            y.balance = -1
            y = y.right

    def _imbalance_dir(self, ya: AVLNode[T2], z: AVLNode[T2]) -> int:
        if z.value < ya.value:
            return 1

        return -1

    def _handle_left_subtree(self, ya: AVLNode[T2], s: AVLNode[T2], i: int) -> None:
        if i == 1:
            self.rr(ya)
        else:
            self.lr(ya)

        ya.balance = 0
        s.balance = 0

    def _handle_right_subtree(self, ya: AVLNode[T2], s: AVLNode[T2], i: int) -> None:
        if i == 1:
            p = s.right
            self.lr(s)
            self.rr(ya)
        else:
            p = s.right
            self.rr(s)
            self.lr(ya)

        if p.balance == 0:
            ya.balance = 0
            s.balance = 0
        elif p.balance == i:
            ya.balance = -i
            s.balance = 0
        else:
            ya.balance = 0
            s.balance = i

        p.balance = 0

    def _avl_fixup(self, ya: AVLNode[T2], z: AVLNode[T2]) -> None:
        s = ya.left if z.value < ya.value else ya.right

        i = self._imbalance_dir(ya, z)

        if s.balance == i:
            return self._handle_left_subtree(ya, s, i)

        return self._handle_right_subtree(ya, s, i)

    def insert(self, value: T2) -> AVLNode[T2]:
        z = AVLNode(value=value)

        if self.root is None:
            self.root = z
            return

        y = None
        x = self.root

        ya = x

        while x is not None:
            y = x
            x = x.left if value < x.value else x.right

            if x is not None and x.balance != 0:
                ya = x

        z.p = y

        if z.value < y.value:
            y.left = z
        else:
            y.right = z

        self._update_balance(ya, z)

        i = self._imbalance_dir(ya, z)

        if ya.balance == 0:
            ya.balance = i
            return

        if ya.balance != i:
            ya.balance = 0
            return

        self._avl_fixup(ya, z)

        return z

    def preorder(self) -> Iterator[AVLNode[T2]]:
        return super().preorder()

    def inorder(self) -> Iterator[AVLNode[T2]]:
        return super().inorder()

    def postorder(self) -> Iterator[AVLNode[T2]]:
        return super().postorder()
