"""Test cases for the singly linked list and queue implementations."""

import pytest
from main.SLL import LinkedListPrime, LinkedQueue


# LinkedListPrime Tests
def test_list_init():
    """Test list initialization."""
    lst = LinkedListPrime()
    assert len(lst) == 0


def test_addfirst():
    """Test adding items to the front of the list."""
    lst = LinkedListPrime()
    lst.addfirst(1)
    assert len(lst) == 1
    lst.addfirst(2)
    assert len(lst) == 2
    assert lst.removefirst() == 2
    assert lst.removefirst() == 1


def test_addlast():
    """Test adding items to the end of the list."""
    lst = LinkedListPrime()
    lst.addlast(1)
    assert len(lst) == 1
    lst.addlast(2)
    assert len(lst) == 2
    assert lst.removelast() == 2
    assert lst.removelast() == 1


def test_removefirst():
    """Test removing items from the front of the list."""
    lst = LinkedListPrime()
    lst.addfirst(1)
    lst.addfirst(2)
    assert lst.removefirst() == 2
    assert lst.removefirst() == 1
    assert len(lst) == 0


def test_removelast():
    """Test removing items from the end of the list."""
    lst = LinkedListPrime()
    lst.addlast(1)
    lst.addlast(2)
    assert lst.removelast() == 2
    assert lst.removelast() == 1
    assert len(lst) == 0


def test_list_concatenation():
    """Test list concatenation operations."""
    lst1 = LinkedListPrime()
    lst2 = LinkedListPrime()
    lst1.addlast(1)
    lst1.addlast(2)
    lst2.addlast(3)
    lst2.addlast(4)

    # Test __add__
    result = lst1 + lst2
    assert len(result) == 4
    assert result.removefirst() == 1
    assert result.removefirst() == 2
    assert result.removefirst() == 3
    assert result.removefirst() == 4

    # Test __iadd__
    lst1 += lst2
    assert len(lst1) == 4
    assert lst1.removefirst() == 1
    assert lst1.removefirst() == 2
    assert lst1.removefirst() == 3
    assert lst1.removefirst() == 4


# LinkedQueue Tests
def test_queue_init():
    """Test queue initialization."""
    queue = LinkedQueue()
    assert len(queue) == 0
    assert queue.isempty() == True


def test_queue_enqueue():
    """Test adding items to the queue."""
    queue = LinkedQueue()
    queue.enqueue(1)
    assert len(queue) == 1
    assert queue.isempty() == False


def test_queue_dequeue():
    """Test removing items from the queue."""
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert len(queue) == 1
    assert queue.dequeue() == 2
    assert queue.isempty() == True


def test_queue_peek():
    """Test peeking at the first item without removing it."""
    queue = LinkedQueue()
    queue.enqueue(1)
    assert queue.peek() == 1
    assert len(queue) == 1
    assert queue.dequeue() == 1


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
    assert queue.isempty() == True


def test_empty_queue_operations():
    """Test operations on an empty queue."""
    queue = LinkedQueue()
    with pytest.raises(IndexError):
        queue.peek()
    with pytest.raises(IndexError):
        queue.dequeue()
    assert len(queue) == 0
    assert queue.isempty() == True
