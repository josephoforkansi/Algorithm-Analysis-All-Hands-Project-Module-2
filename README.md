# All Hands Project 2

## Research Question

**What are the performance differences between Singly Linked List (SLL) Queue, Doubly Linked List (DLL) Queue, and Array-based Queue implementations when executing basic operations:**

This project evaluates the performance of:

- Singly Linked List (SLL) Queue

- Doubly Linked List (DLL) Queue

- Array-based Queue

Each implementation is tested for efficiency in performing:

- enqueue(value): Adds an element to the back of the queue

- dequeue(): Removes and returns the front element of the queue 

- peek(): Returns the front element without removing it

- concat(+): Merges two queues into a new queue

- iconcat(+=): Performs in-place merging of two queues

## 🚀 Project Overview

This project benchmarks queue data structures to analyze their efficiency across basic operations. The implementation is structured within the analyze project.

## Queue Implementations

- Singly Linked List (SLL) Queue - Implemented in sll_queue.py

- Doubly Linked List (DLL) Queue - Implemented in dll_queue.py

- Array-based Queue - Implemented in array_queue.py

## Basic Operations Implemented

Each queue implementation includes methods for:

- enqueue(value): Adds an element to the back of the queue

- dequeue(): Removes and returns the front element of the queue

- peek(): Returns the front element without removing it

- concat(+): Implements the + operation for merging two queues

- iconcat(+=): Implements the += operation for in-place merging

## Supporting Tasks

- Main Implementation (`main.py`): Core functionality and CLI interface
- Queue Approach (`queue_approach.py`): Queue implementation strategy
- Timer (`timer.py`): Performance measurement utilities
- Results: Performance data and analysis stored in `results/` directory
- Test Cases: Unit tests verifying correctness of implementations
- Documentation: Project documentation and analysis

## Running the Project

To run the program:
```bash
cd analyze && poetry install
```

To run just the analyze:
```bash
poetry run analyze analyze
```

To run doubling experiment:
```bash
poetry run analyze doubling
```

You can also run the commands below for a more detailed approach:
```bash
poetry run analyze --help
poetry run analyze analyze --help
poetry run analyze doubling --help
```

## Results & Findings

The benchmarking results will provide insights into the performance trade-offs between SLL, DLL, and Array-based queue implementations. These results will be documented and analyzed as part of the project conclusion.

## Contributors

- Benchmarking: [2 team members]

- Test case development: [1-2 team members]

- Documentation: [README author]

- Data collection: Entire team

## Deadline

The final project submission is due this Friday. Ensure all components are completed and tested before the deadline.

Note: This README will be updated with final performance results once data collection is complete.
