"""Test cases for the ListQueueDisplay implementation."""

import pytest
from main.ListQueue import ListQueueDisplay

def test_init():
    """Test queue initialization."""
    queue = ListQueueDisplay()
    assert len(queue) == 0
    assert queue.isempty() == True

def test_enqueue():
    """Test adding items to the queue."""
    queue = ListQueueDisplay()
    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.isempty() == False
    assert str(queue) == "[1]"

def test_dequeue():
    """Test removing items from the queue."""
    queue = ListQueueDisplay()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert len(queue) == 1
    assert queue.dequeue() == 2
    assert queue.isempty() == True

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
    assert queue.isempty() == True

def test_empty_queue_operations():
    """Test operations on an empty queue."""
    queue = ListQueueDisplay()
    with pytest.raises(IndexError):
        queue.peek()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert len(queue) == 0
    assert queue.isempty() == True
