class ArrayQueue:
    def __init__(self):
        self.queue = []

    def addFirst(self, value):
        self.queue.insert(0, value)

    def addLast(self, value):
        self.queue.append(value)

    def removeFirst(self):
        return self.queue.pop(0) if self.queue else None

    def removeLast(self):
        return self.queue.pop() if self.queue else None

    def __add__(self, other):
        if isinstance(other, ArrayQueue):
            new_queue = ArrayQueue()
            new_queue.queue = self.queue + other.queue
            return new_queue
        raise TypeError("Can only add another ArrayQueue.")

    def __iadd__(self, other):
        if isinstance(other, ArrayQueue):
            self.queue += other.queue
            return self
        raise TypeError("Can only use += with another ArrayQueue.")
