class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum_stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)

        curr_min = self.minimum

        if curr_min is None or val <= curr_min:
            self.minimum_stack.append(val)
            self.minimum = val

    def pop(self) -> None:
        val = self.stack.pop()

        if val == self.minimum:
            self.minimum_stack.pop()
            self.minimum = self.minimum_stack[-1] if self.minimum_stack else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]


if __name__ == "__main__":
    ops = [
        "MinStack",
        "push",
        "push",
        "push",
        "top",
        "pop",
        "getMin",
        "pop",
        "getMin",
        "pop",
        "push",
        "top",
        "getMin",
        "push",
        "top",
        "getMin",
        "pop",
        "getMin",
    ]
    inputs = [
        [],
        [2147483646],
        [2147483646],
        [2147483647],
        [],
        [],
        [],
        [],
        [],
        [],
        [2147483647],
        [],
        [],
        [-2147483648],
        [],
        [],
        [],
        [],
    ]

    stack = MinStack()

    for op, ips in zip(ops[1:], inputs[1:]):
        method = getattr(stack, op)
        print(method(*ips))
