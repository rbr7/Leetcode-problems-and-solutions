class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * (k + 1)
        self.front = self.rear = k
        self.k = k + 1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.k
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[(self.front + 1) % self.k]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % self.k == self.front


if __name__ == "__main__":
    ops = [
        "MyCircularQueue",
        "enQueue",
        "enQueue",
        "enQueue",
        "enQueue",
        "Rear",
        "isFull",
        "deQueue",
        "enQueue",
        "Rear",
    ]
    inputs = [[3], [1], [2], [3], [4], [], [], [], [4], []]

    k = inputs[0][0]
    q = MyCircularQueue(k=k)

    for op, ips in zip(ops[1:], inputs[1:]):
        method = getattr(q, op)
        print(method(*ips))
