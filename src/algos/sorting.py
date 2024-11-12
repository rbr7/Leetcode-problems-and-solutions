from __future__ import annotations

from typing import TypeVar

from src.types import Comparable

T = TypeVar("T", bound=Comparable)


def insertion_sort(A: list[T], l: int = 0, r: int = -1) -> None:
    n = len(A)

    if r == -1 or r >= n:
        r = n - 1

    for i in range(l + 1, r + 1):
        j = i - 1
        t = A[i]

        while j >= l and A[j] > t:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = t
