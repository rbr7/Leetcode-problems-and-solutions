def palindrome_number_sol1(x: int) -> bool:
    x = str(x)
    return x == x[::-1]


def palindrome_number_sol2(x: int) -> bool:
    if x < 0:
        return False

    temp_x, reverse = x, 0

    while temp_x != 0:
        reverse = reverse * 10 + temp_x % 10
        temp_x = temp_x // 10

    return x == reverse


if __name__ == "__main__":
    x = 121

    result = palindrome_number_sol1(x)
    print(result)

    result = palindrome_number_sol2(x)
    print(result)
