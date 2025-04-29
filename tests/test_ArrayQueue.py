import pytest

from analyze.ArrayQueue import ArrayQueue


class TestArrayQueue:

    @pytest.fixture
    def empty_queue(self):
        """Fixture to provide an empty ArrayQueue."""
        return ArrayQueue()

    @pytest.fixture
    def single_item_queue(self):
        """Fixture to provide an ArrayQueue with one item."""
        queue = ArrayQueue()
        queue.enqueue(1)
        return queue

    @pytest.fixture
    def multi_item_queue(self):
        """Fixture to provide an ArrayQueue with multiple items."""
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        return queue

    @pytest.fixture
    def full_queue(self):
        """Fixture to provide a full ArrayQueue (at initial capacity)."""
        queue = ArrayQueue(capacity=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        return queue

    def test_enqueue_empty(self, empty_queue):
        """Test enqueueing into an empty queue."""
        empty_queue.enqueue(1)
        assert not empty_queue.is_empty()
        assert empty_queue.size() == 1
        assert empty_queue.items[empty_queue.front] == 1
        assert empty_queue.front == 0
        assert empty_queue.rear == 1

    def test_enqueue_multiple(self, empty_queue):
        """Test enqueueing multiple items."""
        empty_queue.enqueue(1)
        empty_queue.enqueue(2)
        empty_queue.enqueue(3)
        assert not empty_queue.is_empty()
        assert empty_queue.size() == 3
        assert empty_queue.items[0] == 1
        assert empty_queue.items[1] == 2
        assert empty_queue.items[2] == 3
        assert empty_queue.front == 0
        assert empty_queue.rear == 3

    def test_enqueue_resize(self, full_queue):
        """Test enqueueing into a full queue triggers resizing."""
        initial_capacity = full_queue.capacity
        full_queue.enqueue(4)
        assert full_queue.capacity == 2 * initial_capacity
        assert full_queue.size() == 4
        assert full_queue.items[0] == 1
        assert full_queue.items[1] == 2
        assert full_queue.items[2] == 3
        assert full_queue.items[3] == 4
        assert full_queue.front == 0
        assert full_queue.rear == 4

    def test_enqueue_wraparound(self):
        """Test enqueueing with wraparound."""
        queue = ArrayQueue(capacity=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.dequeue()
        queue.enqueue(3)
        queue.enqueue(4)
        assert queue.size() == 2
        assert queue.items[0] == 3
        assert queue.items[1] == 4
        assert queue.front == 0
        assert queue.rear == 2

    def test_dequeue_empty(self, empty_queue):
        """Test dequeueing from an empty queue."""
        with pytest.raises(IndexError, match="Queue is empty"):
            empty_queue.dequeue()

    def test_dequeue_single(self, single_item_queue):
        """Test dequeueing from a queue with one item."""
        item = single_item_queue.dequeue()
        assert item == 1
        assert single_item_queue.is_empty()
        assert single_item_queue.size() == 0
        assert single_item_queue.items[single_item_queue.front - 1] is None
        assert single_item_queue.front == 1
        assert single_item_queue.rear == 1

    def test_dequeue_multiple(self, multi_item_queue):
        """Test dequeueing multiple items."""
        item1 = multi_item_queue.dequeue()
        assert item1 == 1
        assert multi_item_queue.size() == 2
        assert multi_item_queue.front == 1

        item2 = multi_item_queue.dequeue()
        assert item2 == 2
        assert multi_item_queue.size() == 1
        assert multi_item_queue.front == 2

        item3 = multi_item_queue.dequeue()
        assert item3 == 3
        assert multi_item_queue.is_empty()
        assert multi_item_queue.front == 3
        assert multi_item_queue.rear == 3

    def test_dequeue_wraparound(self):
        """Test dequeueing with wraparound."""
        queue = ArrayQueue(capacity=3)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.dequeue()
        item = queue.dequeue()
        assert item == 3
        assert queue.is_empty()
        assert queue.front == 3
        assert queue.rear == 3

    def test_peek_empty(self, empty_queue):
        """Test peeking at an empty queue."""
        with pytest.raises(IndexError, match="Queue is empty"):
            empty_queue.peek()

    def test_peek_single(self, single_item_queue):
        """Test peeking at a queue with one item."""
        item = single_item_queue.peek()
        assert item == 1
        assert not single_item_queue.is_empty()
        assert single_item_queue.size() == 1
        assert single_item_queue.front == 0

    def test_peek_multiple(self, multi_item_queue):
        """Test peeking at a queue with multiple items."""
        item = multi_item_queue.peek()
        assert item == 1
        assert not multi_item_queue.is_empty()
        assert multi_item_queue.size() == 3
        assert multi_item_queue.front == 0

    def test_size(self, empty_queue, single_item_queue, multi_item_queue):
        """Test the size method."""
        assert empty_queue.size() == 0
        assert single_item_queue.size() == 1
        assert multi_item_queue.size() == 3
        multi_item_queue.dequeue()
        assert multi_item_queue.size() == 2

    def test_is_empty(self, empty_queue, single_item_queue):
        """Test the is_empty method."""
        assert empty_queue.is_empty()
        assert not single_item_queue.is_empty()
        single_item_queue.dequeue()
        assert single_item_queue.is_empty()

    def test_add_empty_empty(self, empty_queue):
        """Test adding two empty queues."""
        other_queue = ArrayQueue()
        new_queue = empty_queue + other_queue
        assert isinstance(new_queue, ArrayQueue)
        assert new_queue.is_empty()
        assert new_queue.size() == 0
        assert new_queue.capacity == empty_queue.capacity + other_queue.capacity  # Initial capacity

    def test_add_empty_non_empty(self, empty_queue, multi_item_queue):
        """Test adding an empty queue to a non-empty queue."""
        new_queue = empty_queue + multi_item_queue
        assert isinstance(new_queue, ArrayQueue)
        assert not new_queue.is_empty()
        assert new_queue.size() == 3
        assert [new_queue.items[i] for i in range(new_queue.size())] == [1, 2, 3]
        assert new_queue.front == 0
        assert new_queue.rear == 3
        assert new_queue.capacity == empty_queue.capacity + multi_item_queue.capacity

    def test_add_non_empty_empty(self, multi_item_queue, empty_queue):
        """Test adding a non-empty queue to an empty queue."""
        new_queue = multi_item_queue + empty_queue
        assert isinstance(new_queue, ArrayQueue)
        assert not new_queue.is_empty()
        assert new_queue.size() == 3
        assert [new_queue.items[i] for i in range(new_queue.size())] == [1, 2, 3]
        assert new_queue.front == 0
        assert new_queue.rear == 3
        assert new_queue.capacity == multi_item_queue.capacity + empty_queue.capacity

    def test_add_non_empty_non_empty(self, single_item_queue, multi_item_queue):
        """Test adding two non-empty queues."""
        new_queue = single_item_queue + multi_item_queue
        assert isinstance(new_queue, ArrayQueue)
        assert not new_queue.is_empty()
        assert new_queue.size() == 4
        assert [new_queue.items[i] for i in range(new_queue.size())] == [1, 1, 2, 3]
        assert new_queue.front == 0
        assert new_queue.rear == 4
        assert new_queue.capacity == single_item_queue.capacity + multi_item_queue.capacity

    def test_iadd_empty_empty(self, empty_queue):
        """Test in-place addition of two empty queues."""
        other_queue = ArrayQueue()
        initial_id = id(empty_queue)
        empty_queue += other_queue
        assert id(empty_queue) == initial_id
        assert empty_queue.is_empty()
        assert empty_queue.size() == 0
        assert empty_queue.capacity == 10  # Initial capacity

    def test_iadd_empty_non_empty(self, empty_queue, multi_item_queue):
        """Test in-place addition of an empty queue to a non-empty queue."""
        initial_id = id(empty_queue)
        empty_queue += multi_item_queue
        assert id(empty_queue) == initial_id
        assert not empty_queue.is_empty()
        assert empty_queue.size() == 3
        assert [empty_queue.items[i] for i in range(empty_queue.size())] == [1, 2, 3]
        assert empty_queue.front == 0
        assert empty_queue.rear == 3
        assert empty_queue.capacity == 10  # Initial capacity

    def test_iadd_non_empty_empty(self, single_item_queue, empty_queue):
        """Test in-place addition of a non-empty queue to an empty queue."""
        initial_id = id(single_item_queue)
        single_item_queue += empty_queue
        assert id(single_item_queue) == initial_id
        assert not single_item_queue.is_empty()
        assert single_item_queue.size() == 1
        assert single_item_queue.items[single_item_queue.front] == 1
        assert single_item_queue.front == 0
        assert single_item_queue.rear == 1
        assert single_item_queue.capacity == 10

    def test_iadd_non_empty_non_empty(self, single_item_queue, multi_item_queue):
        """Test in-place addition of two non-empty queues."""
        initial_id = id(single_item_queue)
        single_item_queue += multi_item_queue
        assert id(single_item_queue) == initial_id
        assert not single_item_queue.is_empty()
        assert single_item_queue.size() == 4
        assert [single_item_queue.items[i] for i in range(single_item_queue.size())] == [1, 1, 2, 3]
        assert single_item_queue.front == 0
        assert single_item_queue.rear == 4
        assert single_item_queue.capacity == 10

    def test_iadd_resize(self):
        """Test in-place addition triggers resize if needed."""
        queue1 = ArrayQueue(capacity=2)
        queue1.enqueue(1)
        queue1.enqueue(2)
        queue2 = ArrayQueue()
        queue2.enqueue(3)
        queue2.enqueue(4)
        queue1 += queue2
        assert queue1.size() == 4
        assert queue1.capacity >= 4
        assert [queue1.items[i] for i in range(queue1.size())] == [1, 2, 3, 4]
        assert queue1.front == 0
        assert queue1.rear == 4
        assert queue2.is_empty()
        assert queue2.size() == 0

    def test_add_different_capacities(self):
        """Test adding queues with different initial capacities."""
        queue1 = ArrayQueue(capacity=5)
        queue1.enqueue(1)
        queue2 = ArrayQueue(capacity=10)
        queue2.enqueue(2)
        result_queue = queue1 + queue2
        assert result_queue.size() == 2
        assert result_queue.capacity == 15
        assert [result_queue.items[i] for i in range(result_queue.size())] == [1, 2]
        assert result_queue.front == 0
        assert result_queue.rear == 2

    def test_iadd_different_capacities(self):
        """Test in-place adding queues with different initial capacities."""
        queue1 = ArrayQueue(capacity=5)
        queue1.enqueue(1)
        queue2 = ArrayQueue(capacity=10)
        queue2.enqueue(2)
        queue1 += queue2
        assert queue1.size() == 2
        assert queue1.capacity == 5  # Should resize if needed
        assert [queue1.items[i] for i in range(queue1.size())] == [1, 2]
        assert queue1.front == 0
        assert queue1.rear == 2
        assert queue2.is_empty()
        assert queue2.size() == 0
