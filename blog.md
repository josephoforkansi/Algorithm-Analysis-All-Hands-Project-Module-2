# All Hands Project 2

## Introduction

Data structures play a critical role in efficient software development, influencing performance, scalability, and system responsiveness. Among them, queues are fundamental, powering applications such as task scheduling, messaging systems, and real-time data processing. In this project, our team explored three key queue implementations—Singly Linked List (SLL), Doubly Linked List (DLL), and Array-based Queue analyzing their performance through benchmarking experiments using SystemSense.

As algorithm engineers tackling this project we considered multiple aspects, including:

- Algorithmic Complexity: Understanding the time and space complexity of queue operations to determine trade-offs between different implementations.

- Memory Management: Evaluating how memory allocation and deallocation affect performance, particularly in linked list-based vs. array-based implementations.

- Concurrency Considerations: Investigating how these data structures behave in multi-threaded environments where multiple processes access and modify queues simultaneously.

- Use Case Optimization: Identifying practical applications where each queue implementation excels, such as high-throughput systems, real-time event processing, and low-latency applications.

- Benchmarking Methodology: Designing experiments to measure execution times, analyze scaling behavior, and compare performance under different workloads.

Through this project, we aim to provide insights into the efficiency of these queue implementations and guide the selection of an optimal data structure based on application requirements. By profiling and analyzing queue operations, we not only enhance our understanding of core data structures but also develop practical skills in performance analysis, a crucial skill in software engineering and systems design.

### Motivation

Efficient data structures are essential in software development, especially when dealing with queues in real-world applications such as scheduling systems, task management, and networking. Different queue implementations like Singly Linked List (SLL), Doubly Linked List (DLL), and Array-based Queue offer trade-offs in terms of performance. Our project aims to benchmark these tradeoffs and analyze the data by comparing the execution times of the queue operations.

### Function Explanation

Each queue implementation supports the following operations:

* **addFirst(value):** Inserts an element to the front of the queue.
* **addLast(value):** Appends an element to the back of the queue.
* **removeFirst():** Removes and returns the front element.
* **removeLast():** Removes and returns the last element.
* **add(other):** Merges two queues using `+` operator.
* **iadd(other):** Performs an in-place merging using the += operator.

Each implementation is tested to measure how efficiently these operations execute under different scenarios.

## Implementation

### Operations

Our Project explores three queue implementations: Singly Linked List (SLL) Queue, Doubly Linked List (DLL) Queue, and Array-based Queue. Each implementation is different in its structure and performance but supports fundamental queue operations.

### Singly Linked List (SLL) Queue

The SLL Queue implementation uses a singly linked list structure where each node contains data and a reference to the next node. Here's the core implementation:

```python
class ListNode:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedListPrime:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
```

#### SLL Considerations
- O(1) operations for addFirst and removeFirst: The implementation maintains a head pointer, allowing immediate access to the front of the list.
- O(n) for removeLast as it needs to traverse the list: Since nodes only have a next pointer, finding the last element requires traversing the entire list.
- Supports efficient concatenation with O(1) using tail pointer: The tail pointer allows quick access to the end of the list for joining operations.
- Best for FIFO operations where elements are added and removed from the front: The structure naturally supports first-in-first-out operations with minimal overhead.

### Doubly Linked List (DLL) Queue

The DLL Queue uses a doubly linked list where each node has references to both next and previous nodes:

```python
class DLLNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
```

#### DLL Considerations
- O(1) operations for both addFirst/removeFirst and addLast/removeLast: The bidirectional links allow immediate access to both ends of the list.
- Efficient bidirectional traversal: Each node maintains references to both its next and previous nodes, enabling traversal in either direction.
- O(1) concatenation operations: The bidirectional structure allows efficient joining of lists at either end.
- Ideal for applications requiring frequent operations at both ends: The structure provides balanced performance for operations at both the front and back of the list.

### Array-based Queue

The Array Queue uses a dynamic array implementation with automatic resizing:

```python
class ListQueueDisplay:
    def __init__(self):
        self._items = []
        self._size = 0
```

#### Array-based Queue Considerations
- O(1) random access: The array structure provides direct access to any element by index.
- O(n) worst-case for addFirst/removeFirst due to shifting: Adding or removing elements at the front requires shifting all other elements.
- O(1) amortized for addLast/removeLast: Appending or removing from the end doesn't require shifting other elements.
- Best for applications with predictable size and infrequent resizing: The array structure works well when the queue size is relatively stable.

Each implementation has its strengths:
- SLL: Efficient for FIFO operations, with minimal overhead for front-end operations
- DLL: Flexible bidirectional operations, with balanced performance for operations at both ends
- Array: Fast random access, with efficient operations at the end of the queue

The choice between implementations depends on the specific use case and performance requirements of the application.

### Benchmarking

## Running and Using the Tool

### Setting Up

To run the benchmarking tool, ensure you have Poetry installed onto your device. Navigate to the project directory and install dependencies if you have not already:

`poetry install`

### Running the Experiments

The tool provides two main benchmarking experiments:

#### Doubling Experiment

To run the doubling experiment, execute:

`poetry run analyze doubling`

This experiment measures how performance will scale with the increasing input sizes.

#### Implementation Performance Analysis

