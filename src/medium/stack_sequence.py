def validate_stack_sequence_sol1(pushed: list[int], popped: list[int]) -> bool:
    n = len(popped)

    stack = []

    push_idx = pop_idx = 0

    seen = set()

    while True:
        # Push all elements which are not equal to the current popped element
        while push_idx < n and pushed[push_idx] != popped[pop_idx]:
            elem = pushed[push_idx]
            seen.add(elem)
            stack.append(elem)
            push_idx += 1

        # Increment by 1 to indicate that this element has been popped
        pop_idx += 1

        # Pop any element that is already pushed
        while stack and popped[pop_idx] in seen:
            # If the TOS and the current element out of those that have been pushed
            # Do not match, the sequence is invalid
            if stack[-1] != popped[pop_idx]:
                return False

            stack.pop()
            pop_idx += 1

        # Or if there is nothing to push and the stack is empty, return True
        # If only one element is remaining, return True
        # Since a push followed by a pop will produce the sequence
        if pop_idx == n - 1 or (push_idx == n and not stack):
            return True

        push_idx += 1


def validate_stack_sequence_sol2(pushed: list[int], popped: list[int]) -> bool:
    stack = []
    index = 0

    for elem in pushed:
        # Push each element in pushed as it is encountered
        stack.append(elem)

        # After every push, see if any pop operations are possible and do them
        while stack and stack[-1] == popped[index]:
            stack.pop()
            index += 1

    # If the stack is empty at the end, the sequence is valid
    return not stack


if __name__ == "__main__":
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]

    print(validate_stack_sequence_sol1(pushed=pushed, popped=popped))

    print(validate_stack_sequence_sol2(pushed=pushed, popped=popped))
