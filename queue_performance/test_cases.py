import unittest
from queue_performance.sll_queue import SLLQueue
from queue_performance.dll_queue import DLLQueue
from queue_performance.array_queue import ArrayQueue

class TestQueueImplementations(unittest.TestCase):
    def test_sll(self):
        q = SLLQueue()
        q.addFirst(1)
        self.assertEqual(q.removeFirst(), 1)

    def test_dll(self):
        q = DLLQueue()
        q.addFirst(2)
        self.assertEqual(q.removeFirst(), 2)

    def test_array(self):
        q = ArrayQueue()
        q.addFirst(3)
        self.assertEqual(q.removeFirst(), 3)

if __name__ == "__main__":
    unittest.main()