To analyze the performance of individual queue operations, run:

`poetry run analyze analyze`

this command will provide execution times for operations like `addList`, `dequeue`, and `enqueue` to compare their efficiency.

## Output Analysis

### Finley Banas

#### Run of systemsense

#### Run of Doubling Experiment

```python
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                         DLL Queue Doubling Experiment Results                                                                                      │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬───────────┬──────────┬──────────┬─────────────┬────────────╮                                              │
│ │ Size (n) │ addfirst │  addlast │   concat │  dequeue │   enqueue │  iconcat │     peek │ removefirst │ removelast │                                              │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼───────────┼──────────┼──────────┼─────────────┼────────────┤                                              │
│ │      100 │ 0.005710 │ 0.003530 │ 0.011750 │ 0.004900 │  0.391390 │ 0.009490 │ 0.010090 │    0.003230 │   0.005170 │                                              │
│ │      200 │ 0.004220 │ 0.002580 │ 0.017490 │ 0.004650 │  0.922270 │ 0.012900 │ 0.009670 │    0.003760 │   0.002580 │                                              │
│ │      400 │ 0.004140 │ 0.003440 │ 0.014130 │ 0.007050 │  1.574360 │ 0.011930 │ 0.009460 │    0.004390 │   0.004200 │                                              │
│ │      800 │ 0.004520 │ 0.003870 │ 0.016340 │ 0.007780 │  5.318540 │ 0.013220 │ 0.011310 │    0.004850 │   0.004410 │                                              │
│ │    1,600 │ 0.005460 │ 0.004030 │ 0.017030 │ 0.008200 │  9.162910 │ 0.014000 │ 0.011390 │    0.005410 │   0.005640 │                                              │
│ │    3,200 │ 0.008430 │ 0.006050 │ 0.019890 │ 0.008410 │ 14.354910 │ 0.018860 │ 0.014960 │    0.006530 │   0.006630 │                                              │
│ │    6,400 │ 0.006580 │ 0.005100 │ 0.022510 │ 0.009120 │ 31.089690 │ 0.020840 │ 0.017100 │    0.006320 │   0.006250 │                                              │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴───────────┴──────────┴──────────┴─────────────┴────────────╯                                              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Plot saved to: results\dll_doubling_20250326_163011.png
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                         SLL Queue Doubling Experiment Results                                                                                      │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬───────────┬──────────┬──────────┬─────────────┬────────────╮                                              │
│ │ Size (n) │ addfirst │  addlast │   concat │  dequeue │   enqueue │  iconcat │     peek │ removefirst │ removelast │                                              │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼───────────┼──────────┼──────────┼─────────────┼────────────┤                                              │
│ │      100 │ 0.006540 │ 0.004560 │ 0.018020 │ 0.013310 │  0.789810 │ 0.013260 │ 0.007590 │    0.004990 │   0.006780 │                                              │
│ │      200 │ 0.005070 │ 0.004380 │ 0.007750 │ 0.008210 │  1.055980 │ 0.005600 │ 0.002540 │    0.006730 │   0.008570 │                                              │
│ │      400 │ 0.004580 │ 0.004510 │ 0.011240 │ 0.006320 │  1.547180 │ 0.006710 │ 0.003190 │    0.005610 │   0.005310 │                                              │
│ │      800 │ 0.012190 │ 0.006700 │ 0.016760 │ 0.009430 │  3.362860 │ 0.011120 │ 0.006250 │    0.006880 │   0.006240 │                                              │
│ │    1,600 │ 0.010710 │ 0.006970 │ 0.025030 │ 0.009050 │  7.287900 │ 0.017110 │ 0.004780 │    0.008590 │   0.008500 │                                              │
│ │    3,200 │ 0.009610 │ 0.010320 │ 0.014100 │ 0.009890 │ 14.180820 │ 0.012600 │ 0.005780 │    0.010540 │   0.009890 │                                              │
│ │    6,400 │ 0.013350 │ 0.011260 │ 0.018110 │ 0.011390 │ 26.073940 │ 0.014110 │ 0.005920 │    0.012290 │   0.010010 │                                              │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴───────────┴──────────┴──────────┴─────────────┴────────────╯                                              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Plot saved to: results\sll_doubling_20250326_163018.png
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                        ARRAY Queue Doubling Experiment Results                                                                                     │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬───────────┬──────────┬──────────┬─────────────┬────────────╮                                              │
│ │ Size (n) │ addfirst │  addlast │   concat │  dequeue │   enqueue │  iconcat │     peek │ removefirst │ removelast │                                              │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼───────────┼──────────┼──────────┼─────────────┼────────────┤                                              │
│ │      100 │ 0.002080 │ 0.003600 │ 0.006120 │ 0.008630 │  0.192060 │ 0.003850 │ 0.005280 │    0.015000 │   0.016320 │                                              │
│ │      200 │ 0.002790 │ 0.002650 │ 0.012200 │ 0.018710 │  0.838030 │ 0.005970 │ 0.011110 │    0.007530 │   0.009110 │                                              │
│ │      400 │ 0.004030 │ 0.002750 │ 0.010640 │ 0.007750 │  0.676010 │ 0.003470 │ 0.005370 │    0.009110 │   0.008520 │                                              │
│ │      800 │ 0.002900 │ 0.002490 │ 0.013590 │ 0.009870 │  1.443740 │ 0.005120 │ 0.006590 │    0.010900 │   0.008220 │                                              │
│ │    1,600 │ 0.003030 │ 0.002700 │ 0.021540 │ 0.013780 │  2.811830 │ 0.005970 │ 0.009970 │    0.010310 │   0.011480 │                                              │
│ │    3,200 │ 0.005390 │ 0.003760 │ 0.048610 │ 0.012610 │  5.757060 │ 0.009470 │ 0.010830 │    0.013380 │   0.018810 │                                              │
│ │    6,400 │ 0.004440 │ 0.004150 │ 0.079600 │ 0.012760 │ 12.759230 │ 0.020740 │ 0.011160 │    0.013500 │   0.016680 │                                              │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴───────────┴──────────┴──────────┴─────────────┴────────────╯                                              │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Plot saved to: results\array_doubling_20250326_163022.png
Combined plot for addfirst saved to: results\combined_addfirst_20250326_163024.png
Combined plot for addlast saved to: results\combined_addlast_20250326_163025.png
Combined plot for concat saved to: results\combined_concat_20250326_163027.png
Combined plot for dequeue saved to: results\combined_dequeue_20250326_163028.png
Combined plot for enqueue saved to: results\combined_enqueue_20250326_163029.png
Combined plot for iconcat saved to: results\combined_iconcat_20250326_163030.png
Combined plot for peek saved to: results\combined_peek_20250326_163032.png
Combined plot for removefirst saved to: results\combined_removefirst_20250326_163033.png
Combined plot for removelast saved to: results\combined_removelast_20250326_163035.png
```

