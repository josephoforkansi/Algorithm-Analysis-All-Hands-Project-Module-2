"""A Doubly Linked List implementation for a Queue."""

from typing import Any, Optional

class Node:
    """Represents a node in the doubly linked list."""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

class Queue:
    """A Doubly Linked List implementation of a Queue (FIFO)."""
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    def enqueue(self, value: Any) -> None:
        """Add an element to the back of the queue (O(1))."""
        new_node = Node(value)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self) -> Any:
        """Remove and return the front element of the queue (O(1))."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._head.data
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        else:
            self._tail = None
        self._size -= 1
        return value

    def peek(self) -> Any:
        """Return the front element without removing it (O(1))."""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._head.data

    def size(self) -> int:
        """Return the number of elements in the queue (O(1))."""
        return self._size

    def is_empty(self) -> bool:
        """Check if the queue is empty (O(1))."""
        return self._size == 0

    def __add__(self, other: "Queue") -> "Queue":
        """Creates a new queue by merging two existing queues (O(n))."""
        new_queue = Queue()
        current = self._head
        while current:
            new_queue.enqueue(current.data)
            current = current.next
        current = other._head
        while current:
            new_queue.enqueue(current.data)
            current = current.next
        return new_queue

    def __iadd__(self, other: "Queue") -> "Queue":
        """Merges another queue into the current queue in place (O(1))."""
        if other._head:
            if not self._head:
                self._head = other._head
                self._tail = other._tail
            else:
                self._tail.next = other._head
                other._head.prev = self._tail
                self._tail = other._tail
            self._size += other._size
            # To avoid issues with the 'other' queue being modified externally
            other._head = None
            other._tail = None
            other._size = 0
        return self
    
