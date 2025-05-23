"""A basic Doubly Linked List implementation for a Queue."""

from typing import Any, Optional

class Node:
    """Represents a node in a doubly linked list."""
    def __init__(self, data: Any):
        self.data = data
        self.prev: Optional['Node'] = None
        self.next: Optional['Node'] = None

class BasicDLLQueue:
    """A Doubly Linked List implementation of a Queue (FIFO)."""
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._size: int = 0

    def enqueue(self, item: Any) -> None:
        new_node = Node(item)
        if self._tail:
            self._tail.next = new_node
            new_node.prev = self._tail
        else:
            self._head = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        result = self._head.data
        self._head = self._head.next
        if self._head:
            self._head.prev = None
        else:
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

    def __add__(self, other: 'BasicDLLQueue') -> 'BasicDLLQueue':
        """Creates a new queue by merging two existing queues (O(n))."""
        new_queue = BasicDLLQueue()
        current = self._head
        while current:
            new_queue.enqueue(current.data)
            current = current.next
        current_other = other._head
        while current_other:
            new_queue.enqueue(current_other.data)
            current_other = current_other.next
        return new_queue

    def __iadd__(self, other: 'BasicDLLQueue') -> 'BasicDLLQueue':
        """Merges another queue into the current queue in place (O(1))."""
        if other._head:
            if not self._head:
                self._head = other._head
                self._tail = other._tail
            else:
                self._tail.next = other._head
                if other._head:
                    other._head.prev = self._tail
                self._tail = other._tail
            self._size += other._size
            other._head = None
            other._tail = None
            other._size = 0
        return self