#### Run of Performance Analysis

```python
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│        DLL Queue Implementation Performance Analysis                                                                                                               │
│ ╭──────────────┬───────────┬──────────┬───────────────────╮                                                                                                        │
│ │ Operation    │ Time (ms) │ Elements │ Time/Element (ms) │                                                                                                        │
│ ├──────────────┼───────────┼──────────┼───────────────────┤                                                                                                        │
│ │ addlast      │  1.269500 │    1,000 │          0.001270 │                                                                                                        │
│ │ dequeue      │  3.385700 │    1,000 │          0.003386 │                                                                                                        │
│ │ enqueue      │  7.086600 │    2,000 │          0.003543 │                                                                                                        │
│ │ is_empty     │  0.722900 │      333 │          0.002171 │                                                                                                        │
│ │ length       │  0.764400 │      833 │          0.000918 │                                                                                                        │
│ │ length/empty │  0.839600 │      250 │          0.003358 │                                                                                                        │
│ │ peek         │  4.028300 │      999 │          0.004032 │                                                                                                        │
│ │ removefirst  │  0.425700 │      500 │          0.000851 │                                                                                                        │
│ ╰──────────────┴───────────┴──────────┴───────────────────╯                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│        SLL Queue Implementation Performance Analysis                                                                                                               │
│ ╭──────────────┬───────────┬──────────┬───────────────────╮                                                                                                        │
│ │ Operation    │ Time (ms) │ Elements │ Time/Element (ms) │                                                                                                        │
│ ├──────────────┼───────────┼──────────┼───────────────────┤                                                                                                        │
│ │ addfirst     │  0.006500 │        1 │          0.006500 │                                                                                                        │
│ │ addlast      │  1.024600 │    1,000 │          0.001025 │                                                                                                        │
│ │ dequeue      │  2.752300 │    1,000 │          0.002752 │                                                                                                        │
│ │ enqueue      │  6.738700 │    2,000 │          0.003369 │                                                                                                        │
│ │ length       │  0.623400 │      500 │          0.001247 │                                                                                                        │
│ │ length/empty │  0.843000 │      250 │          0.003372 │                                                                                                        │
│ │ peek         │  0.675100 │      666 │          0.001014 │                                                                                                        │
│ │ removefirst  │  0.307900 │      500 │          0.000616 │                                                                                                        │
│ ╰──────────────┴───────────┴──────────┴───────────────────╯                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│       Array Queue Implementation Performance Analysis                                                                                                              │
│ ╭──────────────┬───────────┬──────────┬───────────────────╮                                                                                                        │
│ │ Operation    │ Time (ms) │ Elements │ Time/Element (ms) │                                                                                                        │
│ ├──────────────┼───────────┼──────────┼───────────────────┤                                                                                                        │
│ │ dequeue      │  6.014800 │    1,000 │          0.006015 │                                                                                                        │
│ │ enqueue      │  3.074300 │    2,000 │          0.001537 │                                                                                                        │
│ │ is_empty     │  1.960900 │      833 │          0.002354 │                                                                                                        │
│ │ length       │  0.697300 │    1,083 │          0.000644 │                                                                                                        │
│ │ length/empty │  0.835300 │      250 │          0.003341 │                                                                                                        │
│ │ peek         │  5.350100 │    1,166 │          0.004588 │                                                                                                        │
│ ╰──────────────┴───────────┴──────────┴───────────────────╯                                                                                                        │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```



### Anton Hedlund

#### Run of systemsense

