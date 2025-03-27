"""Main module for queue implementation analysis."""

from typing import Type, Any, Dict, List, Callable
import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from time import perf_counter
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

from analyze.DLL import Queue as DLLQueue
from analyze.SLL import BasicSLLQueue as SLLQueue
from analyze.ListQueue import ListQueueDisplay as ArrayQueue
from analyze.timer import TimingResult
from analyze.queue_approach import QueueApproach

# Create console for rich output
console = Console()

# Create Typer app
app = typer.Typer(
    help="Queue Implementation Performance Analysis Tool",
    add_completion=False,
    no_args_is_help=True,
)

# Map queue implementations to their classes
QUEUE_IMPLEMENTATIONS: Dict[QueueApproach, Type[Any]] = {
    QueueApproach.dll: DLLQueue,
    QueueApproach.sll: SLLQueue,
    QueueApproach.array: ArrayQueue,
}


def time_operation(func: Callable[[], None]) -> float:
    """Time an operation using high-precision counter."""
    start_time = perf_counter()
    try:
        func()
    except Exception as e:
        console.print(f"[red]Error during operation: {str(e)}[/red]")
        return 0.0
    return perf_counter() - start_time


def get_operation_function(operation: str, queue: Any, size: int) -> Callable[[], None]:
    """Get the operation function for timing."""
    if operation == "enqueue":
        # Time a single enqueue operation
        return lambda: queue.enqueue(size)
    elif operation == "dequeue":
        # Time a single dequeue operation
        return lambda: queue.dequeue()
    elif operation == "peek":
        return lambda: queue.peek()
    elif operation == "concat":
        # Create other queue once and reuse it
        other = queue.__class__()
        for i in range(size // 10):
            other.enqueue(i)
        return lambda: queue + other
    elif operation == "iconcat":
        # Create other queue once and reuse it
        other = queue.__class__()
        for i in range(size // 10):
            other.enqueue(i)
        return lambda: queue.__iadd__(other)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def run_tests(queue_class: Type[Any], size: int) -> TimingResult:
    """Run performance tests on a queue implementation."""
    if size <= 0:
        raise ValueError("Size must be positive")

    queue = queue_class()

    try:
        # Test enqueue
        enqueue_time = time_operation(lambda: [queue.enqueue(i) for i in range(size)])
        queue.timing_result.add_timing("enqueue", enqueue_time, size)

        # Test dequeue
        dequeue_count = size // 2
        dequeue_time = time_operation(
            lambda: [queue.dequeue() for _ in range(dequeue_count)]
        )
        queue.timing_result.add_timing("dequeue", dequeue_time, dequeue_count)

        # Test peek
        peek_count = size // 3
        peek_time = time_operation(lambda: [queue.peek() for _ in range(peek_count)])
        queue.timing_result.add_timing("peek", peek_time, peek_count)

        # Test length and empty checks
        check_count = size // 4
        check_time = time_operation(
            lambda: [len(queue) or queue.is_empty() for _ in range(check_count)]
        )
        queue.timing_result.add_timing("length/empty", check_time, check_count)

        return queue.timing_result
    finally:
        # Clean up
        del queue


def plot_results(results: Dict[str, List[float]], sizes: List[int], title: str):
    """Plot timing results."""
    plt.figure(figsize=(10, 6))
    for operation, times in results.items():
        plt.plot(sizes, times, marker='o', label=operation)
    plt.title(title)
    plt.xlabel('Size (n)')
    plt.ylabel('Time (ms)')
    plt.grid(True)
    plt.legend()
    
    # Create results directory if it doesn't exist
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    
    # Save plot with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.savefig(results_dir / f"{title.lower().replace(' ', '_')}_{timestamp}.png")
    plt.close()


def display_results(results: List[TimingResult], size: int):
    """Display timing results in a formatted table."""
    for result in results:
        table = Table(
            title=f"{result.name} Queue Implementation Performance Analysis",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("Operation", style="cyan")
        table.add_column("Time (ms)", justify="right")
        table.add_column("Elements", justify="right")
        table.add_column("Time/Element (ms)", justify="right")

        for operation, (total_time, total_elements) in result.operations.items():
            time_per_element = total_time / total_elements if total_elements > 0 else 0
            table.add_row(
                operation,
                f"{total_time:.6f}",
                f"{total_elements:,}",
                f"{time_per_element:.6f}",
            )

        console.print(Panel(table, title=f"Size: {size:,}"))


@app.command()
def analyze(
    size: int = typer.Option(1000, help="Size of queue for testing"),
    dll: bool = typer.Option(False, help="Test DLL implementation"),
    sll: bool = typer.Option(False, help="Test SLL implementation"),
    array: bool = typer.Option(False, help="Test Array implementation"),
):
    """Run performance analysis on queue implementations."""
    if not any([dll, sll, array]):
        console.print("[yellow]Please specify at least one implementation to test[/yellow]")
        return

    results = []
    for approach, queue_class in QUEUE_IMPLEMENTATIONS.items():
        if (approach == QueueApproach.dll and dll) or \
           (approach == QueueApproach.sll and sll) or \
           (approach == QueueApproach.array and array):
            try:
                result = run_tests(queue_class, size)
                results.append(result)
            except Exception as e:
                console.print(f"[red]Error testing {approach.value}: {str(e)}[/red]")

    display_results(results, size)


@app.command()
def doubling(
    initial_size: int = typer.Option(100, help="Initial size for doubling experiment"),
    max_size: int = typer.Option(1000, help="Maximum size for doubling experiment"),
    dll: bool = typer.Option(False, help="Test DLL implementation"),
    sll: bool = typer.Option(False, help="Test SLL implementation"),
    array: bool = typer.Option(False, help="Test Array implementation"),
):
    """Run doubling experiment on queue implementations."""
    if not any([dll, sll, array]):
        console.print("[yellow]Please specify at least one implementation to test[/yellow]")
        return

    sizes = []
    current_size = initial_size
    while current_size <= max_size:
        sizes.append(current_size)
        current_size *= 2

    for approach, queue_class in QUEUE_IMPLEMENTATIONS.items():
        if (approach == QueueApproach.dll and dll) or \
           (approach == QueueApproach.sll and sll) or \
           (approach == QueueApproach.array and array):
            try:
                results = {
                    "concat": [],
                    "dequeue": [],
                    "enqueue": [],
                    "iconcat": [],
                    "peek": []
                }

                for size in sizes:
                    queue = queue_class()
                    
                    # Fill queue
                    for i in range(size):
                        queue.enqueue(i)

                    # Test each operation
                    for operation in results.keys():
                        func = get_operation_function(operation, queue, size)
                        time_taken = time_operation(func)
                        results[operation].append(time_taken)

                # Plot results
                plot_results(results, sizes, f"{approach.value.upper()} Queue Doubling Experiment")

                # Display results in table
                table = Table(
                    title=f"{approach.value.upper()} Queue Doubling Experiment Results",
                    box=box.ROUNDED,
                    show_header=True,
                    header_style="bold magenta",
                )
                table.add_column("Size (n)", justify="right")
                for operation in results.keys():
                    table.add_column(operation, justify="right")

                for i, size in enumerate(sizes):
                    row = [f"{size:,}"]
                    for operation in results.keys():
                        row.append(f"{results[operation][i]:.6f}")
                    table.add_row(*row)

                console.print(Panel(table))

            except Exception as e:
                console.print(f"[red]Error testing {approach.value}: {str(e)}[/red]")

    # Create combined plots
    for operation in ["concat", "dequeue", "enqueue", "iconcat", "peek"]:
        plt.figure(figsize=(10, 6))
        for approach, queue_class in QUEUE_IMPLEMENTATIONS.items():
            if (approach == QueueApproach.dll and dll) or \
               (approach == QueueApproach.sll and sll) or \
               (approach == QueueApproach.array and array):
                queue = queue_class()
                times = []
                for size in sizes:
                    # Fill queue
                    for i in range(size):
                        queue.enqueue(i)
                    # Test operation
                    func = get_operation_function(operation, queue, size)
                    time_taken = time_operation(func)
                    times.append(time_taken)
                plt.plot(sizes, times, marker='o', label=approach.value.upper())

        plt.title(f"Combined {operation} Operation")
        plt.xlabel('Size (n)')
        plt.ylabel('Time (ms)')
        plt.grid(True)
        plt.legend()
        
        # Save combined plot
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plt.savefig(Path("results") / f"combined_{operation}_{timestamp}.png")
        plt.close()


if __name__ == "__main__":
    app()
