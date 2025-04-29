# All Hands Project 2 (Joseph, Anton, Javier)

🔬 Research Question

What are the performance differences between Singly Linked List (SLL) Queue, Doubly Linked List (DLL) Queue and Array-based Queue implementations when executing basic operations.

🚀 Project Overview

This project benchmarks queue data structures to analyze their efficiency across basic operations. The implementation is structured within the `analyze` project.

➡️➡️➡️ Queue Implementations

* Singly Linked List (SLL) Queue - Implemented in `analyze/sll_queue.py` (Class: `BasicSLLQueue`)
* Doubly Linked List (DLL) Queue - Implemented in `analyze/dll_queue.py` (Class: `BasicDLLQueue`)
* Array-based Queue - Implemented in `analyze/ArrayQueue.py` (Class: `ArrayQueue`)

🔧 Basic Operations Implemented

Each queue implementation supports the following fundamental operations:

* `enqueue(value)`: Adds an element to the back of the queue (FIFO).
* `dequeue()`: Removes and returns the front element of the queue.
* `peek()`: Returns the front element without removing it.
* `size()`: Returns the number of elements in the queue.
* `is_empty()`: Checks if the queue is empty.

The queue implementations support merging operations:

* `add (+)`: Creates a new queue by merging two existing queues.
* `iadd (+=)`: Merges another queue into the current queue in place.

🛠️ Supporting Tasks

* `timer.py`: Measures execution times for queue operations.
* `test_cases.py`: Pytest-based tests verifying correctness of implementations.
* `README.md`: Describes implementation, approach, and results.
* Data Collection: Gathering and analyzing performance metrics.

✅ Running the Project

- To run the program:

```bash
cd analyze && poetry install
```

- To run just the basic performance analysis:

```Bash
poetry run analyze analyze
```

- To run the doubling experiment:

```Bash
poetry run analyze doubling
```

You can also run the commands below for a more detailed approach:
```Bash
poetry run analyze --help
poetry run analyze analyze --help
poetry run analyze doubling --help
```