```cmd
poetry run systemsense completeinfo
Displaying System Information

╭─────────────────────────────────────────────────────── System Information ───────────────────────────────────────────────────────╮
│ ╭──────────────────┬───────────────────────────────────────────────────────────────────────────────────────────────────────────╮ │
│ │ System Parameter │ Parameter Value                                                                                           │ │
│ ├──────────────────┼───────────────────────────────────────────────────────────────────────────────────────────────────────────┤ │
│ │ battery          │ 79.00% battery life remaining, 6:15:00 seconds remaining                                                  │ │
│ │ cpu              │ arm                                                                                                       │ │
│ │ cpucores         │ 11 cores                                                                                                  │ │
│ │ cpufrequencies   │ Min: Unknown Mhz, Max: Unknown Mhz                                                                        │ │
│ │ datetime         │ 2025-03-26 22:32:34.509801                                                                                │ │
│ │ disk             │ Using 10.39 GB of 460.43 GB                                                                               │ │
│ │ hostname         │ MacBook-Pro-Anton.local                                                                                   │ │
│ │ memory           │ Using 6.58 GB of 18.00 GB                                                                                 │ │
│ │ platform         │ macOS-15.3.2-arm64-arm-64bit                                                                              │ │
│ │ pythonversion    │ 3.12.8                                                                                                    │ │
│ │ runningprocesses │ 594 running processes                                                                                     │ │
│ │ swap             │ Using 0.49 GB of 2.00 GB                                                                                  │ │
│ │ system           │ Darwin                                                                                                    │ │
│ │ systemload       │ Average Load: 2.82, CPU Utilization: 20.50%                                                               │ │
│ │ virtualenv       │ /Users/antonhedlund/Compsci/algorhytms_202/computer-science-202-algorithm-engineering-project-1-ahedlund… │ │
│ ╰──────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────╯ │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

Displaying Benchmark Results

╭────────────────────────────────────────────────────────────────────────── Benchmark Results ──────────────────────────────────────────────────────────────────────────╮
│ ╭────────────────┬─────────────────────────────────────────────────────────────────╮                                                                                  │
│ │ Benchmark Name │ Benchmark Results (sec)                                         │                                                                                  │
│ ├────────────────┼─────────────────────────────────────────────────────────────────┤                                                                                  │
│ │ addition       │ [0.37942662500427105, 0.38371645798906684, 0.39661604099092074] │                                                                                  │
│ │ concatenation  │ [1.831420500006061, 1.8045542500040028, 1.8012452079856303]     │                                                                                  │
│ │ exponentiation │ [2.1522245419910178, 2.1751532499911264, 2.2064731669961475]    │                                                                                  │
│ │ multiplication │ [0.4023984170053154, 0.45870250000734814, 0.5052193750161678]   │                                                                                  │
│ │ rangelist      │ [0.10194725001929328, 0.09878037497401237, 0.10006220897776075] │                                                                                  │
│ ╰────────────────┴─────────────────────────────────────────────────────────────────╯                                                                                  │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Run of Doubling Experiment

```cmd
poetry run analyze doubling --initial-size 1000 --max-size 1000000
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                         DLL Queue Doubling Experiment Results                                                            │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬────────────┬──────────┬──────────┬─────────────┬────────────╮                   │
│ │ Size (n) │ addfirst │  addlast │   concat │  dequeue │    enqueue │  iconcat │     peek │ removefirst │ removelast │                   │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼────────────┼──────────┼──────────┼─────────────┼────────────┤                   │
│ │    1,000 │ 0.000933 │ 0.000779 │ 0.003279 │ 0.001304 │   1.187083 │ 0.002650 │ 0.002125 │    0.000829 │   0.000858 │                   │
│ │    2,000 │ 0.000825 │ 0.000775 │ 0.003075 │ 0.001142 │   2.307400 │ 0.002612 │ 0.002213 │    0.000746 │   0.001033 │                   │
│ │    4,000 │ 0.000867 │ 0.000854 │ 0.003321 │ 0.001275 │   4.624387 │ 0.002771 │ 0.002392 │    0.000792 │   0.000717 │                   │
│ │    8,000 │ 0.000962 │ 0.000812 │ 0.003508 │ 0.001333 │  11.926154 │ 0.003129 │ 0.002292 │    0.000904 │   0.000854 │                   │
│ │   16,000 │ 0.000937 │ 0.000829 │ 0.003629 │ 0.001471 │  21.639504 │ 0.002938 │ 0.002558 │    0.000992 │   0.000862 │                   │
│ │   32,000 │ 0.001067 │ 0.000850 │ 0.004012 │ 0.001646 │  42.478613 │ 0.003254 │ 0.002608 │    0.001079 │   0.001046 │                   │
│ │   64,000 │ 0.001571 │ 0.000917 │ 0.004800 │ 0.001962 │  86.116583 │ 0.004604 │ 0.003258 │    0.001391 │   0.001304 │                   │
│ │  128,000 │ 0.001579 │ 0.000854 │ 0.005696 │ 0.002279 │ 180.033017 │ 0.004483 │ 0.003975 │    0.001733 │   0.001538 │                   │
│ │  256,000 │ 0.001767 │ 0.001013 │ 0.007225 │ 0.003154 │ 389.395746 │ 0.005829 │ 0.005058 │    0.002362 │   0.002246 │                   │
│ │  512,000 │ 0.002196 │ 0.001092 │ 0.007658 │ 0.003504 │ 852.456588 │ 0.006071 │ 0.005192 │    0.002467 │   0.002058 │                   │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴────────────┴──────────┴──────────┴─────────────┴────────────╯                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Plot saved to: results/dll_doubling_20250326_222545.png
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                         SLL Queue Doubling Experiment Results                                                            │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬────────────┬──────────┬──────────┬─────────────┬────────────╮                   │
│ │ Size (n) │ addfirst │  addlast │   concat │  dequeue │    enqueue │  iconcat │     peek │ removefirst │ removelast │                   │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼────────────┼──────────┼──────────┼─────────────┼────────────┤                   │
│ │    1,000 │ 0.001379 │ 0.001338 │ 0.002692 │ 0.001696 │   1.105913 │ 0.001854 │ 0.000813 │    0.001312 │   0.001246 │                   │
│ │    2,000 │ 0.001383 │ 0.001379 │ 0.002367 │ 0.001317 │   2.142629 │ 0.001692 │ 0.000754 │    0.001317 │   0.001287 │                   │
│ │    4,000 │ 0.001383 │ 0.001404 │ 0.002708 │ 0.001571 │   4.395746 │ 0.001913 │ 0.000796 │    0.001417 │   0.001371 │                   │
│ │    8,000 │ 0.001554 │ 0.001454 │ 0.002854 │ 0.001917 │   8.810400 │ 0.002692 │ 0.001354 │    0.001450 │   0.001813 │                   │
│ │   16,000 │ 0.001713 │ 0.001529 │ 0.003325 │ 0.001950 │  21.788742 │ 0.002888 │ 0.001083 │    0.001600 │   0.001729 │                   │
│ │   32,000 │ 0.001871 │ 0.001817 │ 0.004583 │ 0.002558 │  38.786442 │ 0.003367 │ 0.001054 │    0.002154 │   0.002058 │                   │
│ │   64,000 │ 0.002275 │ 0.001733 │ 0.005712 │ 0.003479 │  79.691100 │ 0.004421 │ 0.001900 │    0.002829 │   0.002983 │                   │
│ │  128,000 │ 0.002171 │ 0.002517 │ 0.005838 │ 0.003308 │ 163.600163 │ 0.005296 │ 0.002696 │    0.003925 │   0.003741 │                   │
│ │  256,000 │ 0.004229 │ 0.003879 │ 0.007388 │ 0.005596 │ 328.856175 │ 0.008075 │ 0.004179 │    0.004583 │   0.005112 │                   │
│ │  512,000 │ 0.005909 │ 0.005517 │ 0.010196 │ 0.006908 │ 657.338554 │ 0.008758 │ 0.005296 │    0.007529 │   0.006167 │                   │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴────────────┴──────────┴──────────┴─────────────┴────────────╯                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Plot saved to: results/sll_doubling_20250326_222804.png
╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                                        ARRAY Queue Doubling Experiment Results                                                           │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬────────────┬──────────┬──────────┬─────────────┬────────────╮                   │
│ │ Size (n) │ addfirst │  addlast │   concat │  dequeue │    enqueue │  iconcat │     peek │ removefirst │ removelast │                   │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼────────────┼──────────┼──────────┼─────────────┼────────────┤                   │
│ │    1,000 │ 0.000600 │ 0.000629 │ 0.004746 │ 0.002858 │   0.494617 │ 0.001500 │ 0.001650 │    0.002171 │   0.002054 │                   │
│ │    2,000 │ 0.000633 │ 0.000675 │ 0.008996 │ 0.002446 │   0.945646 │ 0.001413 │ 0.001775 │    0.002300 │   0.002216 │                   │
│ │    4,000 │ 0.000675 │ 0.000683 │ 0.018225 │ 0.002262 │   1.855137 │ 0.001954 │ 0.001704 │    0.002346 │   0.002200 │                   │
│ │    8,000 │ 0.000788 │ 0.000691 │ 0.050946 │ 0.002296 │   3.635554 │ 0.003804 │ 0.001712 │    0.002704 │   0.002471 │                   │
│ │   16,000 │ 0.000896 │ 0.000804 │ 0.072767 │ 0.003033 │   7.373833 │ 0.007450 │ 0.002134 │    0.002683 │   0.002567 │                   │
│ │   32,000 │ 0.000837 │ 0.000883 │ 0.147313 │ 0.002829 │  14.812092 │ 0.015137 │ 0.002171 │    0.002892 │   0.002600 │                   │
│ │   64,000 │ 0.000783 │ 0.000754 │ 0.345496 │ 0.002667 │  28.765463 │ 0.034875 │ 0.003279 │    0.002896 │   0.003229 │                   │
│ │  128,000 │ 0.000829 │ 0.000742 │ 0.670671 │ 0.004758 │  58.716100 │ 0.082629 │ 0.004554 │    0.002908 │   0.004354 │                   │
│ │  256,000 │ 0.002579 │ 0.002379 │ 1.480738 │ 0.006492 │ 118.324867 │ 0.195350 │ 0.003046 │    0.006863 │   0.006950 │                   │
│ │  512,000 │ 0.003900 │ 0.003163 │ 4.086571 │ 0.009087 │ 238.503688 │ 0.702646 │ 0.004538 │    0.007342 │   0.007658 │                   │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴────────────┴──────────┴──────────┴─────────────┴────────────╯                   │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Run of Performance Analysis



