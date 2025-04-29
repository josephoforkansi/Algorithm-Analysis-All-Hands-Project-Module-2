from typing import Any, List

class ArrayQueue:
    """Basic Array-based Queue implementation using a Python list."""

    def __init__(self, capacity: int = 10):
        """Initialize an empty queue with a given capacity."""
        self.items: List[Any] = [None] * capacity
        self.front: int = 0
        self.rear: int = 0
        self.count: int = 0
        self.capacity: int = capacity

    def enqueue(self, value: Any) -> None:
        """Add an element to the end of the queue. O(1) amortized, O(n) worst-case (resize)."""
        if self.count == self.capacity:
            self._resize(2 * self.capacity)
        self.items[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

    def dequeue(self) -> Any:
        """Remove and return the first element from the queue. O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.items[self.front]
        self.items[self.front] = None  # Help with garbage collection
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value

    def peek(self) -> Any:
        """Return the first element without removing it. O(1)."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.front]

    def size(self) -> int:
        """Return the number of elements in the queue."""
        return self.count

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self.count == 0

    def removelast(self) -> Any:
        """Remove and return the last element from the queue. O(1)."""
        if self.is_empty():
            raise IndexError("removelast from empty queue")
        last_index = (self.rear - 1 + self.capacity) % self.capacity
        value = self.items[last_index]
        self.items[last_index] = None
        self.rear = last_index
        self.count -= 1
        return value

    def _resize(self, new_capacity: int) -> None:
        """Resize the underlying array."""
        temp = [None] * new_capacity
        for i in range(self.count):
            index = (self.front + i) % self.capacity
            temp[i] = self.items[index]
        self.items = temp
        self.front = 0
        self.rear = self.count
        self.capacity = new_capacity

    def __add__(self, other: "ArrayQueue") -> "ArrayQueue":
        """Concatenate two queues. O(n + m) operation."""
        result = ArrayQueue(self.count + other.count)
        for i in range(self.count):
            result.enqueue(self.items[(self.front + i) % self.capacity])
        for i in range(other.count):
            result.enqueue(other.items[(other.front + i) % other.capacity])
        return result

    def __iadd__(self, other: "ArrayQueue") -> "ArrayQueue":
        """Concatenate another queue to this queue. O(m) amortized, O(n*m) worst-case."""
        for i in range(other.count):
            self.enqueue(other.items[(other.front + i) % other.capacity])
        return self
