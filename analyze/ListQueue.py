"""Implementation of a queue using a list with a head pointer for efficient dequeuing."""

from typing import Any
from analyze.timer import timed, TimingResult


class ListQueueDisplay:
    """A queue implementation using a list with a head pointer and display functionality."""

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
        # Return the item at the head index without removing it
        if self.is_empty():
            raise IndexError("Cannot peek at empty queue")
        return self._L[self._head]

    @timed("dequeue")
    def dequeue(self) -> Any:
        """Remove and return the first item from the queue."""
        # Get the item at the head and increment head index
        item = self.peek()
        self._head += 1
        # Check if we need to clean up dequeued items
        if self._head >= self._cleanup_threshold:
            self._cleanup()
        return item

    def _cleanup(self) -> None:
        """Remove dequeued items from the list to free memory."""
        if self._head > 0:
            self._L = self._L[self._head:]
            self._head = 0

    @timed("length")
    def __len__(self) -> int:
        """Return the number of items currently in the queue."""
        # Return the number of items between head and end of list
        return len(self._L) - self._head

    @timed("size")
    def size(self) -> int:
        """Return the size of the queue."""
        return len(self)

    @timed("is_empty")
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        # Check if there are any items between head and end
        return len(self) == 0

    @timed("display")
    def display(self) -> None:
        """Print all items in the queue."""
        print(str(self))

    @timed("str")
    def __str__(self) -> str:
        """Return a string representation of the queue contents."""
        # Return string representation of items from head to end
        return str(self._L[self._head:])

    @timed("add")
    def __add__(self, other: "ListQueueDisplay") -> "ListQueueDisplay":
        """Concatenate two queues and return a new combined queue."""
        result = ListQueueDisplay()
        # Add items from first queue
        result._L.extend(self._L[self._head:])
        # Add items from second queue
        result._L.extend(other._L[other._head:])
        return result

    @timed("iadd")
    def __iadd__(self, other: "ListQueueDisplay") -> "ListQueueDisplay":
        """Concatenate another queue to this queue in-place."""
        # Add items from other queue using extend for efficiency
        self._L.extend(other._L[other._head:])
        # Clean up the other queue's memory
        other._L = []
        other._head = 0
        return self
