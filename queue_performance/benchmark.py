import time
from sll_queue import SLLQueue
from dll_queue import DLLQueue
from array_queue import ArrayQueue


def benchmark(queue_class, operations, initial_size=10, max_size=10000):
    """Benchmark a queue class with doubling sizes."""
    results = {}

    size = initial_size
    while size <= max_size:
        for operation in operations:
            start_time = time.time()

            for _ in range(10):  # Run each operation 10 times per size
                queue = queue_class()

                # Pre-fill the queue to the current size
                for i in range(size):
                    queue.addLast(i)  # Use addLast instead of enqueue

                # Perform the operations
                if operation == "addFirst":
                    queue.addFirst(1)  # Use addFirst
                elif operation == "addLast":
                    queue.addLast(2)  # Use addLast
                elif operation == "removeFirst":
                    queue.removeFirst()
                elif operation == "removeLast":
                    queue.removeLast()
                elif operation == "add (+)":
                    queue1 = queue_class()
                    queue2 = queue_class()
                    for i in range(size):
                        queue1.addLast(i)  # Use addLast
                        queue2.addLast(i + size)  # Use addLast
                    queue1 + queue2  # Concatenate
                elif operation == "iadd (+=)":
                    queue1 = queue_class()
                    queue2 = queue_class()
                    for i in range(size):
                        queue1.addLast(i)  # Use addLast
                        queue2.addLast(i + size)  # Use addLast
                    queue1 += queue2  # In-place concatenation

            end_time = time.time()
            avg_time = (end_time - start_time) / 10  # Average over 10 repetitions

            # Store the result with the current size
            if operation not in results:
                results[operation] = []
            results[operation].append((size, avg_time))

        size *= 2  # Double the queue size for the next iteration

    return results
