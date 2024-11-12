from src.ds import LinkedList


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(val={self.val})"


def merge_sorted_lists(list_a: LinkedList, list_b: LinkedList) -> LinkedList:
    if list_a.is_empty():
        return list_b

    curr_a, curr_b = list_a.head, list_b.head

    result = LinkedList()
    curr_res = result.push(-1)

    while curr_a is not None and curr_b is not None:
        if curr_a.value <= curr_b.value:
            curr_res.next = curr_a
            curr_res, curr_a = curr_res.next, curr_a.next
        else:
            curr_res.next = curr_b
            curr_res, curr_b = curr_res.next, curr_b.next

    longer = curr_b if curr_a is None else curr_a
    curr_res.next = longer

    result.pop()

    return result


if __name__ == "__main__":
    l1 = LinkedList()
    temp = l1.push(1)

    for i in (2, 3, 5):
        temp = l1.insert_after(temp, value=i)

    l2 = LinkedList()
    temp = l2.push(0)

    for i in (2, 4):
        temp = l2.insert_after(temp, value=i)

    result = merge_sorted_lists(list_a=l1, list_b=l2)

    for i in result:
        print(i)
