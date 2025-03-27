"""Test cases for the singly linked list queue implementation."""

import pytest
from analyze.SLL import LinkedQueue


def test_queue_init():
    """Test queue initialization."""
    queue = LinkedQueue()
    assert len(queue) == 0
    assert queue.is_empty() == True


def test_queue_fifo_behavior():
    """Test that the queue follows FIFO (First-In-First-Out) behavior."""
    queue = LinkedQueue()

    # Test basic FIFO
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1  # First in should be first out
    assert queue.dequeue() == 2  # Second in should be second out
    assert queue.dequeue() == 3  # Third in should be third out

    # Test FIFO with mixed operations
    queue.enqueue("A")
    queue.enqueue("B")
    assert queue.peek() == "A"  # Should see first item without removing
    assert queue.dequeue() == "A"  # Should get first item
    queue.enqueue("C")
    assert queue.dequeue() == "B"  # Should get second item
    assert queue.dequeue() == "C"  # Should get third item

    # Test empty queue
    assert queue.is_empty()
    with pytest.raises(IndexError):
        queue.dequeue()
    with pytest.raises(IndexError):
        queue.peek()


def test_queue_operations():
    """Test all queue operations."""
    queue = LinkedQueue()

    # Test enqueue
    queue.enqueue(1)
    assert len(queue) == 1
    assert not queue.is_empty()

    # Test peek
    assert queue.peek() == 1
    assert len(queue) == 1  # Peek shouldn't change size

    # Test dequeue
    assert queue.dequeue() == 1
    assert queue.is_empty()

    # Test size
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.size() == 2
    assert len(queue) == 2


def test_queue_concatenation():
    """Test queue concatenation operations."""
    queue1 = LinkedQueue()
    queue2 = LinkedQueue()

    # Fill queues
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue2.enqueue(3)
    queue2.enqueue(4)

    # Test addition
    combined = queue1 + queue2
    assert combined.dequeue() == 1  # First from first queue
    assert combined.dequeue() == 2  # Second from first queue
    assert combined.dequeue() == 3  # First from second queue
    assert combined.dequeue() == 4  # Second from second queue
    assert combined.is_empty()

    # Test in-place addition
    queue1 += queue2
    assert queue1.dequeue() == 1
    assert queue1.dequeue() == 2
    assert queue1.dequeue() == 3
    assert queue1.dequeue() == 4
    assert queue1.is_empty()


def test_queue_edge_cases():
    """Test edge cases and error conditions."""
    queue = LinkedQueue()

    # Test operations on empty queue
    assert queue.is_empty()
    assert len(queue) == 0
    with pytest.raises(IndexError):
        queue.dequeue()
    with pytest.raises(IndexError):
        queue.peek()

    # Test single element
    queue.enqueue(1)
    assert not queue.is_empty()
    assert len(queue) == 1
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.is_empty()

    # Test multiple enqueue/dequeue cycles
    for i in range(5):
        queue.enqueue(i)
        assert queue.dequeue() == i
        assert queue.is_empty()
