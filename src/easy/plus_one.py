def plus_one(digits: list[int]) -> list[int]:
    i = len(digits) - 1

    while digits[i] == 9:
        digits[i] = 0
        i -= 1

    if i == -1:
        return [1] + digits

    digits[i] += 1
    return digits


if __name__ == "__main__":
    digits = [9] * 100
    print(plus_one(digits=digits))
