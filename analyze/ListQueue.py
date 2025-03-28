"""Basic Array-based Queue implementation."""

from typing import Any, Deque
from collections import deque


class ListQueueDisplay:
    """Basic Array-based Queue implementation using Python's deque."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items: Deque[Any] = deque()

    def enqueue(self, value: Any) -> None:
        """Add an element to the end of the queue. O(1) operation."""
        self.items.append(value)

    def dequeue(self) -> Any:
        """Remove and return the first element from the queue. O(1) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def peek(self) -> Any:
        """Return the first element without removing it. O(1) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.items) == 0

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return len(self.items)

    def __add__(self, other: "ListQueueDisplay") -> "ListQueueDisplay":
        """Concatenate two queues. O(n) operation."""
        result = ListQueueDisplay()
        result.items = deque(self.items)  # Copy first queue
        result.items.extend(other.items)  # Append second queue
        return result

    def __iadd__(self, other: "ListQueueDisplay") -> "ListQueueDisplay":
        """Concatenate another queue to this queue. O(n) operation."""
        self.items.extend(other.items)
        return self
