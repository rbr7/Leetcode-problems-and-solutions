from __future__ import annotations
from typing import TypeVar

from src.types import Comparable

T = TypeVar("T", bound=Comparable)


def partition(A: list[T], l: int, r: int) -> int:
    """
    Partition A[l...r] (both inclusive) around a pivot A[r] such that
    all elements to the left of A[r] are less than or equal to A[r]
    and all elements to the right of A[r] are greater than A[r].

    By convention, the pivot is chosen to be the last element.

    After  partitioning, A[r] is placed at the index where it would be
    if the array were sorted.

    Arguments
    ----------
        A: array to be partitioned
        l: starting index for A[l...r]
        r: ending index for A[l...r]

    Returns
    ----------
        int: the index of the pivot if the array were sorted

    Example
    ----------
    >>> A = [5, 10, 1, 2, 3, 4]
    >>> partition(A, 0, 5)
    >>> A
    [1, 2, 3, 4, 5, 10]
    >>> A = [5, 10, 1, 2, 3, 4]
    >>> A[-1], A[3] = A[3], A[-1]  # Use A[3] as pivot
    >>> partition(A, 0, 5)
    >>> A
    [1, 2, 5, 4, 3, 10]
    """
    pivot = A[r]
    i = l - 1

    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
