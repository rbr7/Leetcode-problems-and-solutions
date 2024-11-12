VALUES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

BEFORE = {
    "I": ("V", "X"),
    "X": ("L", "C"),
    "C": ("D", "M"),
}


def roman_to_int(s: str) -> int:
    limit = len(s) - 1

    result, i = 0, 0

    while i <= limit:
        digit = s[i]
        increment = 1
        value = VALUES[digit]

        if digit in BEFORE and i != limit:
            next_digit = s[i + 1]
            if next_digit in BEFORE[digit]:
                value = VALUES[next_digit] - value
                increment = 2

        result += value

        i += increment

    return result


if __name__ == "__main__":
    s = "MCMXCIV"
    print(roman_to_int(s))
