# All Hands Project 2

## Research Question

**What are the performance differences between Singly Linked List (SLL) Queue, Doubly Linked List (DLL) Queue, and Array-based Queue implementations when executing basic operations:**

This project evaluates the performance of:

- Singly Linked List (SLL) Queue

- Doubly Linked List (DLL) Queue

- Array-based Queue

Each implementation is tested for efficiency in performing:

- enqueue(value): Adds an element to the back of the queue.

- dequeue(): Removes and returns the front element of the queue.

- peek(): Returns the front element without removing it.

- __add__: Merges two queues into a new queue.

- __iadd__: Performs in-place merging of two queues.

## 🚀 Project Overview

This project implements and benchmarks different queue data structures to analyze their performance across common queue operations.

## Queue Implementations

- Singly Linked List (SLL) Queue - Implemented in sll_queue.py

- Doubly Linked List (DLL) Queue - Implemented in dll_queue.py

- Array-based Queue - Implemented in array_queue.py

## Basic Operations Implemented

Each queue implementation includes methods for:

- addFirst(value): Adds an element to the front of the queue.

- addLast(value): Adds an element to the back of the queue.

- removeFirst(): Removes and returns the front element of the queue.

- removeLast(): Removes and returns the last element of the queue.

- __add__(other): Implements the + operation for merging two queues.

- __iadd__(other): Implements the += operation for in-place merging.

## Supporting Tasks

- Benchmarking & Performance Testing (benchmark.py): Compares execution times for queue operations.

- Test Cases (test_cases.py): Unit tests verifying correctness of implementations.

- README Documentation (README.md): Describes implementation, approach, and results.

- Data Collection: Gathering and analyzing performance metrics.

## Running the Project

1. Benchmark Performance

Run main.py to execute performance benchmarking and unit tests:

- `python main.py`

2. Running Unit Tests Separately

To run only the unit tests:

- `python -m unittest test_cases.py`

## Results & Findings

The benchmarking results will provide insights into the performance trade-offs between SLL, DLL, and Array-based queue implementations. These results will be documented and analyzed as part of the project conclusion.

Contributors

- Benchmarking: [2 team members]

- Test case development: [1-2 team members]

- Documentation: [README author]

- Data collection: Entire team

## Deadline

The final project submission is due this Friday. Ensure all components are completed and tested before the deadline.

Note: This README will be updated with final performance results once data collection is complete.