### Anupraj Guragain

#### Run of systemsense

```bash

✨ Displaying System Information

╭─────────────────────────────────────────────────────────────────────────── System Information Panel ───────────────────────────────────────────────────────────────────────────╮
│ ╭──────────────────┬───────────────────────────────────────────────────────────────────────╮                                                                                   │
│ │ System Parameter │ Parameter Value                                                       │                                                                                   │
│ ├──────────────────┼───────────────────────────────────────────────────────────────────────┤                                                                                   │
│ │ battery          │ 77.25% battery life remaining, unknown seconds remaining              │                                                                                   │
│ │ cpu              │ x86_64                                                                │                                                                                   │
│ │ cpucores         │ Physical cores: 4, Logical cores: 8                                   │                                                                                   │
│ │ cpufrequencies   │ Min: 400.0 Mhz, Max: 4400.0 Mhz                                       │                                                                                   │
│ │ datetime         │ 27/03/2025 17:41:34                                                   │                                                                                   │
│ │ disk             │ Using 43.44 GB of 97.87 GB                                            │                                                                                   │
│ │ hostname         │ cislaptop                                                             │                                                                                   │
│ │ memory           │ Using 8.05 GB of 15.35 GB                                             │                                                                                   │
│ │ platform         │ Linux 6.11.0-21-generic                                               │                                                                                   │
│ │ pythonversion    │ 3.12.3                                                                │                                                                                   │
│ │ runningprocesses │ 362                                                                   │                                                                                   │
│ │ swap             │ Total: 4095 MB, Used: 0 MB, Free: 4095 MB                             │                                                                                   │
│ │ system           │ Linux                                                                 │                                                                                   │
│ │ systemload       │ Average Load: 3.07, CPU Utilization: 3.90%                            │                                                                                   │
│ │ virtualenv       │ /home/student/.cache/pypoetry/virtualenvs/systemsense-DC4abhLn-py3.12 │                                                                                   │
│ ╰──────────────────┴───────────────────────────────────────────────────────────────────────╯                                                                                   │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

🏁 Displaying Benchmark Results

╭───────────────────────────────────────────────────────────────────────── Benchmark Information Panel ──────────────────────────────────────────────────────────────────────────╮
│ ╭────────────────┬─────────────────────────────────────────────────────────────────╮                                                                                           │
│ │ Benchmark Name │ Benchmark Results (sec)                                         │                                                                                           │
│ ├────────────────┼─────────────────────────────────────────────────────────────────┤                                                                                           │
│ │ addition       │ [0.39699050600029295, 0.39876872999593616, 0.40132377600093605] │                                                                                           │
│ │ concatenation  │ [1.9879290609969757, 1.9158207119980943, 1.9231829279960948]    │                                                                                           │
│ │ exponentiation │ [1.9385030220000772, 1.9133422640006756, 2.0385779130010633]    │                                                                                           │
│ │ multiplication │ [0.3794930040021427, 0.3551806879986543, 0.35516838500188896]   │                                                                                           │
│ │ rangelist      │ [0.10307988400018075, 0.0976890980018652, 0.0977334429990151]   │                                                                                           │
│ ╰────────────────┴─────────────────────────────────────────────────────────────────╯                                                                                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

#### Run of Doubling Experiment

```bash

