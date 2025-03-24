"""Implementation of a queue using a list with a head pointer for efficient dequeuing."""

class ListQueueDisplay:
    """A queue implementation using a list with a head pointer and display functionality."""
    def __init__(self):
        # Initialize head index and underlying list
        self._head = 0
        self._L = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        # Add item to the end of the list
        self._L.append(item)

    def peek(self):
        """Return the first item in the queue without removing it."""
        # Return the item at the head index without removing it
        return self._L[self._head]

    def dequeue(self):
        """Remove and return the first item from the queue."""
        # Get the item at the head and increment head index
        item = self.peek()
        self._head += 1
        return item

    def __len__(self):
        """Return the number of items currently in the queue."""
        # Return the number of items between head and end of list
        return len(self._L) - self._head

    def isempty(self):
        """Check if the queue is empty."""
        # Check if there are any items between head and end
        return len(self) == 0

    def __str__(self):
        """Return a string representation of the queue contents."""
        # Return string representation of items from head to end
        return str(self._L[self._head:])