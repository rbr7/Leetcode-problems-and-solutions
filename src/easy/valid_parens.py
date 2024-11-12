PAREN_MAP = {
    "(": ")",
    "{": "}",
    "[": "]",
}


def valid_parens(s: str) -> bool:
    stack = []
    push, pop = list.append, list.pop

    for char in s:
        if char in PAREN_MAP:
            push(stack, char)
        else:
            if not stack:
                return False

            bracket = pop(stack)
            if char != PAREN_MAP[bracket]:
                return False

    return not stack


if __name__ == "__main__":
    s = "()[]{}"
    print(valid_parens(s=s))

    s = "(]"
    print(valid_parens(s=s))
