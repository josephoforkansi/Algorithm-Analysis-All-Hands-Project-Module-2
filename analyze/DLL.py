"""Basic Doubly Linked List Queue implementation."""

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class Node:
    """Node class for doubly linked list."""
    value: Any
    prev: Optional["Node"] = None
    next: Optional["Node"] = None


class Queue:
    """Basic Doubly Linked List Queue implementation."""

    def __init__(self):
        """Initialize an empty queue."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def enqueue(self, value: Any) -> None:
        """Add an element to the end of the queue. O(1) operation."""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self) -> Any:
        """Remove and return the first element from the queue. O(1) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
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

    def __add__(self, other: "Queue") -> "Queue":
        """Concatenate two queues and return a new queue. O(1) operation."""
        if self.is_empty():
            return other
        if other.is_empty():
            return self

        # Create a new queue and link nodes
        result = Queue()
        result.head = self.head
        result.tail = other.tail
        result.size = self.size + other.size

        # Link the queues
        self.tail.next = other.head
        other.head.prev = self.tail

        # Ensure original queues remain unchanged
        other.head = None
        other.tail = None
        other.size = 0

        return result

    def __iadd__(self, other: "Queue") -> "Queue":
        """Concatenate another queue to this queue. O(1) operation."""
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
        elif not other.is_empty():
            self.tail.next = other.head
            other.head.prev = self.tail
            self.tail = other.tail
        self.size += other.size
        return self
