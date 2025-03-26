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
        # Automatically update the links of adjacent nodes
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self


class DoublyLinkedList:
    """A doubly linked list implementation."""

    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        # Initialize head and tail pointers to None for empty list
        self._head: Optional[ListNode] = None
        self._tail: Optional[ListNode] = None
        self._length: int = 0
        self.timing_result = TimingResult("DLL")

    @timed("length")
    def __len__(self) -> int:
        """Return the length of the list."""
        return self._length

    @timed("size")
    def size(self) -> int:
        """Return the size of the list."""
        return self._length

    @timed("is_empty")
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self._length == 0

    def _addbetween(
        self,
        item: Any,
        before: Optional[ListNode],
        after: Optional[ListNode],
    ) -> None:
        """Add an item between two nodes."""
        # Create new node and update its links
        node = ListNode(item, before, after)
        # Update head if adding at front
        if after is self._head:
            self._head = node
        # Update tail if adding at back
        if before is self._tail:
            self._tail = node
        self._length += 1

    @timed("addfirst")
    def addfirst(self, item: Any) -> None:
        """Add an item to the front of the list."""
        self._addbetween(item, None, self._head)

    @timed("addlast")
    def addlast(self, item: Any) -> None:
        """Add an item to the end of the list."""
        self._addbetween(item, self._tail, None)

    def _remove(self, node: ListNode) -> Any:
        """Remove a node from the list."""
        # Store references to adjacent nodes
        before, after = node.prev, node.link
        # Update head if removing first node
        if node is self._head:
            self._head = after
        else:
            before.link = after
        # Update tail if removing last node
        if node is self._tail:
            self._tail = before
        else:
            after.prev = before
        self._length -= 1
        return node.data

    @timed("removefirst")
    def removefirst(self) -> Any:
        """Remove and return the first item in the list."""
        if self._head is None:
            raise IndexError("Cannot remove from empty list")
        return self._remove(self._head)

    @timed("removelast")
    def removelast(self) -> Any:
        """Remove and return the last item in the list."""
        if self._tail is None:
            raise IndexError("Cannot remove from empty list")
        return self._remove(self._tail)

    @timed("peek")
    def peek(self) -> Any:
        """Return the first item without removing it."""
        if self._head is None:
            raise IndexError("Cannot peek at empty list")
        return self._head.data


class Queue:
    """A queue implementation using a doubly linked list."""

    def __init__(self) -> None:
        """Initialize an empty queue."""
        # Use doubly linked list as underlying data structure
        self._list: DoublyLinkedList = DoublyLinkedList()
        self.timing_result = self._list.timing_result  # Share timing result with list

    @timed("enqueue")
    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._list.addlast(item)

    @timed("dequeue")
    def dequeue(self) -> Any:
        """Remove and return the first item from the queue."""
        return self._list.removefirst()

    @timed("peek")
    def peek(self) -> Any:
        """Return the first item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek from empty queue")
        return self._list.peek()

    @timed("is_empty")
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._list) == 0

    @timed("size")
    def size(self) -> int:
        """Get the number of items in the queue."""
        return len(self._list)

    @timed("length")
    def __len__(self) -> int:
        """Return the length of the queue."""
        return len(self._list)

    @timed("add")
    def __add__(self, other: "Queue") -> "Queue":
        """Concatenate two queues and return a new combined queue."""
        result = Queue()

        # Handle empty queue cases
        if self.is_empty():
            result._list._head = other._list._head
            result._list._tail = other._list._tail
            result._list._length = other._list._length
            return result
        if other.is_empty():
            result._list._head = self._list._head
            result._list._tail = self._list._tail
            result._list._length = self._list._length
            return result

        # Link the two lists together
        result._list._head = self._list._head
        result._list._tail = other._list._tail
        result._list._length = self._list._length + other._list._length

        # Connect the lists
        self._list._tail.link = other._list._head
        other._list._head.prev = self._list._tail

        return result

    @timed("iadd")
    def __iadd__(self, other: "Queue") -> "Queue":
        """Concatenate another queue to this queue in-place."""
        if not other.is_empty():
            if self.is_empty():
                self._list._head = other._list._head
                self._list._tail = other._list._tail
                self._list._length = other._list._length
            else:
                # Link the lists together
                self._list._tail.link = other._list._head
                other._list._head.prev = self._list._tail
                self._list._tail = other._list._tail
                self._list._length += other._list._length

            # Clear other queue
            other._list._head = None
            other._list._tail = None
            other._list._length = 0
        return self
