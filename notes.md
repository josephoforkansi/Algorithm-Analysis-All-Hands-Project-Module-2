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

To run the benchmarking tool, please install Poetry on your device. Navigate to the project directory and install dependencies if you have not already:

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

This command will provide execution times for operations like `addList`, `dequeue`, and `enqueue` to compare efficiency.

## Output Analysis

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



### Replace with name

#### Run of systemsense

#### Run of Doubling Experiment

#### Run of Performance Analysis
