from __future__ import annotations


class Node:
    def __init__(self, val: int) -> None:
        self.val: int = val
        self.next: Node = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(val={self.val})"


class MyLinkedList:
    def __init__(self):
        self.head: Node = None
        self.length: int = 0

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(length={self.length})"

    def _get_node_at_index(self, index: int) -> Node | None:
        if index >= self.length:
            return

        node = self.head

        for _ in range(1, index + 1):
            node = node.next

        return node

    def get(self, index: int) -> int:
        result = self._get_node_at_index(index)
        if result is None:
            return -1

        return result.val

    def addAtHead(self, val: int) -> None:
        node = Node(val=val)
        node.next = self.head
        self.head = node

        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            return self.addAtHead(val)

        node = self.head

        while node.next is not None:
            node = node.next

        new_node = Node(val=val)
        node.next = new_node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == self.length:
            return self.addAtTail(val)

        if index == 0:
            return self.addAtHead(val)

        new_node = Node(val)
        node = self._get_node_at_index(index - 1)

        new_node.next = node.next
        node.next = new_node

        self.length += 1

    def pop(self):
        del_node = self.head
        self.head = del_node.next
        del del_node
        self.length -= 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        if index == 0:
            return self.pop()

        node = self._get_node_at_index(index - 1)
        del_node = node.next
        node.next = del_node.next
        del del_node

        self.length -= 1


if __name__ == "__main__":
    ops = [
        "MyLinkedList",
        "addAtHead",
        "get",
        "addAtIndex",
        "addAtIndex",
        "deleteAtIndex",
        "addAtHead",
        "addAtHead",
        "deleteAtIndex",
        "addAtIndex",
        "addAtHead",
        "deleteAtIndex",
    ]
    inputs = [[], [9], [1], [1, 1], [1, 7], [1], [7], [4], [1], [1, 4], [2], [5]]

    ll = MyLinkedList()

    result = []

    for op, ips in zip(ops[1:], inputs[1:]):
        method = getattr(ll, op)
        result.append(method(*ips))

    print(result)
