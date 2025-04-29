import pytest

from analyze.dll_queue import BasicDLLQueue


class TestBasicDLLQueue:

    @pytest.fixture
    def empty_queue(self):
        """Fixture to provide an empty BasicDLLQueue."""
        return BasicDLLQueue()

    @pytest.fixture
    def single_item_queue(self):
        """Fixture to provide a BasicDLLQueue with one item."""
        queue = BasicDLLQueue()
        queue.enqueue(1)
        return queue

    @pytest.fixture
    def multi_item_queue(self):
        """Fixture to provide a BasicDLLQueue with multiple items."""
        queue = BasicDLLQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        return queue

    def test_enqueue_empty(self, empty_queue):
        """Test enqueueing into an empty queue."""
        empty_queue.enqueue(1)
        assert not empty_queue.is_empty()
        assert len(empty_queue) == 1
        assert empty_queue._head.data == 1
        assert empty_queue._tail.data == 1
        assert empty_queue._head.prev is None
        assert empty_queue._head.next is None

    def test_enqueue_multiple(self, empty_queue):
        """Test enqueueing multiple items."""
        empty_queue.enqueue(1)
        empty_queue.enqueue(2)
        empty_queue.enqueue(3)
        assert not empty_queue.is_empty()
        assert len(empty_queue) == 3
        assert empty_queue._head.data == 1
        assert empty_queue._tail.data == 3
        assert empty_queue._head.next.data == 2
        assert empty_queue._tail.prev.data == 2

    def test_dequeue_empty(self, empty_queue):
        """Test dequeueing from an empty queue."""
        with pytest.raises(IndexError):
            empty_queue.dequeue()

    def test_dequeue_single(self, single_item_queue):
        """Test dequeueing from a queue with one item."""
        item = single_item_queue.dequeue()
        assert item == 1
        assert single_item_queue.is_empty()
        assert len(single_item_queue) == 0
        assert single_item_queue._head is None
        assert single_item_queue._tail is None

    def test_dequeue_multiple(self, multi_item_queue):
        """Test dequeueing multiple items."""
        item1 = multi_item_queue.dequeue()
        assert item1 == 1
        assert len(multi_item_queue) == 2
        assert multi_item_queue._head.data == 2
        assert multi_item_queue._head.prev is None

        item2 = multi_item_queue.dequeue()
        assert item2 == 2
        assert len(multi_item_queue) == 1
        assert multi_item_queue._head.data == 3
        assert multi_item_queue._tail.data == 3
        assert multi_item_queue._head.next is None
        assert multi_item_queue._tail.prev is None

        item3 = multi_item_queue.dequeue()
        assert item3 == 3
        assert multi_item_queue.is_empty()

    def test_peek_empty(self, empty_queue):
        """Test peeking at an empty queue."""
        with pytest.raises(IndexError):
            empty_queue.peek()

    def test_peek_single(self, single_item_queue):
        """Test peeking at a queue with one item."""
        item = single_item_queue.peek()
        assert item == 1
        assert not single_item_queue.is_empty()
        assert len(single_item_queue) == 1

    def test_peek_multiple(self, multi_item_queue):
        """Test peeking at a queue with multiple items."""
        item = multi_item_queue.peek()
        assert item == 1
        assert not multi_item_queue.is_empty()
        assert len(multi_item_queue) == 3
        assert multi_item_queue._head.data == 1

    def test_is_empty(self, empty_queue, single_item_queue):
        """Test the is_empty method."""
        assert empty_queue.is_empty()
        assert not single_item_queue.is_empty()
        single_item_queue.dequeue()
        assert single_item_queue.is_empty()

    def test_len(self, empty_queue, single_item_queue, multi_item_queue):
        """Test the __len__ method."""
        assert len(empty_queue) == 0
        assert len(single_item_queue) == 1
        assert len(multi_item_queue) == 3
        multi_item_queue.dequeue()
        assert len(multi_item_queue) == 2

    def test_add_empty_empty(self, empty_queue):
        """Test adding two empty queues."""
        other_queue = BasicDLLQueue()
        new_queue = empty_queue + other_queue
        assert isinstance(new_queue, BasicDLLQueue)
        assert new_queue.is_empty()
        assert len(new_queue) == 0
        assert empty_queue.is_empty()
        assert other_queue.is_empty()

    def test_add_empty_non_empty(self, empty_queue, multi_item_queue):
        """Test adding an empty queue to a non-empty queue."""
        new_queue = empty_queue + multi_item_queue
        assert isinstance(new_queue, BasicDLLQueue)
        assert not new_queue.is_empty()
        assert len(new_queue) == 3
        assert new_queue.dequeue() == 1
        assert new_queue.dequeue() == 2
        assert new_queue.dequeue() == 3
        assert empty_queue.is_empty()
        assert not multi_item_queue.is_empty()
        assert len(multi_item_queue) == 3

    def test_add_non_empty_empty(self, multi_item_queue, empty_queue):
        """Test adding a non-empty queue to an empty queue."""
        new_queue = multi_item_queue + empty_queue
        assert isinstance(new_queue, BasicDLLQueue)
        assert not new_queue.is_empty()
        assert len(new_queue) == 3
        assert new_queue.dequeue() == 1
        assert new_queue.dequeue() == 2
        assert new_queue.dequeue() == 3
        assert not multi_item_queue.is_empty()
        assert len(multi_item_queue) == 3
        assert empty_queue.is_empty()

    def test_add_non_empty_non_empty(self, single_item_queue, multi_item_queue):
        """Test adding two non-empty queues."""
        new_queue = single_item_queue + multi_item_queue
        assert isinstance(new_queue, BasicDLLQueue)
        assert not new_queue.is_empty()
        assert len(new_queue) == 4
        assert new_queue.dequeue() == 1
        assert new_queue.dequeue() == 1  # From single_item_queue
        assert new_queue.dequeue() == 2  # From multi_item_queue
        assert new_queue.dequeue() == 3  # From multi_item_queue
        assert not single_item_queue.is_empty()
        assert len(single_item_queue) == 1
        assert not multi_item_queue.is_empty()
        assert len(multi_item_queue) == 3

    def test_iadd_empty_empty(self, empty_queue):
        """Test in-place addition of two empty queues."""
        other_queue = BasicDLLQueue()
        initial_id = id(empty_queue)
        empty_queue += other_queue
        assert id(empty_queue) == initial_id
        assert empty_queue.is_empty()
        assert len(empty_queue) == 0
        assert other_queue.is_empty()

    def test_iadd_empty_non_empty(self, empty_queue, multi_item_queue):
        """Test in-place addition of an empty queue to a non-empty queue."""
        initial_id = id(empty_queue)
        empty_queue += multi_item_queue
        assert id(empty_queue) == initial_id
        assert not empty_queue.is_empty()
        assert len(empty_queue) == 3
        assert empty_queue.dequeue() == 1
        assert empty_queue.dequeue() == 2
        assert empty_queue.dequeue() == 3
        assert multi_item_queue.is_empty()
        assert len(multi_item_queue) == 0

    def test_iadd_non_empty_empty(self, single_item_queue, empty_queue):
        """Test in-place addition of a non-empty queue to an empty queue."""
        initial_id = id(single_item_queue)
        single_item_queue += empty_queue
        assert id(single_item_queue) == initial_id
        assert not single_item_queue.is_empty()
        assert len(single_item_queue) == 1
        assert single_item_queue.dequeue() == 1
        assert empty_queue.is_empty()
        assert len(empty_queue) == 0

    def test_iadd_non_empty_non_empty(self, single_item_queue, multi_item_queue):
        """Test in-place addition of two non-empty queues."""
        initial_id = id(single_item_queue)
        single_item_queue += multi_item_queue
        assert id(single_item_queue) == initial_id
        assert not single_item_queue.is_empty()
        assert len(single_item_queue) == 4
        assert single_item_queue.dequeue() == 1
        assert single_item_queue.dequeue() == 1  # From original single_item_queue
        assert single_item_queue.dequeue() == 2  # From multi_item_queue
        assert single_item_queue.dequeue() == 3  # From multi_item_queue
        assert multi_item_queue.is_empty()
        assert len(multi_item_queue) == 0
