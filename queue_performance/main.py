from queue_performance.benchmark import benchmark
from queue_performance.sll_queue import SLLQueue
from queue_performance.dll_queue import DLLQueue
from queue_performance.array_queue import ArrayQueue
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
    
    for queue_type in [SLLQueue, DLLQueue, ArrayQueue]:
        print(f"Benchmarking {queue_type.__name__}:\n")
        benchmark(queue_type)
        print("\n" + "-"*50 + "\n")

    print("Running test cases...\n")
    run_tests()
    print("All tasks completed.")

if __name__ == "__main__":
    main()
