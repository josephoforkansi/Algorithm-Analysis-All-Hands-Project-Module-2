"""Basic Singly Linked List Queue implementation."""

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class Node:
    """Node class for singly linked list."""

    value: Any
    next: Optional["Node"] = None


class BasicSLLQueue:
    """Basic Singly Linked List Queue implementation without tail pointer."""

    def __init__(self):
        """Initialize an empty queue."""
        self.head: Optional[Node] = None
        self.size: int = 0

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

    def __add__(self, other: "BasicSLLQueue") -> "BasicSLLQueue":
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

    def __iadd__(self, other: "BasicSLLQueue") -> "BasicSLLQueue":
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
