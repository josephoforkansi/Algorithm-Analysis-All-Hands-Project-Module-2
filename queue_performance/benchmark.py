import time
from queue_performance.sll_queue import SLLQueue
from queue_performance.dll_queue import DLLQueue
from queue_performance.array_queue import ArrayQueue

def benchmark(queue_type, operations=1000):
    queue = queue_type()
    
    start = time.time()
    for i in range(operations):
        queue.addFirst(i)
    end = time.time()
    print(f"{queue_type.__name__} addFirst: {end - start:.6f} seconds")

    start = time.time()
    for i in range(operations):
        queue.addLast(i)
    end = time.time()
    print(f"{queue_type.__name__} addLast: {end - start:.6f} seconds")

    start = time.time()
    for _ in range(operations):
        queue.removeFirst()
    end = time.time()
    print(f"{queue_type.__name__} removeFirst: {end - start:.6f} seconds")

    start = time.time()
    for _ in range(operations):
        queue.removeLast()
    end = time.time()
    print(f"{queue_type.__name__} removeLast: {end - start:.6f} seconds")

if __name__ == "__main__":
    for q in [SLLQueue, DLLQueue, ArrayQueue]:
        benchmark(q)
