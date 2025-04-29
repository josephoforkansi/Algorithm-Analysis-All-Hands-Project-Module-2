"""A basic Singly Linked List implementation for a Queue."""

from typing import Any, Optional

class Node:
    """Represents a node in the singly linked list."""
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['Node'] = None

class BasicSLLQueue:
    """A Singly Linked List implementation of a Queue (FIFO)."""
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    def enqueue(self, item: Any) -> None:
        new_node = Node(item)
        if self._tail:
            self._tail.next = new_node
        else:
            self._head = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        result = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return result

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._head.data

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def iconcat(self, other: 'BasicSLLQueue') -> None:
        if other.is_empty():
            return
        if self.is_empty():
            self._head = other._head
            self._tail = other._tail
        else:
            self._tail.next = other._head
            self._tail = other._tail
        self._size += other._size
        other._head = None
        other._tail = None
        other._size = 0

    def removelast(self) -> Any:
        """Removes and returns the last element."""
        if self.is_empty():
            raise IndexError("Remove from empty queue")
        if self._head == self._tail:
            # Only one element
            value = self._head.data
            self._head = self._tail = None
            self._size = 0
            return value
        current = self._head
        while current.next != self._tail:
            current = current.next
        value = self._tail.data
        current.next = None
        self._tail = current
        self._size -= 1
        return value
