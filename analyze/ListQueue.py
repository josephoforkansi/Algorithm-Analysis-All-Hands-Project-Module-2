"""Basic Array-based Queue implementation."""

from typing import Any, List
from .timer import TimingResult


class ListQueueDisplay:
    """Basic Array-based Queue implementation using Python's list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items: List[Any] = []
        self.timing_result = TimingResult("ARRAY")

    def enqueue(self, value: Any) -> None:
        """Add an element to the end of the queue."""
        self.items.append(value)

    def dequeue(self) -> Any:
        """Remove and return the first element from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self) -> Any:
        """Return the first element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.items) == 0

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return len(self.items)

    def __add__(self, other: 'ListQueueDisplay') -> 'ListQueueDisplay':
        """Concatenate two queues."""
        result = ListQueueDisplay()
        result.items = self.items + other.items
        return result

    def __iadd__(self, other: 'ListQueueDisplay') -> 'ListQueueDisplay':
        """Concatenate another queue to this queue."""
        self.items.extend(other.items)
        return self