DLL Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                DLL Queue Doubling Experiment Results                                                                        │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                                         │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                                         │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                                         │
│ │      100 │ 0.030002 │ 0.008219 │ 0.002683 │ 0.001251 │ 0.000877 │                                                         │
│ │      200 │ 0.090407 │ 0.014986 │ 0.004260 │ 0.000555 │ 0.000276 │                                                         │
│ │      400 │ 0.152446 │ 0.036750 │ 0.008676 │ 0.000508 │ 0.000311 │                                                         │
│ │      800 │ 0.313388 │ 0.072579 │ 0.019583 │ 0.000548 │ 0.000318 │                                                         │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

SLL Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                 SLL Queue Doubling Experiment Results                                                                       │
│ ╭──────────┬───────────┬──────────┬──────────┬───────────┬──────────╮                                                       │
│ │ Size (n) │   enqueue │  dequeue │     peek │    concat │  iconcat │                                                       │
│ ├──────────┼───────────┼──────────┼──────────┼───────────┼──────────┤                                                       │
│ │      100 │  0.494748 │ 0.010471 │ 0.005463 │  0.698542 │ 0.009062 │                                                       │
│ │      200 │  2.828292 │ 0.022604 │ 0.008451 │  1.486568 │ 0.008854 │                                                       │
│ │      400 │  6.827565 │ 0.029496 │ 0.009866 │  5.607181 │ 0.017691 │                                                       │
│ │      800 │ 25.202299 │ 0.056766 │ 0.016603 │ 20.527040 │ 0.031615 │                                                       │
│ ╰──────────┴───────────┴──────────┴──────────┴───────────┴──────────╯                                                       │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

