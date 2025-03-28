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
    assert queue.is_empty() is True


def test_enqueue():
    """Test adding items to the queue."""
    queue = Queue()
    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.is_empty() is False
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
    assert queue.is_empty() is True


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
    assert queue.is_empty() is True


def test_empty_queue_operations():
    """Test operations on an empty queue."""
    queue = Queue()
    with pytest.raises(IndexError):
        queue.peek()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert len(queue) == 0
    assert queue.is_empty() is True


def test_add_front():
    """Test adding items to the front of the doubly linked list."""
    lst = DoublyLinkedList()
    lst.add_front(1)
    assert len(lst) == 1
    lst.add_front(2)
    assert len(lst) == 2
    assert lst.head.data == 2


def test_add_back():
    """Test adding items to the back of the doubly linked list."""
    lst = DoublyLinkedList()
    lst.add_back(1)
    assert len(lst) == 1
    lst.add_back(2)
    assert len(lst) == 2
    assert lst.tail.data == 2


def test_remove_front():
    """Test removing items from the front of the doubly linked list."""
    lst = DoublyLinkedList()
    lst.add_front(1)
    lst.add_front(2)
    assert lst.remove_front() == 2
    assert len(lst) == 1


def test_remove_back():
    """Test removing items from the back of the doubly linked list."""
    lst = DoublyLinkedList()
    lst.add_back(1)
    lst.add_back(2)
    assert lst.remove_back() == 2
    assert len(lst) == 1


def test_traversal():
    """Test forward and backward traversal of the doubly linked list."""
    lst = DoublyLinkedList()
    lst.add_front(1)
    lst.add_back(2)
    lst.add_back(3)
    assert lst.traverse_forward() == [1, 2, 3]
    assert lst.traverse_backward() == [3, 2, 1]
