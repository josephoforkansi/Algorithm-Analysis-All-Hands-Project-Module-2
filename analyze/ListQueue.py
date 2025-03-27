"""Basic Array-based Queue implementation."""

from typing import Any, List


class ListQueueDisplay:
    """Basic Array-based Queue implementation using Python's list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.items: List[Any] = []

    def enqueue(self, value: Any) -> None:
        """Add an element to the end of the queue. O(1) operation."""
        self.items.append(value)

    def dequeue(self) -> Any:
        """Remove and return the first element from the queue. O(n) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        # This is explicitly O(n) as it shifts all elements
        return self.items.pop(0)

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
        # Explicitly create a new list requiring O(n) copy operations
        result.items = list(self.items)  # Copy first
        result.items.extend(other.items)  # Then extend
        return result

    def __iadd__(self, other: "ListQueueDisplay") -> "ListQueueDisplay":
        """Concatenate another queue to this queue. O(n) operation."""
        # Explicitly O(n) operation to copy all elements from other
        for item in other.items:
            self.items.append(item)
        return self
