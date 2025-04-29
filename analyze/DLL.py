""" "A doubly linked list implementation with O(1) concatenation."""


class ListNode:
    """Represents a node in the doubly linked list."""

    def __init__(self, data, prev=None, link=None):
        """Initializes a new ListNode."""
        self.data = data
        self.prev = prev
        self.link = link
        # No automatic linking in the ListNode constructor


class DoublyLinkedList:
    """Represents a doubly linked list with O(1) concatenation."""

    def __init__(self):
        """Initializes an empty DoublyLinkedList."""
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        """Returns the length of the list."""
        return self._length

    def _addbetween(self, item, before, after):
        """Adds a new node with item between before and after."""
        new_node = ListNode(item, before, after)
        if before is None:
            self._head = new_node
        else:
            before.link = new_node
        if after is None:
            self._tail = new_node
        else:
            after.prev = new_node
        self._length += 1

        assert self._length > 0, "List length should be positive after adding"
        assert self._head is not None or self._length == 0, (
            "Head should not be None if list is not empty"
        )
        assert self._tail is not None or self._length == 0, (
            "Tail should not be None if list is not empty"
        )

    def addfirst(self, item):
        """Adds a new node with item to the beginning of the list."""
        self._addbetween(item, None, self._head)

    def addlast(self, item):
        """Adds a new node with item to the end of the list."""
        self._addbetween(item, self._tail, None)

    def _remove(self, node):
        """Removes the given node from the list."""
        before, after = node.prev, node.link
        if before is None:
            self._head = after
            if self._head is None:
                self._tail = None
        else:
            before.link = after
        if after is None:
            self._tail = before
            if self._tail is None:
                self._head = None
        else:
            after.prev = before
        self._length -= 1
        return node.data

    def removefirst(self):
        """Removes and returns the data from the first node."""
        if self._head is None:
            raise IndexError("remove from empty list")
        return self._remove(self._head)

    def removelast(self):
        """Removes and returns the data from the last node."""
        if self._tail is None:
            raise IndexError("remove from empty list")
        return self._remove(self._tail)

    def concatenate(self, other):
        """Concatenates two DoublyLinkedList in O(1) time (modifies self)."""
        if not isinstance(other, DoublyLinkedList):
            raise TypeError(
                "Can only concatenate DoublyLinkedList with another DoublyLinkedList"
            )

        if other._head is None:
            return self  # Nothing to add from the other list

        if self._head is None:
            self._head = other._head
            self._tail = other._tail
            self._length = other._length
        else:
            self._tail.link = other._head
            other._head.prev = self._tail
            self._tail = other._tail
            self._length += other._length

        # Reset the other list
        other._head = None
        other._tail = None
        other._length = 0

        return self

    def __add__(self, other):
        """Concatenates two DoublyLinkedList in O(1) time (modifies self)."""
        return self.concatenate(other)

    def __iadd__(self, other):
        """In-place concatenation of two DoublyLinkedList (O(1))."""
        return self.concatenate(other)

    def clear(self):
        """Clears the entire list."""
        self._head = None
        self._tail = None
        self._length = 0

    def __str__(self):
        """Returns a string representation of the list."""
        elements = []
        current = self._head
        while current:
            elements.append(str(current.data))
            current = current.link
        return " <-> ".join(elements)

    def __repr__(self):
        """Returns a string representation of the list for debugging."""
        return f"DoublyLinkedList(head={self._head.data if self._head else None}, tail={self._tail.data if self._tail else None}, length={self._length})"
