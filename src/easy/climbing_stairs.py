def climbing_stairs(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        b, a = a + b, b

    return b


if __name__ == "__main__":
    n = 7
    print(climbing_stairs(n=n))
