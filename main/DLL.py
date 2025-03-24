"""A doubly linked list implementation with a Queue interface."""

from typing import Any, Optional


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

    def __len__(self) -> int:
        """Return the length of the list."""
        return self._length

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

    def addfirst(self, item: Any) -> None:
        """Add an item to the front of the list."""
        self._addbetween(item, None, self._head)

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

    def removefirst(self) -> Any:
        """Remove and return the first item in the list."""
        if self._head is None:
            raise IndexError("Cannot remove from empty list")
        return self._remove(self._head)

    def removelast(self) -> Any:
        """Remove and return the last item in the list."""
        if self._tail is None:
            raise IndexError("Cannot remove from empty list")
        return self._remove(self._tail)


class Queue:
    """A queue implementation using a doubly linked list."""

    def __init__(self) -> None:
        """Initialize an empty queue."""
        # Use doubly linked list as underlying data structure
        self._list: DoublyLinkedList = DoublyLinkedList()

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._list.addlast(item)

    def dequeue(self) -> Any:
        """Remove and return the first item from the queue."""
        return self._list.removefirst()

    def peek(self) -> Any:
        """Return the first item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek from empty queue")
        # Temporarily remove and re-add to peek without modifying structure
        item = self._list.removefirst()
        self._list.addfirst(item)
        return item

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._list) == 0

    def size(self) -> int:
        """Get the number of items in the queue."""
        return len(self._list)

    def __len__(self) -> int:
        """Return the length of the queue."""
        return len(self._list)
