# Assignment 4 – Heap Data Structures, Analysis, and Applications

## Course: Algorithms and Data Structures Student: Pranavi Balakulla

This project implements and analyzes Heapsort and a Priority Queue using a Binary Heap, followed by an empirical performance comparison with other sorting algorithms.

## Project Overview
This assignment contains three main components:
1. Heapsort Implementation & Analysis
2. Empirical Comparison (Heapsort vs Quicksort vs Merge Sort)
3. Priority Queue Implementation & Scheduler Simulation
The goal is to study both theoretical complexity and real-world performance behavior of heap-based algorithms.

##  Project Structure
```
├── heapsort.py                 # Heapsort implementation
├── comparison_benchmark.py     # Performance comparison of sorting algorithms
├── priority_queue.py           # Binary heap based priority queue
├── scheduler_simulation.py     # Demonstrates task scheduling using priority queue
└── README.md                   # Project documentation

```

## Requirements 
* Python 3.x
* No external libraries required (standard Python only)

## Running the Programs

### 1. Heapsort

Runs the heap-based sorting algorithm.

### python heapsort.py

### 2. Empirical Comparison

Compares Heapsort, Merge Sort, and Quicksort using different input sizes and distributions.

### python comparison_benchmark.py

The program prints a table showing:

* Input size
* Distribution type
* Algorithm
* Execution time (seconds)

### 3. Priority Queue Scheduler Simulation

Demonstrates how tasks are executed based on priority.

### python scheduler_simulation.py

Example Output:

Task Execution Order (Highest Priority First):
Task(ID=T2, Priority=10)
Task(ID=T4, Priority=8)
Task(ID=T3, Priority=5)
Task(ID=T1, Priority=3)


Concepts Implemented

### Heapsort
* Max-heap construction (O(n))
* Repeated extraction (O(n log n))
* In-place sorting

### Priority Queue
Operations supported:
* insert(task)
* extract_max()
* increase_key()
* decrease_key()
* is_empty()

All core operations run in O(log n) time except is_empty() which runs in O(1).

### Scheduler Simulation
A simple priority-based scheduling system demonstrating practical usage of heaps.

### Complexity Summary
Operation	Time Complexity
Build Heap	O(n)
Heapsort	O(n log n)
Insert	O(log n)
Extract Max	O(log n)
Increase/Decrease Key	O(log n)
is_empty	O(1)

### Key Observations 
* Heapsort provides consistent O(n log n) performance for all input types.
* Quicksort is often faster in practice due to cache locality but lacks worst-case guarantee.
* Merge Sort performs consistently but requires extra memory.
* Priority queues are useful in scheduling systems where urgent tasks must execute first.
