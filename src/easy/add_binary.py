def add_binary_sol1(a: str, b: str) -> str:
    n_a = len(a)
    n_b = len(b)
    end = -(n_b + 1)

    if n_a < n_b:
        a, b = b, a
        end = -(n_a + 1)
        n_a, n_b = n_b, n_a

    carry = 0
    result = ""
    i = -1

    while i > end:
        bit_a = int(a[i])
        bit_b = int(b[i])
        carry, res = divmod(bit_a + bit_b + carry, 2)
        result += f"{res}"
        i -= 1

    end = -(n_a + 1)

    while i > end:
        bit_a = int(a[i])
        carry, res = divmod(bit_a + carry, 2)
        result += f"{res}"
        i -= 1

    if carry == 1:
        result += f"{carry}"

    return result[::-1]


def add_binary_sol2(a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    result = bin(a + b)
    return str(result)[2:]


if __name__ == "__main__":
    a = "1111001"
    b = "1101"

    print(add_binary_sol1(a=a, b=b))

    print(add_binary_sol2(a=a, b=b))
