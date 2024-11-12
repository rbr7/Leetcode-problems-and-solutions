from typing import Generic, TypeVar

from src.exceptions import UnderflowError

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.stack = []

    def __bool__(self) -> bool:
        return bool(self.stack)

    def tos(self, *, ignore_uf=False) -> T | None:
        if ignore_uf is True:
            try:
                return self.stack[-1]
            except IndexError:
                return None

        if not self.stack:
            raise UnderflowError("stack is empty")

        return self.stack[-1]

    def push(self, value: T) -> None:
        self.stack.append(value)

    def pop(self) -> T:
        if not self.stack:
            raise UnderflowError("stack is empty")

        return self.stack.pop()
