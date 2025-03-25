class DLLNode:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None

class DLLQueue:
    def __init__(self):
        self.head = self.tail = None

    def addFirst(self, value):
        new_node = DLLNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addLast(self, value):
        new_node = DLLNode(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def removeFirst(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return value

    def removeLast(self):
        if not self.tail:
            return None
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value

    def __add__(self, other):
        if isinstance(other, DLLQueue):
            new_queue = DLLQueue()
            current = self.head
            while current:
                new_queue.addLast(current.value)
                current = current.next
            current = other.head
            while current:
                new_queue.addLast(current.value)
                current = current.next
            return new_queue
        raise TypeError("Can only add another DLLQueue.")

    def __iadd__(self, other):
        if isinstance(other, DLLQueue):
            current = other.head
            while current:
                self.addLast(current.value)
                current = current.next
            return self
        raise TypeError("Can only use += with another DLLQueue.")
