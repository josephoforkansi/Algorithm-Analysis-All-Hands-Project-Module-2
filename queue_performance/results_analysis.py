import json
import matplotlib.pyplot as plt

def load_results(filename="benchmark_results.json"):
    """Load benchmark results from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Run benchmark.py first.")
        return None

def plot_results(results):
    """Plot benchmarking results as bar charts."""
    if not results:
        print("No results to analyze.")
        return

    operations = list(results.keys())
    sll_times = [results[op]["SLL"] for op in operations]
    dll_times = [results[op]["DLL"] for op in operations]
    array_times = [results[op]["Array"] for op in operations]

    x = range(len(operations))

    plt.figure(figsize=(10, 5))
    plt.bar(x, sll_times, width=0.2, label="SLL", align="center")
    plt.bar([i + 0.2 for i in x], dll_times, width=0.2, label="DLL", align="center")
    plt.bar([i + 0.4 for i in x], array_times, width=0.2, label="Array", align="center")

    plt.xticks([i + 0.2 for i in x], operations)
    plt.ylabel("Execution Time (ms)")
    plt.title("Queue Performance Analysis")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.show()

def main():
    """Main function to load and analyze results."""
    results = load_results()
    if results:
        plot_results(results)

if __name__ == "__main__":
    main()
