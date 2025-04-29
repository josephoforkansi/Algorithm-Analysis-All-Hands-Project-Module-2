""" "Implementation of a singly linked list."""


class Node:
    """Represents a node in the singly linked list."""

    def __init__(self, data):
        self.data = data
        self.link = None


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def is_empty(self):
        """Checks if the list is empty."""
        return self._head is None

    def addfirst(self, data):
        """Adds a new node with the given data to the beginning of the list."""
        new_node = Node(data)
        if self.is_empty():
            self._tail = new_node
        new_node.link = self._head
        self._head = new_node
        self._length += 1

        assert self._head is not None, "Head should not be None after adding"
        assert self._length > 0, "Length should be greater than 0 after adding"

    def addlast(self, data):
        """Adds a new node with the given data to the end of the list."""
        new_node = Node(data)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.link = new_node
            self._tail = new_node
        self._length += 1

    def removefirst(self):
        item = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        self._length -= 1
        return item

    def removelast(self):
        """Removes and returns the data from the last node of the list."""
        if self.is_empty():
            return None
        if self._head == self._tail:
            data = self._head.data
            self._head = None
            self._tail = None
            self._length = 0
            return data
        current = self._head
        while current.link != self._tail:
            current = current.link
        data = self._tail.data
        current.link = None
        self._tail = current
        self._length -= 1
        return data

    def __len__(self):
        """Returns the length of the list."""
        return self._length

    def __add__(self, other):
        """Concatenates two singly linked lists, returning a new list."""
        new_list = SinglyLinkedList()
        if self._head:
            new_list._head = Node(self._head.data)
            current = self._head.link
            new_list_current = new_list._head
            while current:
                new_node = Node(current.data)
                new_list_current.link = new_node
                new_list_current = new_node
                current = current.link
            new_list._tail = new_list_current
            new_list._length = self._length

            if other._head:
                new_list._tail.link = Node(other._head.data)
                current = other._head.link
                new_list_current = new_list._tail.link
                while current:
                    new_node = Node(current.data)
                    new_list_current.link = new_node
                    new_list_current = new_node
                    current = current.link
                new_list._tail = new_list_current
                new_list._length += other._length
        elif other._head:
            new_list = other.__copy__()
        return new_list

    def __copy__(self):
        """Creates a shallow copy of the singly linked list."""
        new_list = SinglyLinkedList()
        if self._head:
            new_list._head = Node(self._head.data)
            current = self._head.link
            new_list_current = new_list._head
            while current:
                new_node = Node(current.data)
                new_list_current.link = new_node
                new_list_current = new_node
                current = current.link
            new_list._tail = new_list_current
            new_list._length = self._length
        return new_list

    def __iadd__(self, other):
        """In-place concatenation of two singly linked lists."""
        if other._head is not None:
            if self._head is None:
                self._head = other._head
                self._tail = other._tail
            else:
                self._tail.link = other._head
                self._tail = other._tail
            self._length += other._length
            # Empty the other list manually
            other._head = None
            other._tail = None
            other._length = 0
        return self

    def __str__(self):
        """Returns a string representation of the list."""
        elements = []
        current = self._head
        while current:
            elements.append(str(current.data))
            current = current.link
        return " -> ".join(elements)
