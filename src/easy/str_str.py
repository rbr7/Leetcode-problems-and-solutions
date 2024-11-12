import string

import src.algos as algos

alphabet = string.ascii_lowercase


def str_str_sol1(haystack: str, needle: str) -> int:
    """
    Naive Solution - Check all possible positions for needle.
    If the length of haystack is n and that of needle is n,
    then the needle can start at 0, 1, ..., or n - m + 1
    """
    if not needle:
        return 0

    return algos.naive_matcher(text=haystack, pattern=needle, first_only=True)


def str_str_sol2(haystack: str, needle: str) -> int:
    """
    Deterministic finite automata (DFA) -
    Build a DFA which accepts all strings that end with needle
    And then run haystack through the DFA, returning as soon as
    The final state is reached.

    Note: A more efficient implementation of transition function
    exits but is not used here.
    """
    if not needle:
        return 0

    return algos.automata_matcher(text=haystack, pattern=needle, first_only=True)


def str_str_sol3(haystack: str, needle: str) -> int:
    """
    Knuth-Morris-Pratt Algorithm
    """
    if not needle:
        return 0

    return algos.kmp_matcher(text=haystack, pattern=needle, first_only=True)


if __name__ == "__main__":
    haystack = "aaaaa"
    needle = "bba"

    print(str_str_sol1(haystack, needle))

    print(str_str_sol2(haystack, needle))

    print(str_str_sol3(haystack, needle))