ARRAY Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│               ARRAY Queue Doubling Experiment Results                                                                       │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                                         │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                                         │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                                         │
│ │      100 │ 0.005900 │ 0.005746 │ 0.003158 │ 0.001537 │ 0.000531 │                                                         │
│ │      200 │ 0.009531 │ 0.011918 │ 0.006305 │ 0.000965 │ 0.000500 │                                                         │
│ │      400 │ 0.018393 │ 0.027901 │ 0.012270 │ 0.001366 │ 0.000729 │                                                         │
│ │      800 │ 0.038183 │ 0.071488 │ 0.023332 │ 0.002206 │ 0.001292 │                                                         │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

```

#### Run of Performance Analysis

```bash

DLL Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│              DLL Queue Performance Analysis                                                                                 │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                    │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                    │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                    │
│ │ enqueue   │  0.330256 │    1,000 │          0.000330 │                                                                    │
│ │ dequeue   │  0.079288 │      500 │          0.000159 │                                                                    │
│ │ peek      │  0.021357 │      333 │          0.000064 │                                                                    │
│ │ concat    │  0.001133 │      100 │          0.000011 │                                                                    │
│ │ iconcat   │  0.000801 │      100 │          0.000008 │                                                                    │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

SLL Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│              SLL Queue Performance Analysis                                                                                 │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                    │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                    │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                    │
│ │ enqueue   │ 41.262779 │    1,000 │          0.041263 │                                                                    │
│ │ dequeue   │  0.068746 │      500 │          0.000137 │                                                                    │
│ │ peek      │  0.021231 │      333 │          0.000064 │                                                                    │
│ │ concat    │ 33.722232 │      100 │          0.337222 │                                                                    │
│ │ iconcat   │  0.040489 │      100 │          0.000405 │                                                                    │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

ARRAY Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│             ARRAY Queue Performance Analysis                                                                                │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                    │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                    │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                    │
│ │ enqueue   │  0.060772 │    1,000 │          0.000061 │                                                                    │
│ │ dequeue   │  0.096347 │      500 │          0.000193 │                                                                    │
│ │ peek      │  0.026885 │      333 │          0.000081 │                                                                    │
│ │ concat    │  0.003602 │      100 │          0.000036 │                                                                    │
│ │ iconcat   │  0.001578 │      100 │          0.000016 │                                                                    │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

### Joseph Oforkansi

#### Run of systemsense

```wsl

╭──────────────────────────────────── Displaying System Panel Information ────────────────────────────────────╮
│ ┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓              │
│ ┃ System Parameter ┃ Parameter Value                                                         ┃              │
│ ┣━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫              │
│ ┃ battery          ┃ 49.48% battery life remaining, 3:34:11 seconds remaining                ┃              │
│ ┃ cpu              ┃ x86_64                                                                  ┃              │
│ ┃ cpucores         ┃ Physical cores: 6, Logical cores: 12                                    ┃              │
│ ┃ cpufrequencies   ┃ Min: 0.0 Mhz, Max: 0.0 Mhz                                              ┃              │
│ ┃ datetime         ┃ 2025-03-28 00:07:56                                                     ┃              │
│ ┃ disk             ┃ Total: 1006.85 GB, Used: 4.94 GB, Free: 950.70 GB                       ┃              │
│ ┃ hostname         ┃ Ubasinachi                                                              ┃              │
│ ┃ memory           ┃ Total: 3.55 GB, Available: 2.97 GB, Used: 0.42 GB                       ┃              │
│ ┃ platform         ┃ Linux-5.15.167.4-microsoft-standard-WSL2-x86_64-with-glibc2.39          ┃              │
│ ┃ pythonversion    ┃ 3.12.3                                                                  ┃              │
│ ┃ runningprocesses ┃ 30                                                                      ┃              │
│ ┃ swap             ┃ Total: 1.00 GB, Used: 0.00 GB, Free: 1.00 GB                            ┃              │
│ ┃ system           ┃ Linux                                                                   ┃              │
│ ┃ systemload       ┃ (0.09033203125, 0.02294921875, 0.00537109375)                           ┃              │
│ ┃ virtualenv       ┃ /home/oforkansi/.cache/pypoetry/virtualenvs/systemsense-Rt5TvRuf-py3.12 ┃              │
│ ┗━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛              │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────╯


Displaying Benchmark Results

╭────────────────────────────────── Displaying Benchmark Panel Information ───────────────────────────────────╮
│ ┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓                         │
│ ┃ Benchmark Name ┃ Benchmark Results (sec)                                        ┃                         │
│ ┣━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫                         │
│ ┃ addition       ┃ [0.31629270799749065, 0.3047017440003401, 0.30586198799937847] ┃                         │
│ ┃ concatenation  ┃ [1.252448921000905, 1.2106726849997358, 1.196216729000298]     ┃                         │
│ ┃ exponentiation ┃ [3.4946560460011824, 2.8278707829995255, 2.6028115440021793]   ┃                         │
│ ┃ multiplication ┃ [0.46731175999957486, 0.47331768200092483, 0.4569921219990647] ┃                         │
│ ┃ rangelist      ┃ [0.18792873100028373, 0.1763109790008457, 0.17144616799851065] ┃                         │
│ ┗━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Run of Doubling Experiment

```wsl
DLL Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                DLL Queue Doubling Experiment Results                                                          │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                           │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                           │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                           │
│ │      100 │ 0.078146 │ 0.021706 │ 0.005929 │ 0.001395 │ 0.001344 │                                           │
│ │      200 │ 0.204515 │ 0.048069 │ 0.011960 │ 0.000667 │ 0.000349 │                                           │
│ │      400 │ 0.248051 │ 0.056235 │ 0.015726 │ 0.000554 │ 0.000380 │                                           │
│ │      800 │ 0.438154 │ 0.106643 │ 0.029851 │ 0.000493 │ 0.000328 │                                           │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

