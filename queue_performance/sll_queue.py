class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLLQueue:
    def __init__(self):
        self.head = self.tail = None

    def addFirst(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addLast(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def removeFirst(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def removeLast(self):
        if not self.head:
            return None
        if self.head == self.tail:
            value = self.head.value
            self.head = self.tail = None
            return value
        current = self.head
        while current.next != self.tail:
            current = current.next
        value = self.tail.value
        self.tail = current
        self.tail.next = None
        return value

    def __add__(self, other):
        if isinstance(other, SLLQueue):
            new_queue = SLLQueue()
            current = self.head
            while current:
                new_queue.addLast(current.value)
                current = current.next
            current = other.head
            while current:
                new_queue.addLast(current.value)
                current = current.next
            return new_queue
        raise TypeError("Can only add another SLLQueue.")

    def __iadd__(self, other):
        if isinstance(other, SLLQueue):
            current = other.head
            while current:
                self.addLast(current.value)
                current = current.next
            return self
        raise TypeError("Can only use += with another SLLQueue.")
