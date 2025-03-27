"""A doubly linked list implementation with a Queue interface."""

from typing import Any, Optional
from analyze.timer import timed, TimingResult


class ListNode:
    """A node in a doubly linked list."""

    def __init__(
        self,
        data: Any,
        prev: Optional["ListNode"] = None,
        link: Optional["ListNode"] = None,
    ) -> None:
        """Initialize a new ListNode."""
        self.data = data
        self.prev = prev
        self.link = link


class DoublyLinkedList:
    """A doubly linked list implementation with head and tail pointers for Queue operations."""

    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        # Initialize empty list with no head or tail
        self._head = None
        self._tail = None
        self._length = 0
        self.timing_result = TimingResult("DLL")

    def clear(self):
        """Clear all nodes from the list."""
        self._head = None
        self._tail = None
        self._length = 0

    @timed("enqueue")
    def enqueue(self, item: Any) -> None:
        """Add an item to the end of the queue (FIFO)."""
        new_node = ListNode(item)
        if self._head is None:
            self._head = new_node
        else:
            new_node.prev = self._tail
            self._tail.link = new_node
        self._tail = new_node
        self._length += 1

    @timed("dequeue")
    def dequeue(self) -> Any:
        """Remove and return the first item from the queue (FIFO).
        This implementation is O(1) as it removes from the head."""
        # Check if list is empty
        if self._head is None:
            raise IndexError("Queue is empty")

        # Store data from head
        item = self._head.data

        # If only one element, clear the list
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            # Move head to next node
            self._head = self._head.link
            # Clear prev pointer of new head
            self._head.prev = None

        self._length -= 1
        return item

    @timed("length")
    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return self._length

    @timed("size")
    def size(self) -> int:
        """Return the size of the queue."""
        return self._length

    @timed("is_empty")
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._length == 0

    @timed("peek")
    def peek(self) -> Any:
        """Return the first item without removing it from the queue."""
        if self._head is None:
            raise IndexError("Cannot peek at empty queue")
        return self._head.data

    def __add__(self, other: "DoublyLinkedList") -> "DoublyLinkedList":
        """Concatenate two queues and return a new combined queue."""
        # Handle empty queue cases
        if self._head is None:
            return other
        if other._head is None:
            return self

        # Create new queue and copy first queue's nodes
        result = DoublyLinkedList()
        result._head = self._head
        result._tail = self._tail
        result._length = self._length

        # Link the two queues together
        result._tail.link = other._head
        other._head.prev = result._tail
        result._tail = other._tail
        result._length += len(other)

        return result

    def __iadd__(self, other: "DoublyLinkedList") -> "DoublyLinkedList":
        """Concatenate another queue to the current queue in-place."""
        # Only proceed if other queue is not empty
        if other._head is not None:
            # Handle empty current queue case
            if self._head is None:
                self._head = other._head
            else:
                # Link other queue to current queue's tail
                self._tail.link = other._head
                other._head.prev = self._tail
            self._tail = other._tail
            self._length += len(other)
            # Clear other queue
            other._head = None
            other._tail = None
            other._length = 0
        return self


class Queue:
    """A queue implementation using a doubly linked list."""

    def __init__(self) -> None:
        """Initialize an empty queue."""
        # Use doubly linked list as underlying data structure
        self._list: DoublyLinkedList = DoublyLinkedList()
        self.timing_result = self._list.timing_result  # Share timing result with list

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._list.enqueue(item)

    def dequeue(self) -> Any:
        """Remove and return the first item from the queue."""
        return self._list.dequeue()

    def peek(self) -> Any:
        """Return the first item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek from empty queue")
        return self._list.peek()

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._list) == 0

    def size(self) -> int:
        """Get the number of items in the queue."""
        return len(self._list)

    def __len__(self) -> int:
        """Return the length of the queue."""
        return len(self._list)

    def __add__(self, other: "Queue") -> "Queue":
        """Concatenate two queues and return a new combined queue."""
        result = Queue()
        result._list = self._list + other._list
        return result

    def __iadd__(self, other: "Queue") -> "Queue":
        """Concatenate another queue to this queue in-place."""
        self._list += other._list
        return self
