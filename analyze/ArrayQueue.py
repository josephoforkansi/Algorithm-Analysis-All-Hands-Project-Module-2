"""A basic array-based implementation of a Queue."""

from typing import Any

class ArrayQueue:
    """An array (list) implementation of a Queue (FIFO)."""
    def __init__(self):
        self._data = []

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._data.pop(0)

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def iconcat(self, other: 'ArrayQueue') -> None:
        self._data.extend(other._data)
        other._data.clear()

    def removelast(self) -> Any:
        """Removes and returns the last element."""
        if self.is_empty():
            raise IndexError("Remove from empty queue")
        return self._data.pop()
