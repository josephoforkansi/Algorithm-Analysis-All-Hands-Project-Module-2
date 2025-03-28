# 😊 All Hands Project 2

## 🔬 Research Question

**What are the performance differences between Singly Linked List (SLL) Queue, Doubly Linked List (DLL) Queue and Array-based Queue implementations when executing basic operations.**

## 🚀 Project Overview

This project benchmarks queue data structures to analyze their efficiency across basic operations. The implementation is structured within the analyze project.

## ➡️➡️➡️ Queue Implementations

- Singly Linked List (SLL) Queue - Implemented in sll_queue.py

- Doubly Linked List (DLL) Queue - Implemented in dll_queue.py

- Array-based Queue - Implemented in array_queue.py

## 🔧 Basic Operations Implemented

Each queue implementation supports the following fundamental operations:

- enqueue(value): Adds an element to the back of the queue (FIFO).

- dequeue(): Removes and returns the front element of the queue.

- peek(): Returns the front element without removing it.

- size(): Returns the number of elements in the queue.

- is_empty(): Checks if the queue is empty.

The queue implementations support merging operations:

- add (+): Creates a new queue by merging two existing queues.

- iadd (+=): Merges another queue into the current queue in place.

## 🛠️ Supporting Tasks

- Timing Utilities (timer.py): Measures execution times for queue operations.

- Test Cases (test_cases.py): Pytest-based tests verifying correctness of implementations.

- README Documentation (README.md): Describes implementation, approach, and results.

- Data Collection: Gathering and analyzing performance metrics.

## ✅ Running the Project

To run the program

- `cd analyze && poetry install`

To run just the analyze

- `poetry run analyze analyze`

To run doubling experiment

- `poetry run analyze doubling`

You can also run the commands below for a more detailed approach:

- `poetry run analyze --help`
- `poetry run analyze analyze --help`
- `poetry run analyze doubling --help`

## 📄 Results & Findings

The benchmarking results will provide insights into the performance trade-offs between SLL, DLL, and Array-based queue implementations. These results will be documented and analyzed as part of the project conclusion.

Contributors

- Benchmarking: [Anoop and Finley]

- Test case development: [Anton and Javier]

- Documentation: [Joseph]

- Data collection: [Entire team]

## 🎯 Deadline

The final project submission is due this Friday. Ensure all components are completed and tested before the deadline.

Note: This README will be updated with final performance results once data collection is complete.
