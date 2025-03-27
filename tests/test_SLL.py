"""Test cases for the singly linked list and queue implementations."""

import pytest
from analyze.SLL import LinkedListPrime, LinkedQueue


# LinkedListPrime Tests
def test_list_init():
    """Test list initialization."""
    lst = LinkedListPrime()
    assert len(lst) == 0
    assert lst.is_empty() == True


# LinkedQueue Tests
def test_queue_init():
    """Test queue initialization."""
    queue = LinkedQueue()
    assert len(queue) == 0
    assert queue.is_empty() == True


def test_queue_enqueue():
    """Test adding items to the queue."""
    queue = LinkedQueue()
    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.is_empty() == False


def test_queue_dequeue():
    """Test removing items from the queue."""
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert len(queue) == 1
    assert queue.dequeue() == 2
    assert queue.is_empty() == True


def test_queue_peek():
    """Test peeking at the front of the queue."""
    queue = LinkedQueue()
    queue.enqueue(1)
    assert queue.peek() == 1
    assert len(queue) == 1


def test_queue_multiple_operations():
    """Test a sequence of queue operations."""
    queue = LinkedQueue()
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
    assert queue.is_empty() == True


def test_empty_queue_operations():
    """Test operations on an empty queue."""
    queue = LinkedQueue()
    with pytest.raises(IndexError):
        queue.peek()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert len(queue) == 0
    assert queue.is_empty() == True
