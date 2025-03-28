# All Hands Project 2

## Introduction

Data structures play a critical role in efficient software development, influencing performance, scalability, and system responsiveness. Among them, queues are fundamental, powering applications such as task scheduling, messaging systems, and real-time data processing. In this project, our team explored three key queue implementations—Singly Linked List (SLL), Doubly Linked List (DLL), and Array-based Queue. This project seeks to answer our research question: What are the performance differences between SLL queue, DLL queue, and array-based queue implementations when executing basic operations (addfirst, addlast, removefirst, removelast, add (+), and iadd (+=)?. We analyzed their performance through benchmarking experiments using SystemSense.

As algorithm engineers tackling this project we considered multiple aspects, including:

- Algorithmic Complexity: Understanding the time and space complexity of queue operations to determine trade-offs between different implementations.

- Memory Management: Evaluating how memory allocation and deallocation affect performance, particularly in linked list-based vs. array-based implementations.

- Concurrency Considerations: Investigating how these data structures behave in multi-threaded environments where multiple processes access and modify queues simultaneously.

- Use Case Optimization: Identifying practical applications where each queue implementation excels, such as high-throughput systems, real-time event processing, and low-latency applications.

- Benchmarking Methodology: Designing experiments to measure execution times, analyze scaling behavior, and compare performance under different workloads.

Through this project, we aim to provide insights into the efficiency of these queue implementations and guide the selection of an optimal data structure based on application requirements. By profiling and analyzing queue operations, we not only enhance our understanding of core data structures but also develop practical skills in performance analysis, a crucial skill in algorithm engineering and systems design.

### Motivation

Efficient data structures are essential in software development, especially when dealing with queues in real-world applications such as scheduling systems, task management, and networking. Different queue implementations like Singly Linked List (SLL), Doubly Linked List (DLL), and Array-based Queue offer trade-offs in terms of performance. Our project aims to benchmark these tradeoffs and analyze the data by comparing the execution times of the queue operations.

# Queue Implementations Analysis

## Queue Structure and FIFO Principle

Queues follow the First-In-First-Out (FIFO) principle where elements are added at the rear and removed from the front, ensuring sequential processing order.

## Implementations Overview

This project explores three queue implementations:

1. **Singly Linked List (SLL) Queue**
   - Uses one-directional nodes with `next` references
   - Maintains both head and tail pointers for efficient operations
   - Each node stores only the value and next reference

2. **Doubly Linked List (DLL) Queue**
   - Uses bidirectional nodes with both `prev` and `next` references
   - Maintains both head and tail pointers
   - Each node stores value, previous, and next references

3. **Array-based Queue**
   - No explicit node structure, just a container of elements
   - Optimized for operations at both ends

## Key Operations

All implementations support these core operations:
- `enqueue`: Add element to the rear (O(1) in all implementations)
- `dequeue`: Remove element from the front (O(1) in all implementations)
- `peek`: View front element without removing (O(1) in all implementations)
- `__add__`: Concatenate queues (O(1) in linked lists, O(n) in array-based)
- `__iadd__`: In-place concatenation (O(1) in linked lists, O(n) in array-based)

### Key Implementation Examples

#### Enqueue Operation (SLL)

```python
def enqueue(self, value: Any) -> None:
    """Add an element to the end of the queue. O(1) operation using tail pointer."""
    new_node = Node(value)
    if self.is_empty():
        self.head = new_node
    else:
        self.tail.next = new_node  # Directly append at tail
    self.tail = new_node  # Update tail pointer
    self.size += 1
```

#### Dequeue Operation (DLL)

```python
def dequeue(self) -> Any:
    """Remove and return the first element from the queue. O(1) operation."""
    if self.is_empty():
        raise IndexError("Queue is empty")
    value = self.head.value
    self.head = self.head.next
    if self.head is None:
        self.tail = None
    else:
        self.head.prev = None
    self.size -= 1
    return value
```

#### Queue Concatenation (Array-based)

```python
def __add__(self, other: "ListQueueDisplay") -> "ListQueueDisplay":
    """Concatenate two queues. O(n) operation."""
    result = ListQueueDisplay()
    result.items = deque(self.items)  # Copy first queue
    result.items.extend(other.items)  # Append second queue
    return result
```

## Implementation Considerations

### SLL Queue Considerations
- Simpler structure with less memory overhead per node
- Forward-only traversal limits some operations
- Uses tail pointer for O(1) enqueue operations
- Efficient concatenation due to tail pointer

### DLL Queue Considerations
- Bidirectional links enable more flexible operations
- Higher memory usage due to extra pointer per node
- All operations including concatenation are O(1)
- Supports easy traversal in both directions

### Array-based Queue Considerations
- No manual pointer management needed
- Leverages efficient implementation of Python's `deque`
- Basic operations are O(1), but concatenation is O(n)
- Internal array may require occasional reallocation

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

```bash
DLL Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                DLL Queue Doubling Experiment Results                                                                                              │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                                                               │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                                                               │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                                                               │
│ │      100 │ 0.023667 │ 0.006667 │ 0.001916 │ 0.000333 │ 0.000417 │                                                                               │
│ │      200 │ 0.073833 │ 0.013459 │ 0.003500 │ 0.000208 │ 0.000167 │                                                                               │
│ │      400 │ 0.115250 │ 0.024208 │ 0.006083 │ 0.000125 │ 0.000125 │                                                                               │
│ │      800 │ 0.200166 │ 0.048375 │ 0.011542 │ 0.000167 │ 0.000166 │                                                                               │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

SLL Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                SLL Queue Doubling Experiment Results                                                                                              │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                                                               │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                                                               │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                                                               │
│ │      100 │ 0.022000 │ 0.005958 │ 0.002292 │ 0.000958 │ 0.000500 │                                                                               │
│ │      200 │ 0.040667 │ 0.011459 │ 0.003500 │ 0.000417 │ 0.000209 │                                                                               │
│ │      400 │ 0.099958 │ 0.020958 │ 0.006125 │ 0.000333 │ 0.000208 │                                                                               │
│ │      800 │ 0.169250 │ 0.041334 │ 0.011708 │ 0.000333 │ 0.000209 │                                                                               │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

ARRAY Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│               ARRAY Queue Doubling Experiment Results                                                                                             │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                                                               │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                                                               │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                                                               │
│ │      100 │ 0.003791 │ 0.003334 │ 0.002459 │ 0.001833 │ 0.000250 │                                                                               │
│ │      200 │ 0.007083 │ 0.006166 │ 0.004667 │ 0.001917 │ 0.000208 │                                                                               │
│ │      400 │ 0.014125 │ 0.013125 │ 0.009208 │ 0.003375 │ 0.000292 │                                                                               │
│ │      800 │ 0.027542 │ 0.026292 │ 0.017792 │ 0.006417 │ 0.000375 │                                                                               │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### Run of Performance Analysis

```bash
oetry run analyze analyze                                     

DLL Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│              DLL Queue Performance Analysis                                                                                                       │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                                          │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                                          │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                                          │
│ │ enqueue   │  0.258167 │    1,000 │          0.000258 │                                                                                          │
│ │ dequeue   │  0.060583 │      500 │          0.000121 │                                                                                          │
│ │ peek      │  0.015292 │      333 │          0.000046 │                                                                                          │
│ │ concat    │  0.000334 │      100 │          0.000003 │                                                                                          │
│ │ iconcat   │  0.000417 │      100 │          0.000004 │                                                                                          │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                                                          │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

SLL Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│              SLL Queue Performance Analysis                                                                                                       │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                                          │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                                          │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                                          │
│ │ enqueue   │  0.196000 │    1,000 │          0.000196 │                                                                                          │
│ │ dequeue   │  0.050458 │      500 │          0.000101 │                                                                                          │
│ │ peek      │  0.014625 │      333 │          0.000044 │                                                                                          │
│ │ concat    │  0.000791 │      100 │          0.000008 │                                                                                          │
│ │ iconcat   │  0.000500 │      100 │          0.000005 │                                                                                          │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                                                          │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

ARRAY Queue Implementation
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│             ARRAY Queue Performance Analysis                                                                                                      │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                                          │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                                          │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                                          │
│ │ enqueue   │  0.043708 │    1,000 │          0.000044 │                                                                                          │
│ │ dequeue   │  0.029083 │      500 │          0.000058 │                                                                                          │
│ │ peek      │  0.019541 │      333 │          0.000059 │                                                                                          │
│ │ concat    │  0.007208 │      100 │          0.000072 │                                                                                          │
│ │ iconcat   │  0.000625 │      100 │          0.000006 │                                                                                          │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                                                          │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

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
│ │      100 │ 0.039566 │ 0.011458 │ 0.003488 │ 0.000625 │ 0.000858 │                                                         │
│ │      200 │ 0.113858 │ 0.022507 │ 0.006425 │ 0.000403 │ 0.000311 │                                                         │
│ │      400 │ 0.202240 │ 0.047851 │ 0.012279 │ 0.000379 │ 0.000280 │                                                         │
│ │      800 │ 0.361492 │ 0.094825 │ 0.022960 │ 0.000330 │ 0.000355 │                                                         │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

SLL Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│                SLL Queue Doubling Experiment Results                                                                        │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                                         │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                                         │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                                         │
│ │      100 │ 0.078195 │ 0.014763 │ 0.003961 │ 0.001582 │ 0.000946 │                                                         │
│ │      200 │ 0.070928 │ 0.019607 │ 0.006181 │ 0.000761 │ 0.000489 │                                                         │
│ │      400 │ 0.176146 │ 0.049838 │ 0.012285 │ 0.000710 │ 0.000490 │                                                         │
│ │      800 │ 0.309921 │ 0.083965 │ 0.024419 │ 0.000687 │ 0.000442 │                                                         │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

ARRAY Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│               ARRAY Queue Doubling Experiment Results                                                                       │
│ ╭──────────┬──────────┬──────────┬──────────┬──────────┬──────────╮                                                         │
│ │ Size (n) │  enqueue │  dequeue │     peek │   concat │  iconcat │                                                         │
│ ├──────────┼──────────┼──────────┼──────────┼──────────┼──────────┤                                                         │
│ │      100 │ 0.007520 │ 0.006178 │ 0.004555 │ 0.002887 │ 0.000509 │                                                         │
│ │      200 │ 0.013283 │ 0.012204 │ 0.008401 │ 0.002614 │ 0.000355 │                                                         │
│ │      400 │ 0.026229 │ 0.025153 │ 0.016454 │ 0.007943 │ 0.000658 │                                                         │
│ │      800 │ 0.110293 │ 0.075074 │ 0.031935 │ 0.009347 │ 0.000694 │                                                         │
│ ╰──────────┴──────────┴──────────┴──────────┴──────────┴──────────╯                                                         │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Plots saved to results directory

```

#### Run of Performance Analysis

```bash

DLL Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│              DLL Queue Performance Analysis                                                                                 │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                    │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                    │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                    │
│ │ enqueue   │  0.477277 │    1,000 │          0.000477 │                                                                    │
│ │ dequeue   │  0.117047 │      500 │          0.000234 │                                                                    │
│ │ peek      │  0.032079 │      333 │          0.000096 │                                                                    │
│ │ concat    │  0.000720 │      100 │          0.000007 │                                                                    │
│ │ iconcat   │  0.000936 │      100 │          0.000009 │                                                                    │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

SLL Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│              SLL Queue Performance Analysis                                                                                 │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                    │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                    │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                    │
│ │ enqueue   │  0.411052 │    1,000 │          0.000411 │                                                                    │
│ │ dequeue   │  0.106158 │      500 │          0.000212 │                                                                    │
│ │ peek      │  0.031625 │      333 │          0.000095 │                                                                    │
│ │ concat    │  0.002308 │      100 │          0.000023 │                                                                    │
│ │ iconcat   │  0.001400 │      100 │          0.000014 │                                                                    │
│ ╰───────────┴───────────┴──────────┴───────────────────╯                                                                    │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

ARRAY Queue Implementation
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│             ARRAY Queue Performance Analysis                                                                                │
│ ╭───────────┬───────────┬──────────┬───────────────────╮                                                                    │
│ │ Operation │ Time (ms) │ Elements │ Time/Element (ms) │                                                                    │
│ ├───────────┼───────────┼──────────┼───────────────────┤                                                                    │
│ │ enqueue   │  0.115217 │    1,000 │          0.000115 │                                                                    │
│ │ dequeue   │  0.069180 │      500 │          0.000138 │                                                                    │
│ │ peek      │  0.044262 │      333 │          0.000133 │                                                                    │
│ │ concat    │  0.012812 │      100 │          0.000128 │                                                                    │
│ │ iconcat   │  0.001020 │      100 │          0.000010 │                                                                    │
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
