def sqrt(x: int) -> int:
    if x == 0:
        return x

    root = x / 2
    epsilon = 1e-3

    while True:
        prev = root
        root = (root + x / root) * 0.5

        if abs(root - prev) <= epsilon:
            return int(root)


if __name__ == "__main__":
    x = 53
    print(sqrt(x=x))
