import string


def compute_prefix_function(pattern: str) -> list[int]:
    prefix_func = [-1] * len(pattern)
    prefix_func[0] = 0

    k = 0

    for idx, char in enumerate(pattern[1:], 1):
        while k > 0 and pattern[k] != char:
            k = prefix_func[k - 1]

        if pattern[k] == char:
            k += 1

        prefix_func[idx] = k

    return prefix_func


def naive_matcher(
    text: str, pattern: str, *, first_only: bool = False
) -> int | list[int]:
    shifts = []
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        if pattern == text[i : i + m]:

            if first_only is True:
                return i

            shifts.append(i)

    return -1 if first_only is True else shifts


def _transition_func(pattern: str, alphabet: str) -> dict[tuple[int, str], int]:
    prefix_func = compute_prefix_function(pattern)

    m, func = len(pattern), {}

    for a in alphabet:
        func[(0, a)] = 0

    func[(0, pattern[0])] = 1

    for a in alphabet:
        for q in range(1, m + 1):
            state = q + 1

            if q == m or pattern[q] != a:
                state = func[(prefix_func[q - 1], a)]

            func[(q, a)] = state

    return func


def automata_matcher(
    text: str,
    pattern: str,
    alphabet: str = string.ascii_lowercase,
    *,
    first_only: bool = False
) -> int | list[int]:
    shifts = []
    m = len(pattern)
    delta = _transition_func(pattern=pattern, alphabet=alphabet)

    q = 0

    for idx, a in enumerate(text):
        q = delta[(q, a)]
        if q == m:
            pos = idx - m + 1

            if first_only is True:
                return pos

            shifts.append(pos)

    return -1 if first_only is True else shifts


def kmp_matcher(
    text: str, pattern: str, *, first_only: bool = False
) -> int | list[int]:
    prefix_func = compute_prefix_function(pattern)

    shifts = []

    q, m = 0, len(pattern)

    for idx, char in enumerate(text):
        while q > 0 and pattern[q] != char:
            q = prefix_func[q - 1]

        if pattern[q] == char:
            q += 1

        if q == m:
            pos = idx - m + 1

            if first_only is True:
                return pos

            shifts.append(pos)
            q = prefix_func[q]

    return -1 if first_only is True else shifts
