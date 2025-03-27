"""Test cases for the doubly linked list and queue implementations."""

import pytest
from analyze.DLL import DoublyLinkedList, Queue


# DoublyLinkedList Tests
def test_list_init():
    """Test list initialization."""
    lst = DoublyLinkedList()
    assert len(lst) == 0


# Queue Tests
def test_queue_init():
    """Test queue initialization."""
    queue = Queue()
    assert len(queue) == 0
    assert queue.is_empty() == True


def test_enqueue():
    """Test adding items to the queue."""
    queue = Queue()
    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.is_empty() == False
    queue.enqueue(2)
    assert len(queue) == 2
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2


def test_dequeue():
    """Test removing items from the queue."""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert len(queue) == 1
    assert queue.dequeue() == 2
    assert queue.is_empty() == True


def test_peek():
    """Test peeking at the first item without removing it."""
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1
    assert len(queue) == 1
    assert queue.dequeue() == 1


def test_queue_multiple_operations():
    """Test a sequence of queue operations."""
    queue = Queue()
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
    queue = Queue()
    with pytest.raises(IndexError):
        queue.peek()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert len(queue) == 0
    assert queue.is_empty() == True