SLL Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                SLL Queue Doubling Experiment Results                                                          │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                           │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                           │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                           │
│ │      100 │ 0.064944 │ 0.017890 │ 0.007950 │ 0.003057 │ 0.001652 │                                           │
│ │      200 │ 0.216928 │ 0.023132 │ 0.008165 │ 0.001077 │ 0.000482 │                                           │
│ │      400 │ 0.203469 │ 0.047208 │ 0.015469 │ 0.000790 │ 0.000452 │                                           │
│ │      800 │ 0.389417 │ 0.094077 │ 0.078423 │ 0.001128 │ 0.000595 │                                           │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

ARRAY Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│               ARRAY Queue Doubling Experiment Results                                                         │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                           │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                           │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                           │
│ │      100 │ 0.014208 │ 0.011386 │ 0.009879 │ 0.006011 │ 0.000964 │                                           │
│ │      200 │ 0.024209 │ 0.053722 │ 0.016782 │ 0.005693 │ 0.000687 │                                           │
│ │      400 │ 0.031636 │ 0.028630 │ 0.063159 │ 0.008494 │ 0.000677 │                                           │
│ │      800 │ 0.102058 │ 0.097903 │ 0.088619 │ 0.022486 │ 0.001354 │                                           │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                           │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Run of Performance Analysis

```wsl
DLL Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│              DLL Queue Performance Analysis                                                                   │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                      │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                      │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                      │
│ │ enqueue   │  1.033531 │    1,000 │          0.001034 │                                                      │
│ │ dequeue   │  0.136059 │      500 │          0.000272 │                                                      │
│ │ peek      │  0.036996 │      333 │          0.000111 │                                                      │
│ │ concat    │  0.000893 │      100 │          0.000009 │                                                      │
│ │ iconcat   │  0.000914 │      100 │          0.000009 │                                                      │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

SLL Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│              SLL Queue Performance Analysis                                                                   │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                      │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                      │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                      │
│ │ enqueue   │  1.117241 │    1,000 │          0.001117 │                                                      │
│ │ dequeue   │  0.232174 │      500 │          0.000464 │                                                      │
│ │ peek      │  0.051571 │      333 │          0.000155 │                                                      │
│ │ concat    │  0.002783 │      100 │          0.000028 │                                                      │
│ │ iconcat   │  0.001448 │      100 │          0.000014 │                                                      │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

ARRAY Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│             ARRAY Queue Performance Analysis                                                                  │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                      │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                      │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                      │
│ │ enqueue   │  0.121895 │    1,000 │          0.000122 │                                                      │
│ │ dequeue   │  0.121803 │      500 │          0.000244 │                                                      │
│ │ peek      │  0.071548 │      333 │          0.000215 │                                                      │
│ │ concat    │  0.085331 │      100 │          0.000853 │                                                      │
│ │ iconcat   │  0.001982 │      100 │          0.000020 │                                                      │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```


#### Run of Performance Analysis

I am going to talk about the performance analysis of the three queue implementations: SLL, DLL, and Array when running operations like removeFirst, removeLast, addFirst, addLast, peek, dequeue, enqueue, and concat.

First, I want to explain the performance analysis of the SLL queue implementation. The SLL stores a list of elements and accesses the elements in a linear way, so the time complexity of the SLL queue implementation is O(n) for most operations. The SLL has one exception: thanks to its head pointer, the addFirst operation is O(1). For example, in the doubling experiment, the addFirst operation for the SLL took only 0.0065 ms for 1 element, while addLast took 1.0246 ms for 1,000 elements because it requires traversing the list.

The DLL queue implementation stores a list of elements as well, but it accesses the elements in a bidirectional way. This means the time complexity of the DLL for operations with the first and last items, such as addFirst and addLast, is O(1) due to the head and tail pointers. For instance, in the doubling experiment, the addLast operation for the DLL took 0.00353 ms for 100 elements and remained efficient even as the input size increased, taking only 0.0051 ms for 6,400 elements.

What is a head and tail pointer?

These are pointers that reference the first and last elements of the linked list. When removing or adding elements at these positions, the list does not need to shift its elements. Instead, the pointers are updated to reference the next or previous node. In the SLL, there is only a head pointer, while in the DLL, there are both head and tail pointers.

The Array-based Queue implementation uses a list of elements where the time complexity for accessing the first and last elements is O(1). However, adding or removing elements is only O(1) if the operation is at the end of the list. If the operation is at the beginning or in the middle, it becomes O(n) because all the elements need to shift to make space or fill the gap. For example, in the doubling experiment, the addFirst operation for the Array-based Queue took 0.00208 ms for 100 elements but increased to 0.00444 ms for 6,400 elements due to the shifting required.
