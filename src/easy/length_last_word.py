def length_last_word(s: str) -> int:
    i = len(s) - 1

    while s[i] == " ":
        i -= 1

    word_len = 1

    for j in range(i - 1, -1, -1):
        if s[j] != " ":
            word_len += 1
            continue

        break

    return word_len


if __name__ == "__main__":
    s = "  fly    me  to the   moon  "

    print(length_last_word(s=s))
