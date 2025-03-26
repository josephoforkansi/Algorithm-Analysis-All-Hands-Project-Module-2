# All Hands Project 2

## Introduction

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

Our Project explores three queue implementations: Singly Linked List (SLL) Queue, Doubly Linked List (DLL) Queue, and Array-based Queue. Each implementation is different in its structure, performance, and memory efficiency but supports fundamental queue operations.

### Singly Linked List (SLL) Queue

#### SLL Considerations

### Doubly Linked List (DLL) Queue

#### DLL Considerations

### Array-based Queue

#### Array-based Queue Considerations

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



### Replace with name

#### Run of systemsense

#### Run of Doubling Experiment

#### Run of Performance Analysis



### Replace with name

#### Run of systemsense

#### Run of Doubling Experiment

#### Run of Performance Analysis



### Replace with name

#### Run of systemsense

#### Run of Doubling Experiment

#### Run of Performance Analysis



### Replace with name

#### Run of systemsense

#### Run of Doubling Experiment

#### Run of Performance Analysis