"""Implementation of a singly linked list and queue using linked nodes."""

from typing import Any, Optional
from analyze.timer import timed, TimingResult


class ListNode:
    """A node in a singly linked list containing data and a link to the next node."""

    def __init__(self, data, link=None):
        # Initialize node with data and optional link to next node
        self.data = data
        self.link = link


class LinkedListPrime:
    """A singly linked list implementation with head and tail pointers for Queue operations."""

    def __init__(self):
        # Initialize empty list with no head or tail
        self._head = None
        self._tail = None
        self._length = 0
        self.timing_result = TimingResult("SLL")

    def clear(self):
        """Clear all nodes from the list."""
        self._head = None
        self._tail = None
        self._length = 0

    @timed("enqueue")
    def enqueue(self, item):
        """Add an item to the end of the queue (FIFO)."""
        # If list is empty, use addfirst logic
        if self._head is None:
            self._head = ListNode(item)
            self._tail = self._head
        else:
            # Add new node after current tail
            self._tail.link = ListNode(item)
            self._tail = self._tail.link
        self._length += 1

    @timed("dequeue")
    def dequeue(self) -> Any:
        """Remove and return the last item from the queue (FIFO).
        This implementation is O(n) as it needs to traverse to find the previous node."""
        # Check if list is empty
        if self._tail is None:
            raise IndexError("Queue is empty")
            
        # Store data from tail
        item = self._tail.data
        
        # If only one element, clear the list
        if self._tail == self._head:
            self._head = None
            self._tail = None
        else:
            # Find the previous node by traversing from head
            current = self._head
            while current.link != self._tail:
                current = current.link
            # Update links
            current.link = None
            self._tail = current
            
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
        """Return the last item without removing it from the queue."""
        if self._tail is None:
            raise IndexError("Cannot peek at empty queue")
        return self._tail.data

    def __add__(self, other: "LinkedListPrime") -> "LinkedListPrime":
        """Concatenate two queues and return a new combined queue."""
        # Handle empty queue cases
        if self._head is None:
            return other
        if other._head is None:
            return self

        # Create new queue and copy first queue's nodes
        result = LinkedListPrime()
        result._head = self._head
        result._tail = self._tail
        result._length = self._length

        # Link the two queues together
        result._tail.link = other._head
        result._tail = other._tail
        result._length += len(other)

        return result

    def __iadd__(self, other: "LinkedListPrime") -> "LinkedListPrime":
        """Concatenate another queue to the current queue in-place."""
        # Only proceed if other queue is not empty
        if other._head is not None:
            # Handle empty current queue case
            if self._head is None:
                self._head = other._head
            else:
                # Link other queue to current queue's tail
                self._tail.link = other._head
            self._tail = other._tail
            self._length += len(other)
            # Clear other queue
            other.clear()
        return self


class LinkedQueue:
    """A queue implementation using a singly linked list."""

    def __init__(self):
        # Initialize queue with empty linked list
        self._L = LinkedListPrime()
        self.timing_result = self._L.timing_result  # Share timing result with list

    @timed("enqueue")
    def enqueue(self, item):
        """Add an item to the end of the queue."""
        # Add item to end of list
        self._L.enqueue(item)

    @timed("dequeue")
    def dequeue(self):
        """Remove and return the first item from the queue."""
        # Check if queue is empty
        if self._L._head is None:
            raise IndexError("Queue is empty")
        # Remove and return first item
        return self._L.dequeue()

    @timed("peek")
    def peek(self):
        """Return the first item without removing it from the queue."""
        if self._L._head is None:
            raise IndexError("Queue is empty")
        return self._L._head.data

    @timed("display")
    def display(self):
        """Print all items in the queue."""
        # Print all items in the queue
        current = self._L._head
        while current is not None:
            print(current.data, end=" ")
            current = current.link

    @timed("length")
    def __len__(self):
        """Return the number of items in the queue."""
        # Return number of items in queue
        return len(self._L)

    @timed("size")
    def size(self) -> int:
        """Return the size of the queue."""
        return len(self._L)

    @timed("is_empty")
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self) == 0

    @timed("add")
    def __add__(self, other: "LinkedQueue") -> "LinkedQueue":
        """Concatenate two queues and return a new combined queue."""
        result = LinkedQueue()
        result._L = self._L + other._L
        return result

    @timed("iadd")
    def __iadd__(self, other: "LinkedQueue") -> "LinkedQueue":
        """Concatenate another queue to this queue in-place."""
        self._L += other._L
        return self
