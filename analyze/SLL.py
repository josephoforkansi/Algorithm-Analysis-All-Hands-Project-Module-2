"""Basic Singly Linked List Queue implementation."""

from typing import Any, Optional
from dataclasses import dataclass


@dataclass
class Node:
    """Node class for singly linked list."""
    value: Any
    next: Optional["Node"] = None


class BasicSLLQueue:
    """Optimized Singly Linked List Queue implementation with tail pointer."""

    def __init__(self):
        """Initialize an empty queue with head and tail pointers."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self.size == 0

    def enqueue(self, value: Any) -> None:
        """Add an element to the end of the queue. O(1) operation using tail pointer."""
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node  # Directly append at tail
        self.tail = new_node  # Update tail pointer
        self.size += 1

    def dequeue(self) -> Any:
        """Remove and return the first element from the queue. O(1) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:  # If queue is now empty, reset tail
            self.tail = None
        self.size -= 1
        return value

    def peek(self) -> Any:
        """Return the first element without removing it. O(1) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.value

    def removelast(self) -> Any:
        """Remove and return the last element from the queue. O(n) operation."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        if self.head == self.tail:  # Only one element
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            # Traverse to find second-to-last node
            current = self.head
            while current.next != self.tail:
                current = current.next
            value = self.tail.value
            current.next = None
            self.tail = current
        
        self.size -= 1
        return value

    def __add__(self, other: "BasicSLLQueue") -> "BasicSLLQueue":
        """Concatenate two queues. O(1) operation using tail pointer."""
        if self.is_empty():
            return other
        if other.is_empty():
            return self

        result = BasicSLLQueue()
        result.head = self.head
        result.tail = other.tail
        result.size = self.size + other.size

        self.tail.next = other.head  # Connect self to other
        return result

    def __iadd__(self, other: "BasicSLLQueue") -> "BasicSLLQueue":
        """Concatenate another queue to this queue. O(1) operation."""
        if self.is_empty():
            self.head = other.head
            self.tail = other.tail
        elif not other.is_empty():
            self.tail.next = other.head
            self.tail = other.tail
        self.size += other.size
        return self
