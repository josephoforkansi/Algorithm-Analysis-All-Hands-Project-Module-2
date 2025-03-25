from benchmark import benchmark
from sll_queue import SLLQueue
from dll_queue import DLLQueue
from array_queue import ArrayQueue
import unittest
import test_cases

def run_tests():
    """Run all unit tests."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_cases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

def main():
    print("Running performance benchmarks...\n")
    
    operations = ["addFirst", "addLast", "removeFirst", "removeLast", "add (+)", "iadd (+=)"]
    for queue_type in [SLLQueue, DLLQueue, ArrayQueue]:
        print(f"Benchmarking {queue_type.__name__}:\n")
        results = benchmark(queue_type, operations)
        for operation, timings in results.items():
            print(f"Operation: {operation}")
            for size, avg_time in timings:
                print(f"  Size: {size}, Avg Time: {avg_time:.6f} seconds")
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    main()
