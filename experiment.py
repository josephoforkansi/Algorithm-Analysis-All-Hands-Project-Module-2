import time
import csv
from data_structures import SLLQueue, DLLDeque, ArrayQueue

def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time

def run_experiment(data_structure, operation, size, num_operations=1000):
    times = []
    for _ in range(num_operations):
        instance = None
        if data_structure == "SLLQueue":
            instance = SLLQueue()
        elif data_structure == "DLLDeque":
            instance = DLLDeque()
        elif data_structure == "ArrayQueue":
            instance = ArrayQueue()

        # Fill the initial structure
        for i in range(size):
            instance.add_last(i)

        start_time = time.perf_counter()
        if operation == "add_first":
            instance.add_first(-1)
        elif operation == "add_last":
            instance.add_last(size)
        elif operation == "remove_first":
            instance.remove_first()
        elif operation == "remove_last":
            if isinstance(instance, DLLDeque): # Only DLLDeque has remove_last efficiently
                instance.remove_last()
            elif isinstance(instance, ArrayQueue) and instance.items:
                instance.items.pop() # Simulate remove last for array
            elif isinstance(instance, SLLQueue):
                # Removing last in SLL is O(n), not ideal for benchmarking this way
                pass # You might want to handle this differently or skip for SLL
        elif operation == "add":
            # Assuming 'add' means adding an element at a specific index (e.g., middle)
            if instance.items and isinstance(instance, ArrayQueue):
                instance.items.insert(size // 2, -1)
            elif isinstance(instance, (SLLQueue, DLLDeque)):
                # For linked lists, adding at a specific index requires traversal
                pass # You might want to implement this if needed
        elif operation == "iadd":
            # Assuming 'iadd' means adding multiple elements (e.g., a list)
            if isinstance(instance, ArrayQueue):
                instance.items.extend(range(10)) # Add a small range
            elif isinstance(instance, (SLLQueue, DLLDeque)):
                for i in range(10):
                    instance.add_last(i) # Or add_first, depending on interpretation
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return sum(times) / num_operations # Return average time

if __name__ == "__main__":
    data_structures_to_test = ["SLLQueue", "DLLDeque", "ArrayQueue"]
    operations_to_test = ["add_first", "add_last", "remove_first", "remove_last", "add", "iadd"]
    sizes = [100, 200, 400, 800, 1600] # Doubling sizes
    num_repetitions = 5 # Number of times to run each experiment for averaging

    results = []

    with open("results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Data Structure", "Operation", "Size", "Average Time"])

        for ds in data_structures_to_test:
            for op in operations_to_test:
                for size in sizes:
                    all_times = []
                    for _ in range(num_repetitions):
                        time_taken = run_experiment(ds, op, size)
                        all_times.append(time_taken)
                    avg_time = sum(all_times) / num_repetitions
                    results.append([ds, op, size, avg_time])
                    writer.writerow([ds, op, size, avg_time])

    print("Experiment finished. Results saved to results.csv")
