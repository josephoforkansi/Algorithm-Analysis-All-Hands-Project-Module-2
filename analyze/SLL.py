"""Implementation of a singly linked list and queue using linked nodes."""

from typing import Any, Optional
from analyze.timer import timed, TimingResult
from dataclasses import dataclass


class ListNode:
    """A node in a singly linked list containing data and a link to the next node."""

    def __init__(self, data, link=None):
        # Initialize node with data and optional link to next node
        self.data = data
        self.link = link


class LinkedListPrime:
    """A singly linked list implementation with only head pointer for Queue operations."""

    def __init__(self):
        # Initialize empty list with just head pointer
        self._head = None
        self._length = 0
        self.timing_result = TimingResult("SLL")

    def clear(self):
        """Clear all nodes from the list."""
        self._head = None
        self._length = 0

    @timed("enqueue")
    def enqueue(self, item):
        """Add an item to the end of the queue (FIFO).
        Time complexity: O(n) as we need to traverse to the end."""
        new_node = ListNode(item)
        
        if self._head is None:
            self._head = new_node
        else:
            # Must traverse to end - this makes it O(n)
            current = self._head
            while current.link is not None:
                current = current.link
            current.link = new_node
            
        self._length += 1

    @timed("dequeue")
    def dequeue(self) -> Any:
        """Remove and return the first item from the queue (FIFO).
        Time complexity: O(1) as we only update head."""
        if self._head is None:
            raise IndexError("Queue is empty")

        item = self._head.data
        self._head = self._head.link
        self._length -= 1
        return item

    @timed("peek")
    def peek(self) -> Any:
        """Return the first item without removing it from the queue."""
        if self._head is None:
            raise IndexError("Cannot peek at empty queue")
        return self._head.data

    @timed("length")
    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return self._length

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._length == 0

    def __add__(self, other: "LinkedListPrime") -> "LinkedListPrime":
        """Concatenate two queues and return a new combined queue."""
        if self._head is None:
            return other
        if other._head is None:
            return self

        result = LinkedListPrime()
        result._head = self._head
        result._length = self._length

        # Must traverse to end - O(n)
        current = result._head
        while current.link is not None:
            current = current.link

        current.link = other._head
        result._length += len(other)
        return result

    def __iadd__(self, other: "LinkedListPrime") -> "LinkedListPrime":
        """Concatenate another queue to the current queue in-place."""
        if other._head is not None:
            if self._head is None:
                self._head = other._head
            else:
                # Must traverse to end - O(n)
                current = self._head
                while current.link is not None:
                    current = current.link
                current.link = other._head
            self._length += len(other)
            other._head = None
            other._length = 0
        return self


class LinkedQueue:
    """A queue implementation using a singly linked list."""

    def __init__(self):
        self._L = LinkedListPrime()
        self.timing_result = self._L.timing_result

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self._L.enqueue(item)

    def dequeue(self):
        """Remove and return the first item from the queue."""
        if self._L._head is None:
            raise IndexError("Queue is empty")
        return self._L.dequeue()

    def peek(self):
        """Return the first item without removing it from the queue."""
        if self._L._head is None:
            raise IndexError("Queue is empty")
        return self._L._head.data

    def __len__(self):
        """Return the number of items in the queue."""
        return len(self._L)

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self) == 0

    def __add__(self, other: "LinkedQueue") -> "LinkedQueue":
        """Concatenate two queues and return a new combined queue."""
        result = LinkedQueue()
        result._L = self._L + other._L
        return result

    def __iadd__(self, other: "LinkedQueue") -> "LinkedQueue":
        """Concatenate another queue to this queue in-place."""
        self._L += other._L
        return self


@dataclass
class Node:
    """Node class for singly linked list."""
    value: Any
    next: Optional['Node'] = None


class BasicSLLQueue:
    """Basic Singly Linked List Queue implementation without tail pointer."""

    def __init__(self):
        """Initialize an empty queue."""
        self.head: Optional[Node] = None
        self.size: int = 0
        self.timing_result = TimingResult("SLL")

    def enqueue(self, value: Any) -> None:
        """Add an element to the end of the queue. O(n) operation."""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            # Must traverse to end - O(n)
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def dequeue(self) -> Any:
        """Remove and return the first element from the queue. O(1) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self) -> Any:
        """Return the first element without removing it. O(1) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.value

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self.size == 0

    def __len__(self) -> int:
        """Return the number of elements in the queue."""
        return self.size

    def __add__(self, other: 'BasicSLLQueue') -> 'BasicSLLQueue':
        """Concatenate two queues. O(n) operation."""
        result = BasicSLLQueue()
        # Copy first queue
        current = self.head
        while current is not None:
            result.enqueue(current.value)
            current = current.next
        # Copy second queue
        current = other.head
        while current is not None:
            result.enqueue(current.value)
            current = current.next
        return result

    def __iadd__(self, other: 'BasicSLLQueue') -> 'BasicSLLQueue':
        """Concatenate another queue to this queue. O(n) operation."""
        if self.is_empty():
            self.head = other.head
        else:
            # Find end of current queue
            current = self.head
            while current.next is not None:
                current = current.next
            # Link to other queue
            current.next = other.head
        self.size += other.size
        return self


# For compatibility with tests
LinkedQueue = BasicSLLQueue
LinkedListPrime = BasicSLLQueue
