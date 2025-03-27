"""Implementation of a queue using a list with a head pointer for efficient dequeuing."""

from typing import Any
from analyze.timer import timed, TimingResult


class ListQueueDisplay:
    """A queue implementation using a list with a head pointer."""

    def __init__(self):
        # Initialize head index and underlying list
        self._head = 0
        self._L = []
        self.timing_result = TimingResult("ARRAY")
        self._cleanup_threshold = 1000  # Cleanup when there's this many dequeued items

    @timed("enqueue")
    def enqueue(self, item: Any) -> None:
        """Add an item to the end of the queue."""
        # Add item to the end of the list
        self._L.append(item)
        # Check if we need to clean up dequeued items
        if self._head >= self._cleanup_threshold:
            self._cleanup()

    @timed("peek")
    def peek(self) -> Any:
        """Return the first item in the queue without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at empty queue")
        return self._L[self._head]

    @timed("dequeue")
    def dequeue(self) -> Any:
        """Remove and return the first item from the queue (FIFO).
        This implementation is O(1) as it uses the head pointer."""
        if self.is_empty():
            raise IndexError("Queue is empty")

        # Store data from head
        item = self._L[self._head]

        # If only one element, clear the list
        if len(self._L) == 1:
            self._L = []
            self._head = 0
        else:
            # Move head pointer
            self._head += 1

        # Check if we need to clean up dequeued items
        if self._head >= self._cleanup_threshold:
            self._cleanup()
        return item

    def _cleanup(self) -> None:
        """Remove dequeued items from the list to free memory."""
        if self._head > 0:
            self._L = self._L[self._head :]
            self._head = 0

    @timed("length")
    def __len__(self) -> int:
        """Return the number of items currently in the queue."""
        return len(self._L) - self._head

    @timed("is_empty")
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self) == 0

    @timed("add")
    def __add__(self, other: "ListQueueDisplay") -> "ListQueueDisplay":
        """Concatenate two queues and return a new combined queue.
        Time complexity: O(n) where n is the total number of elements.
        More efficient than extend() as it pre-allocates the array."""
        result = ListQueueDisplay()
        # Create a new list with the combined size
        result._L = [None] * (len(self) + len(other))
        # Copy elements from first queue
        for i in range(len(self)):
            result._L[i] = self._L[self._head + i]
        # Copy elements from second queue
        for i in range(len(other)):
            result._L[len(self) + i] = other._L[other._head + i]
        return result

    @timed("iadd")
    def __iadd__(self, other: "ListQueueDisplay") -> "ListQueueDisplay":
        """Concatenate another queue to this queue in-place.
        Time complexity: O(n) where n is the total number of elements.
        More efficient than extend() as it pre-allocates the array."""
        # Create a new list with the combined size
        new_list = [None] * (len(self) + len(other))
        # Copy elements from current queue
        for i in range(len(self)):
            new_list[i] = self._L[self._head + i]
        # Copy elements from other queue
        for i in range(len(other)):
            new_list[len(self) + i] = other._L[other._head + i]
        # Update the queue
        self._L = new_list
        self._head = 0
        # Clean up other queue
        other._L = []
        other._head = 0
        return self
