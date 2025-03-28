"""Test cases for the list queue implementation."""

import pytest
from analyze.ListQueue import ListQueueDisplay


def test_init():
    """Test queue initialization."""
    queue = ListQueueDisplay()
    assert len(queue) == 0
    assert queue.is_empty() is True


def test_enqueue():
    """Test adding items to the queue."""
    queue = ListQueueDisplay()
    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.is_empty() is False


def test_dequeue():
    """Test removing items from the queue."""
    queue = ListQueueDisplay()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert len(queue) == 1
    assert queue.dequeue() == 2
    assert queue.is_empty() is True


def test_peek():
    """Test peeking at the first item without removing it."""
    queue = ListQueueDisplay()
    queue.enqueue(1)
    assert queue.peek() == 1
    assert len(queue) == 1
    assert queue.dequeue() == 1


def test_multiple_operations():
    """Test a sequence of queue operations."""
    queue = ListQueueDisplay()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert len(queue) == 3
    assert queue.peek() == 1
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert len(queue) == 1
    queue.enqueue(4)
    assert len(queue) == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() == 4
    assert queue.is_empty() is True


def test_empty_queue_operations():
    """Test operations on an empty queue."""
    queue = ListQueueDisplay()
    with pytest.raises(IndexError):
        queue.peek()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert len(queue) == 0
    assert queue.is_empty() is True


def test_queue_add():
    """Test the addition of two queues."""
    queue1 = ListQueueDisplay()
    queue2 = ListQueueDisplay()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue2.enqueue(3)
    queue2.enqueue(4)
    
    concatenated_queue = queue1 + queue2
    assert len(concatenated_queue) == 4
    assert concatenated_queue.dequeue() == 1
    assert concatenated_queue.dequeue() == 2
    assert concatenated_queue.dequeue() == 3
    assert concatenated_queue.dequeue() == 4
    assert concatenated_queue.is_empty() is True


def test_queue_iadd():
    """Test in-place addition of two queues."""
    queue1 = ListQueueDisplay()
    queue2 = ListQueueDisplay()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue2.enqueue(3)
    queue2.enqueue(4)
    
    queue1 += queue2
    assert len(queue1) == 4
    assert queue1.dequeue() == 1
    assert queue1.dequeue() == 2
    assert queue1.dequeue() == 3
    assert queue1.dequeue() == 4
    assert queue1.is_empty() is True
