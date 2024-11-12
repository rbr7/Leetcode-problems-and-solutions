from src.ds import LinkedList


def remove_duplicates(l: LinkedList) -> LinkedList:
    if l.is_empty():
        return l

    curr = l.head.value
    prev = l.head
    node = l.head.next

    while node is not None:
        if curr != node.value:
            curr = node.value
            prev.next = node
            prev = prev.next
            node = prev.next
            continue

        node = node.next

    prev.next = None

    return l


if __name__ == "__main__":
    l = LinkedList()
    temp = l.push(1)

    items = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 11]
    for item in items:
        temp = l.insert_after(temp, value=item)

    l_str = " -> ".join(f"{node.value}" for node in l)
    print(f"Input: {l_str}")

    result = remove_duplicates(l=l)

    res_str = " -> ".join(f"{node.value}" for node in result)
    print(f"Output: {res_str}")
