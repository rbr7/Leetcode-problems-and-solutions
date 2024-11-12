from __future__ import annotations

import enum
import random
from typing import TypeVar

from src.types import Comparable

from .partition import partition
from .sorting import insertion_sort

T = TypeVar("T", bound=Comparable)


def randomized_quickselect(A: list[T], l: int, r: int, k: int) -> T:
    if k > 0 and k <= (r - l + 1):
        pivot_idx = random.randint(l, r)

        A[r], A[pivot_idx] = A[pivot_idx], A[r]

        q = partition(A, l, r)

        pivot_rank = 1 + (r - q)

        if k == pivot_rank:
            return A[q]

        if k < pivot_rank:
            return randomized_quickselect(A, q + 1, r, k)

        return randomized_quickselect(A, l, q - 1, k - pivot_rank)


def _find_medians_of_groups(A: list[T], l: int, r: int) -> list[T]:
    i = l
    medians = []

    while i <= r:
        start, end = i, min(i + 4, r)

        insertion_sort(A, l=start, r=end)
        medians.append(A[(start + end) // 2])

        i += 5

    return medians


def quickselect_mom(A: list[T], l: int, r: int, k: int) -> T:
    n = r - l + 1

    if k < 0 or k > n or n == 0:
        return

    if l == r:
        return l

    medians = _find_medians_of_groups(A, l, r)

    n_medians = len(medians)

    # Find the index of median of medians
    pivot_idx = quickselect_mom(medians, l=0, r=n_medians - 1, k=n_medians // 2)

    # Make it the pivot
    A[r], A[pivot_idx] = A[pivot_idx], A[r]

    q = partition(A, l, r)

    pivot_rank = 1 + (r - q)

    if k == pivot_rank:
        return q

    if k < pivot_rank:
        return quickselect_mom(A, q + 1, r, k)

    return quickselect_mom(A, l, q - 1, k - pivot_rank)
